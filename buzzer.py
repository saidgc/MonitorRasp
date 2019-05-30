# Libraries
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer = 23
GPIO.setup(buzzer, GPIO.OUT)


def times(n):
    for i in range(n):
        GPIO.output(buzzer, GPIO.HIGH)
        print("Beep")
        sleep(0.5)
        GPIO.output(buzzer, GPIO.LOW)
        print("No Beep")
        sleep(0.5)
