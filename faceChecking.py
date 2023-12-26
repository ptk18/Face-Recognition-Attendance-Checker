import cv2
import numpy as np
import face_recognition
import os

path = 'imagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for i in myList:
    currentImage = cv2.imread(f'{path}/{i}')
    images.append(currentImage)
    classNames.append(os.path.splitext(i)[0])
  
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    #since we are capturing real-time image, reducing image size can help our program run faster
    imgSmall = cv2.resize(img,(0,0),None,0.25,0.25) #one fourth of the original size
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)
    
    #for dectecting face in web cam can find many faces if you're in crowded place. so we have to find the locations of the face that we want to track
    facesInCurrentFrame = face_recognition.face_locations(imgSmall)
    encodesInCurrentFrame = face_recognition.face_encodings(imgSmall,facesInCurrentFrame)
    
    for encodeFace, faceLoc in zip(encodesInCurrentFrame,facesInCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDistance)
        matchIndex = np.argmin(faceDistance) #will give the index
        
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            
            y1,x2,y2,x1 = faceLoc
            y1,x2,y2,x1 = y1*4 ,x2*4 ,y2*4 ,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED) 
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        
    cv2.imshow('webcam',img)
    cv2.waitKey(1)