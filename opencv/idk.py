#get video input from camera
import cv2
import numpy as np
import time
import os


#get video input from camera
cap = cv2.VideoCapture(0)


#set the width and height of the video
cap.set(3,640)
cap.set(4,480)


#set the frame rate
cap.set(5,60)

#get the input
while True:
    #get the frame
    ret, frame = cap.read()
    #convert the frame to gray
    #filter out any color that is not blue
    #convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_blue = 209 / 360 * 179
    upper_blue = 257 / 360 * 179
    min_val = 0.25 * 255 * 0
    min_sat = 0.22 * 255 * 0

    #set all the value and saturation to 0 for hsv
    h,s,v = cv2.split(hsv)

    # v[:] = 10
    # s[:] = 10
    
    
    h[ h < lower_blue] = 0
    h[ h > upper_blue] = 0
    h[h != 0] = 1
    v[v < min_val] = 0
    s[s < min_sat] = 0
    
    
    v[h == 0] = 0
    s[h == 0] = 0

    #create a mask of h
    mask = cv2.merge((h,s,v))


    #apply the mask to the frame
    res = cv2.bitwise_and(frame, frame, mask = mask)

    # result = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)
    
    # result = cv2.bitwise_and(frame, mask, mask=mask)


    
    #show the frame
    cv2.imshow('frame',res)
    #wait for 1ms
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

