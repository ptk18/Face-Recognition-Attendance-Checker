import cv2
import numpy as np
import face_recognition

person1 = face_recognition.load_image_file('images/elon1.jpg')
person1 = cv2.cvtColor(person1, cv2.COLOR_BGR2RGB)

person2 = face_recognition.load_image_file('images/billGate.jpeg')
person2 = cv2.cvtColor(person2, cv2.COLOR_BGR2RGB)

facelocation1 = face_recognition.face_locations(person1)[0]
print(facelocation1)
cv2.rectangle(person1, (facelocation1[3], facelocation1[0]), (facelocation1[1], facelocation1[2]), (57, 255, 20), 3)
encodePerson1 = face_recognition.face_encodings(person1)[0]
print(encodePerson1)

facelocation2 = face_recognition.face_locations(person2)[0]
print(facelocation2)
cv2.rectangle(person2, (facelocation2[3], facelocation2[0]), (facelocation2[1], facelocation2[2]), (57, 255, 20), 3)
encodePerson2 = face_recognition.face_encodings(person2)[0]
print(encodePerson2)

isSamePerson = face_recognition.compare_faces([encodePerson1],encodePerson2)
print(isSamePerson)

#in some cases, there can be simlarity in some different persons' faces
#will check face distance to know how similar the faces are
#the lower the distance, the better the match is 
faceDistance = face_recognition.face_distance([encodePerson1],encodePerson2)
print(faceDistance)

cv2.putText(person2,f'{isSamePerson} {round(faceDistance[0],2)}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)


cv2.imshow('Elon Musk 1', person1)
cv2.imshow('Bill Gate', person2)
cv2.waitKey(0)
