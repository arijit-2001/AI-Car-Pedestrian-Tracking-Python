# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 00:06:12 2021

@author: Shayantani Kar
"""

from cv2 import cv2

img_file = 'Car_Photo.jpg'

video = cv2.VideoCapture('video3.mp4')

car_tracker_file = 'cars.xml'
pedestrian_tracker_file = 'haarcascade_fullbody.xml'

car_tracker = cv2.CascadeClassifier(car_tracker_file)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)

while True:
    (read_succesful, frame) = video.read()
    
    if read_succesful:
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    cars = car_tracker.detectMultiScale(grayscaled_frame)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)
    
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)


    cv2.imshow('Car_Detector', frame)

    key2 = cv2.waitKey(1) & 0xFF
    if key2 == ord('q'):
        break

video.release()  
cv2.destroyAllWindows()
