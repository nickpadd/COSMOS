import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#note equals the user input
#the loop allows the led to light up
#depedning on wut the user's input is..

#Raspberry pi0W pinout
#BCM 14 = note A
#BCM 15 = note B
#BCM 23 = note C
#BCM 18 = note D
#BCM 24= note E
#BCM 25 = note F
#BCM 7 = note G


def make_light (note):
        if (note == "a"):
                GPIO.setup(14,GPIO.OUT)
                GPIO.output(14, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(14,GPIO.LOW)
                
        elif (note == 'b'):
                GPIO.setup(15,GPIO.OUT)
                GPIO.output(15, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(15,GPIO.LOW)
                
        elif (note == 'c'):
                GPIO.setup(23,GPIO.OUT)
                GPIO.output(23, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(23,GPIO.LOW)
                
        elif (note == 'd'):
                GPIO.setup(18,GPIO.OUT)
                GPIO.output(18, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(18,GPIO.LOW)
                
        elif (note == 'e'):
                GPIO.setup(24,GPIO.OUT)
                GPIO.output(24, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(24,GPIO.LOW)
                
        elif (note == 'f'):
                GPIO.setup(25,GPIO.OUT)
                GPIO.output(25, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(25,GPIO.LOW)
                
        elif (note == 'g'):
                GPIO.setup(7,GPIO.OUT)
                GPIO.output(7, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(7,GPIO.LOW)

