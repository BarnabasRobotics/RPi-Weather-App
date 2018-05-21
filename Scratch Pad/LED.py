from gpiozero import LED
from time import sleep
import RPi.GPIO as GPIO
#import RPi.GPIO as IO  
from time import sleep
import pyowm
import time 
#from openWeather import openWeather
#create a function to just have servo(90) and have it move the servo to 90

owm = pyowm.OWM('9276659d9dc88d95bfbd5db39938c052')

observation= owm.weather_at_place("North Glendale, US")

w= observation.get_weather()

#wind= w.get_wind()

temperature= w.get_temperature('fahrenheit')
temp_value= temperature.get('temp')
humidity = w.get_humidity()

GPIO.setmode (GPIO.BCM)            # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)
GPIO.setup(19,GPIO.OUT)             # initialize GPIO19 as an output
p = GPIO.PWM(19,50)              # GPIO19 as PWM output, with 50Hz frequency
p.start(2.5)                             # generate PWM signal with 7.5% duty cycle

def move_servo(num):             #function to move servo             
    p = GPIO.PWM(19,50)
    p.start(2.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(num)           
    time.sleep(0.3)
    p.stop()
    time.sleep(0.3)
    p = GPIO.PWM(19,50) 
    p.start(num)
    time.sleep(0.3)
    p.ChangeDutyCycle(2.5)
    p.stop()
    time.sleep(20)
    
     
    
    
while True:
        
        if humidity<= 50:
            move_servo(3)
            
        
        elif humidity <=70 and humidity>50:
            move_servo(7.5)
            
        
        elif humidity <=120 and humidity >70:
            move_servo(11)
            
            
