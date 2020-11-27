import cv2
from gtts import gTTS
import os
from threading import *
from playsound import playsound
cap=cv2.VideoCapture('testinvideo.mp4')
cap.set(3,800)
cap.set(4,700)
nplate=cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
minarea=300
count=0
def sound():
    playsound('/Users/rohanmahto/PycharmProjects/numberplate/sound.mp3')
while True:
    success,img=cap.read()
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberplates=nplate.detectMultiScale(imgGray,1.1,3)
    for(x,y,w,h) in numberplates:
        area=w*h
        if area>minarea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),2)
            cropimage=img[y:y+h,x:x+w]
            cv2.imshow("numberplate_image",cropimage)
    cv2.imshow('output',img)
    if cv2.waitKey(50)&0xFF==ord('s'):
        cv2.imwrite('/Users/rohanmahto/PycharmProjects/numberplate/scannedIMage/'+str(count)+'.jpg',cropimage)
        cv2.rectangle(img,(0,200),(640,300),(255,0,255),cv2.FILLED)
        count+=1
        xy = Thread(target=sound)
        xy.start()
        xy.join(timeout=7)
        cv2.putText(img, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 2)

        cv2.imshow('output', img)

    if cv2.waitKey(50)&0xFF==ord('a'):
        break




