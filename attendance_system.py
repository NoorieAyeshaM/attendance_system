import cv2
import numpy as np
from keras.models import load_model
import mysql.connector
from datetime import datetime
import os

# Suppress TensorFlow GPU warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load the model
model = load_model(r"C:\Users\noori\PycharmProjects\face_recognition_attendance\keras_model.h5", compile=False)

# Load the labels
try:
    with open("labels.txt", "r") as file:
        class_names = file.readlines()
except FileNotFoundError:
    print("Error: labels.txt file not found.")
    exit()

# Connect to MySQL database
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # Your MySQL username
        password="ayeshamub@04",  # Your MySQL password
        database="attendance_system"  # Your database name
    )
    cursor = conn.cursor()
    print("Database connected successfully.")
except mysql.connector.Error as e:
    print(f"Error connecting to database: {e}")
    exit()

# CAMERA settings
camera_index = 0  # Change index if needed (e.g., 1 or 2)
camera = cv2.VideoCapture(camera_index)

# Check if the camera opened successfully
if not camera.isOpened():
    print(f"Error: Camera with index {camera_index} not accessible.")
    exit()

# Helper function to mark attendance
def mark_attendance(person_name):
    current_date = datetime.now().strftime('%Y-%m-%d')  # Get today's date
    current_time = datetime.now().strftime('%H:%M:%S')  # Get current time

    try:
        # Check if the person has already been marked for the day
        cursor.execute("SELECT * FROM attendance WHERE person_name = %s AND date = %s", (person_name, current_date))
        record = cursor.fetchone()

        if record:
            print(f"Attendance for {person_name} already marked today.")
        else:
            # Mark attendance if not already marked for today
            cursor.execute(""" 
                INSERT INTO attendance (person_name, attendance, date, time)
                VALUES (%s, %s, %s, %s)
            """, (person_name, 1, current_date, current_time))
            conn.commit()
            print(f"Attendance marked for {person_name} at {current_time}")
    except Exception as e:
        print(f"Error marking attendance: {e}")

# Initialize attendance tracking variables
last_detected_person = ""
already_notified = False

while True:
    # Grab the webcam image
    ret, image = camera.read()

    if not ret:
        print("Failed to grab image. Exiting...")
        break

    # Resize image to match model input
    image_resized = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    cv2.imshow("Webcam Image", image)

    # Prepare the image for prediction
    image_array = np.asarray(image_resized, dtype=np.float32).reshape(1, 224, 224, 3)
    image_array = (image_array / 127.5) - 1  # Normalize image

    # Get predictions
    prediction = model.predict(image_array, verbose=0)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    # If confidence is above 90%, mark attendance
    if confidence_score > 0.90:
        if class_name.lower() != "unknown":  # Ensure "unknown" is not marked as present
            if class_name != last_detected_person:
                print(f"Detected: {class_name}, Confidence: {confidence_score * 100:.2f}%")
                mark_attendance(class_name)
                last_detected_person = class_name
                already_notified = False  # Reset the flag for the new person
            elif not already_notified:
                print(f"{class_name} is still in front of the camera.")
                already_notified = True  # Prevent duplicate notifications
        else:
            print(f"Unknown detected, not marking attendance.")

    # Listen to the keyboard for presses (press ESC to exit)
    keyboard_input = cv2.waitKey(1)

    if keyboard_input == 27:  # ESC key to quit
        break

# Release resources and close window
camera.release()
cv2.destroyAllWindows()
conn.close()
