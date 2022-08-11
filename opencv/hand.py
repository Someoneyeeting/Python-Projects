import cv2
import time
import os
import handTrackingModule as hm

detector = hm.handDetector(detectionCon=1)

cam = cv2.VideoCapture(0)
cam.set(3,300)
cam.set(4,400)

ctime = time.time()
prevtime = ctime

while True:
    if(prevtime - ctime != 0):
        print(1/(prevtime - ctime))
    ctime = time.time()
    suc,img = cam.read()
    
    img = detector.findHands(img)
    
    cv2.imshow("output",img)
    cv2.waitKey(1)
    
    prevtime = time.time()