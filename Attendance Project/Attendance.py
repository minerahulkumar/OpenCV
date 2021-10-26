import cv2
import face_recognition
import numpy as np
import os

# ***** Below code adds image manually ****
"""
imgRahul = face_recognition.load_image_file("Rahul.jpg")
imgRahul = cv2.cvtColor(imgRahul, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file("Rahul-test.jpg")
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
"""

# ***** Find number of images automatically and find there encodings
path = "Attendance Resources"
images = []  # this will have all the images
classNames = []  # contain names of all images with extension
mylist = os.listdir(path)
# print(mylist)

for cls in mylist:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    # this will split name with extension and append name to studImgNames
    classNames.append(os.path.splitext(cls)[0])
# print(studImgNames)  # this list will have names without extension

# ***** function to find all the encodings *******
def findEncodings(images):







