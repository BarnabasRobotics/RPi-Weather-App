from gpiozero import LED
from time import sleep
import RPi.GPIO as GPIO 
from time import sleep
import pyowm
import time 
from gpiozero import LED
from time import sleep
import RPi.GPIO as GPIO 
from time import sleep
import pyowm
import time
import sys

def move_servo(num): #function to move servo             
    p = GPIO.PWM(19,50)
    p.start(1.2)
    time.sleep(0.8)
    p.ChangeDutyCycle(num)           
    time.sleep(0.3)
    p.stop()
    time.sleep(40)
        
def weather():
    print(" ------------------------------------")
    print(" Welcome to Barnabas Weather Station ")
    print(" ------------------------------------")
    city=str(input('Please enter a city in the United States:\n'))
    
    owm = pyowm.OWM('9276659d9dc88d95bfbd5db39938c052')

    observation= owm.weather_at_place(city +", US")
 
    w= observation.get_weather()


    temperature= w.get_temperature('fahrenheit')
    temp_value= temperature.get('temp')
    humidity = w.get_humidity()

    led= LED(17)
    if temp_value >= 60 and temp_value <= 65:
        led.on()
        sleep(1)
        led.off()
        sleep(1)
         
    elif temp_value> 65 and temp_value <= 100:
        led.on()
        sleep(1)
        led.off()
        sleep(1)
        led.on()
        sleep(1)
        led.off()
        sleep(1)
        led.on()
        sleep(1)
        led.off()
        sleep(1)

    GPIO.setmode (GPIO.BCM)            # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)
    GPIO.setup(19,GPIO.OUT)            # initialize GPIO19 as an output
    p = GPIO.PWM(19,50)                # GPIO19 as PWM output, with 50Hz frequency
    p.start(1.2)                       # generate PWM signal with 7.5% duty cycle

        
    while True:
            
            if humidity<= 50:
                move_servo(3) #moves dial to low
                
            
            elif humidity <=70 and humidity>50:
                move_servo(5) #moves dial to medium
                
            
            elif humidity <=120 and humidity >70:
                move_servo(7) #moves dial to high

try:
    weather()
except:
    print ("Invalid city")
    weather()
    

owm = pyowm.OWM('9276659d9dc88d95bfbd5db39938c052')

observation= owm.weather_at_place("Pasadena, US")

w= observation.get_weather()


temperature= w.get_temperature('fahrenheit')
temp_value= temperature.get('temp')
humidity = w.get_humidity()

GPIO.setmode (GPIO.BCM)            # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)
GPIO.setup(19,GPIO.OUT)            # initialize GPIO19 as an output
p = GPIO.PWM(19,50)                # GPIO19 as PWM output, with 50Hz frequency
p.start(1.2)                       # generate PWM signal with 7.5% duty cycle

def move_servo(num):               #function to move servo             
    p = GPIO.PWM(19,50)
    p.start(1.2)
    time.sleep(0.8)
    p.ChangeDutyCycle(num)           
    time.sleep(0.3)
    p.stop()
    time.sleep(200)
    #p = GPIO.PWM(19,50) #this part makes it reset to 0 at the end of the program but if you want to 
    #reset when first running the program don't use this 
    #p.start(num)
    #time.sleep(0.3)
    #p.ChangeDutyCycle(1)
    #time.sleep(0.3)
    #p.stop()
    #time.sleep(20)
    
while True:
        
        if humidity<= 50:
            move_servo(3) #moves dial to low
            
        
        elif humidity <=70 and humidity>50:
            move_servo(5) #moves dial to medium
            
        
        elif humidity <=120 and humidity >70:
            move_servo(7) #moves dial to high
            
            