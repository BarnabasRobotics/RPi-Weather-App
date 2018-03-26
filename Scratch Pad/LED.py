from gpiozero import LED
from time import sleep
import RPi.GPIO as GPIO
from time import sleep
import pyowm
#from openWeather import openWeather

GPIO.setmode(GPIO.BOARD)
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
    GPIO.cleanup()


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
