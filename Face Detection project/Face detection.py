import cv2
# import numpy as np
import face_recognition

# imgAnish = cv2.VideoCapture(0)
# result= True
# while(result):
#     ret,frame = imgAmit.read()
#     cv2.imwrite("Amit-test.jpg",frame)
#     result=False
# imgAmit.release()
# cv2.destroyWindow()

imgElon = face_recognition.load_image_file("Amit-Shah.jpg")
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file("Amit-test.jpg")
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
# print(faceLoc)   #this gives the co-ordinates of face location

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeElonTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

results = face_recognition.compare_faces([encodeElon], encodeElonTest)
faceDisplay = face_recognition.face_distance([encodeElon], encodeElonTest)
cv2.putText(imgTest, f'{results} {round(faceDisplay[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Amit Shah', imgElon)
cv2.imshow("Amit Test", imgTest)
cv2.waitKey(0)
