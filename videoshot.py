#!/usr/bin/python

import time
import datetime
import picamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)

videorecordingstatus = 0

def cameraledblink():
    with picamera.PiCamera() as camera:
        camera.led = True
        time.sleep(0.5)
        camera.led = False
        time.sleep(0.5)

def videoshot():
    with picamera.PiCamera() as camera:
        videorecordingstatus = 0
        #camera.led = True
        camera.resolution = (1024, 768) # recording resolution
        camera.hflip = True
        camera.vflip = True
        GPIO.wait_for_edge(17, GPIO.FALLING)
        timestamp = time.strftime('%Y%m%d-%H%M%S') # Timestamp
        videorecordingstatus = 1
        camera.start_recording('/home/pi/video/video-' + timestamp + '.h264')
        print (timestamp + "--> " + "Videorecording started")
        time.sleep(0.5)
        #camera.led = True
        GPIO.wait_for_edge(17, GPIO.FALLING)
        timestamp = time.strftime('%Y%m%d-%H%M%S') # Timestamp
        print (timestamp + "--> " + "Videorecording stopped")
        camera.stop_recording()
        #camera.led = False

while (videorecordingstatus > 0):
    cameraledblink()

while True:
    videoshot()
