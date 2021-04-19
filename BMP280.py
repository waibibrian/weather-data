"""
@author Brian Waibi with Elvis
Created on Sunday 19 04 2021
"""

import RPi.GPIO as GPIO # For control of GPIO Pins
import board #Mode of board in use
import busio #support a variety of serial protocols ie uart, spi, i2c etc
import adafruit_bmp280
from time import sleep
import serial #For communication with XBee
GPIO.setmode(GPIO.BCM)

"""
Pin Assignment
servo 1 => pin 11
servo 2 => pin 12

#bmp280 connections
Pi 3.3V to sensor VIN
Pi GND to sensor GND
Pi SCL to sensor SCK
Pi pin SDA to sensor SDI

"""

GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)
sensor.sea_level_pressure = 1010 #pressure at sea level for UGANDA

pwm_1 = GPIO.PWM(13, 50) #controlling Servo motors
pwm_2 = GPIO.PWM(19, 50) #create PWM instance with frequency

#start with all servos at 0 degrees
pwm_1.start(0)
pwm_2.start(0)

while true:
    #get data from bmp280 pressure sensor
    temperature = sensor.temperature # in degrees celsius
    pressure = sensor.pressure # in Pa
    altitude = sensor.altitude

    if altitude >= 21000:
        # move motors to 90
        GPIO.output(13, True)
        GPIO.output(19, True)

        pwm_1.ChangeDutyCycle(7) #set pwm to a duty of 7 so as to move the servo to 90 degrees
        pwm_2.ChangeDutyCycle(7)
        sleep(1)

        GPIO.output(13, False)
        GPIO.output(19, False)


        sleep(2)
    


    


    
