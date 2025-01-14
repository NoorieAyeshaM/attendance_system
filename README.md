FACE RECOGNITION ATTENDANCE SYSTEM:

1.OVERVIEW:

This project is a face recognition-based attendance system that uses a pre-trained Keras model to identify individuals in real-time through a webcam. Attendance is recorded in a MySQL database with checks to prevent duplicate entries for the same person on the same day.

2.FEATURES:

* Real-time face recognition using a webcam feed.

* Integration with MySQL database for attendance management.

* Ensures attendance is marked only once per day per individual.

* Ignores unrecognized faces labeled as "Unknown."

* User-friendly design with minimal configuration required.

3.PREREQUISITES:

Before running this project, ensure you have the following:

SOFTWARE REQUIREMENTS:

* Python (version 3.9)

* MySQL server installed and running.

4.FILE STRUCTURE:

* keras_model.h5: Pre-trained Keras model file.

* labels.txt: Text file with class names for the model.

* attendance_system.py: Main Python script for running the program.

5.HOW IT WORKS:

Workflow:

* Initialization: Load the model, labels, and connect to the MySQL database.

* Camera Setup: Open the webcam and start capturing frames.

* Face Recognition: Process each frame, predict identity, and check confidence score (>90%).

* Attendance Marking: Record attendance in the database if not already marked for the day.

* Exit: Press ESC to safely close the camera and database connection.

6.CUSTOMIZATION:

* Change Database Configuration: Update credentials and modify the attendance table as needed.
  
* Adjust Confidence Threshold: Modify the threshold (confidence_score > 0.90) for recognition.

* Replace keras_model.h5 with a custom model trained for their use case.

* Update labels.txt with corresponding class names.

* Change the video source (e.g., use a video file instead of a camera).

7.STEP BY STEP PROCEDURE TO MAKE THE PROJECT RUN SUCCESSFULLY:

Step 1: Install Python:

Download Python from python.org/downloads and install it on your system. During installation, ensure you check the box to add Python to your PATH.

Step 2:Install MySQL Workbench:

GO THROUGH THIS LINK FOR INSTALLATION: https://youtu.be/hiS_mWZmmI0?si=4cxyEo_w0Cv2GQ6B

Step 3:Install PyCharm:

Step 1:Download PyCharm from jetbrains.com/pycharm/download and install it. PyCharm will serve as your development environment to write and execute Python programs. 

Step 2: Create a New Python Project in PyCharm Launch PyCharm and select New Project. Choose a project directory and ensure Python is selected as the interpreter.

Step 3: Create a Python File In the project folder, right-click and select New > Python File. Name the file face_recognition_py. 

Step 4: Import Required Libraries Open the attendance_system.py file.(install these in the terminal of the project located in the bottom left side)

1.Install TensorFlow 2.10.0:
pip install tensorflow==2.10.0

2.Install Numpy (compatible version):
pip install numpy==1.21.6

set CUDA_VISIBLE_DEVICES=-1

3.Install OpenCV with  GUI suport:
pip install opencv-python==4.5.5.64

STEP 5: Load a Pre-Trained Face Detection Model use google teacheable Machines to create pre trained model using the steps

8.STEPS TO BE FOLLOWED TO TRAIN THE MODEL:

1.Search for google teachable machine

![pic-1](https://github.com/user-attachments/assets/0bc2094c-8aaa-4e51-82d3-3476b2a0a6a8)

2.Select get started

![oic-2](https://github.com/user-attachments/assets/5c34d813-eed1-4b91-b4e5-d759b812edc8)

3.Select image project

![pic-3](https://github.com/user-attachments/assets/c232140d-5840-4d6f-8c6d-a3441ee5ea1e)

4.Select standard image model

![pic-4](https://github.com/user-attachments/assets/6b1c9f6f-aa0a-47f0-aada-8829c62e3ef1)

5.Add class name (eg.yourname) click on web cam and record your face with 3-4 angles,train the model and then check the output then export the model

![pic-5](https://github.com/user-attachments/assets/0abe8da3-783f-4e2e-904f-d3434e6b8e4b)

6.Select Tensorflow----OpenCVKeras----Download my model

![pic-6](https://github.com/user-attachments/assets/d1bc8541-c3db-4de9-8e5e-d281d7baeffd)

9.SQL QUERY:

![sql](https://github.com/user-attachments/assets/842a2681-13b3-4151-9463-c92ce6a9e72f)

10.COMPLETE CODE:

![image](https://github.com/user-attachments/assets/09852900-04ac-46df-8d10-c84de2798e8e)

![image](https://github.com/user-attachments/assets/c4fb65a3-5a62-40f3-a8e8-31276a322197)

![image](https://github.com/user-attachments/assets/b80b4607-b846-4a3c-9b90-edc71d2bee91)

![image](https://github.com/user-attachments/assets/37d3836d-3974-40ce-95a6-bb9b8806dce0)

EXECUTE THE SCRIPT:

![image](https://github.com/user-attachments/assets/cacdb3f2-876d-4846-8e8b-46099e02f4e0)

OUTPUT OF THE MODEL:

![output 2](https://github.com/user-attachments/assets/a22a153c-6ec0-4251-be0e-556ae7f75850)

Go to mysql workbench and PARTICULARLY run only this query:

![image](https://github.com/user-attachments/assets/544458a6-cfcd-4c3a-aa2f-56a4a2ea0f1d)

After executing the script you will see the updated database table:

![sql-output](https://github.com/user-attachments/assets/2794ab62-c1d2-4bd1-bc2d-74fc420b8127)

11.TROUBLESHOOTING:

* Database Connection Issues: Error:- Error connecting to database

Solution: * Ensure MySQL server is running.

          * Verify the database credentials (username, password, host, and database name).

          * Check if the attendance_system database and attendance table exist.

* Camera Not Accessible: Ensure no other application is using the camera.

*  MySQL Query Errors: Error:- Error marking attendance

Solution: * Verify the attendance table schema matches the INSERT query fields.

          * Face Not Recognized: Issue:- Known faces are not being detected.

Solution: * Ensure the face data was included when the model was trained.

          * Check lighting conditions and camera angle for clear face visibility.


  
