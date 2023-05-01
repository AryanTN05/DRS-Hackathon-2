# Emotion Detector for Online Classes
This is a machine learning model that uses facial recognition technology to detect the emotions and behavior patterns of students during online classes. The purpose of this project is to help teachers pay special attention to students who may need extra support.

# Problem Statement
India is home to 8 million children with disabilities, and only 61% of children with disabilities aged between 5 and 19 are attending educational institutions, according to UNICEF. The lack of accessible physical infrastructure, assistive technologies, information and communication technology, and devices aggravates the situation of school dropout among disabled children.

# Solution
The pandemic has made it challenging for students with special needs to attend physical schools. Therefore, online classes have become a viable alternative. This model uses facial recognition technology to detect the emotions and behavior patterns of students during online classes. The model alerts teachers to pay special attention to students who may need extra support, thus helping to improve their learning experience.

# Usage
To use this model, you will need to have a computer with a webcam and an internet connection. You can run the model on your local machine by cloning the repository and running the script. The model will use your webcam to analyze your facial expressions and provide feedback on your emotions and behavior patterns.

# How Does It Work?
This script searches for the student's face, then use the dlib library to predict 68 facial keypoints. The enumeration and location of all the face keypoints/landmarks can be seen here.

With those keypoints, the following scores are computed:

* Blink Score: The blink score is calculated by counting the number of times the student blinks during the class. If the student is blinking too much, it may indicate drowsiness or distraction.
* Head Pose: The head pose is calculated by tracking the orientation of the student's head. If the head is tilted or turned away for a prolonged period of time, it may indicate disinterest or discomfort.

The student's states can be classified as:
* Normal: no messages are printed
* Distracted: when the attention score is lower than a certain threshold for a certain amount of time, a warning message is printed on screen
* Uninterested: when the head pose score is higher than a certain threshold for a certain amount of time, a warning message is printed on screen
* Drowsy: when the blink score is higher than a certain threshold for a certain amount of time, a warning message is printed on screen
* Engaged: when the smile score is higher than a certain threshold, it indicates that the student is happy and engaged in the class.

Note: This script is specifically designed to help students with special needs to ensure they are receiving the necessary attention and support during their online classes.
