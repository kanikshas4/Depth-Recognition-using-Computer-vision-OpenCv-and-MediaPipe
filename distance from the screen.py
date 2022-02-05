#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import cvzone
import mediapipe as mp
from cvzone.FaceMeshModule import FaceMeshDetector
cap=cv2.VideoCapture(0)
detector= FaceMeshDetector(maxFaces=1)
while True:
    rat,frame=cap.read()
    frame, faces = detector.findFaceMesh(frame)
    
    if faces:
        face= faces[0]
        pointLeft=face[145]
        pointRight=face[374]
        cv2.line(frame,pointLeft,pointRight,(0,200,0),3)
        cv2.circle(frame,pointRight,5,(255,0,255),cv2.FILLED)
        cv2.circle(frame,pointLeft,5,(255,0,255),cv2.FILLED)
        
        w, _= detector.findDistance(pointLeft,pointRight)
        W=6.3
        #focal length
        
        #d=50
       # f=(w*d)/W
        #print(f)
        f=1120
        d=(W*f)/w
        #print(d)
        
        cvzone.putTextRect(frame,f'Depth: {int(d)}cm',
                       (face[10][0]-100,face[10][1]-50),
                       scale=2)
       
        
    cv2.imshow('frame',frame)
    cv2.waitKey(1)


# In[ ]:




