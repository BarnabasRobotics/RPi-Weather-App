from gpiozero import LED
from time import sleep
import RPi.GPIO as GPIO
#import RPi.GPIO as IO  
from time import sleep
import pyowm
import time 
#from openWeather import openWeather
#create a function to just have servo(90) and have it move the servo to 90
GPIO.setmode (GPIO.BCM)            # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)
GPIO.setup(19,GPIO.OUT)             # initialize GPIO19 as an output
p = GPIO.PWM(19,50)              # GPIO19 as PWM output, with 50Hz frequency
p.start(2.5)                             # generate PWM signal with 7.5% duty cycle
while True:
    
        
        p.ChangeDutyCycle(2.5)           
        time.sleep(0.3)
        p.stop()
        time.sleep(0.5)
        
        p = GPIO.PWM(19,50) 
        p.start(2.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.3)
        p.stop()
        time.sleep(0.5)
        
        p = GPIO.PWM(19,50) 
        p.start(7.5)
        p.ChangeDutyCycle(12.5)                  
        time.sleep(0.3)
        p.stop()
        time.sleep(0.5)
        p = GPIO.PWM(19,50) 
        p.start(12.5)
      
        
       

'''GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)
pwm= GPIO.PWM(03, 50)
pwm.start(0)
defsetAngle(angle):
    duty = angle / 18+2
    GPIO.output(03, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    pwm.ChangeDutyCyle(0)
    SetAngle(90)
    pwm.stop
    GPIO.cleanup()'''


owm = pyowm.OWM('9276659d9dc88d95bfbd5db39938c052')

observation= owm.weather_at_place("North Glendale, US")

w= observation.get_weather()

#wind= w.get_wind()

temperature= w.get_temperature('fahrenheit')
temp_value= temperature.get('temp') 

led= LED(17)

if temp_value >= 60 and temp_value <= 65:
        led.on()
        sleep(1)
        led.off()
        sleep(1)

elif temp_value> 65 and temp_value <= 70:
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

#comment
