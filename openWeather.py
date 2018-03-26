import pyowm

owm = pyowm.OWM('9276659d9dc88d95bfbd5db39938c052')

observation= owm.weather_at_place("North Glendale, US")

w= observation.get_weather()

#wind= w.get_wind()

temperature= w.get_temperature('fahrenheit')
#print (temperature.split(','))
for line in temperature:
    Type= line.split(",")
    x= Type[1]
    y= Type[2]
    print(x,y)
#tomorrow= pyowm.timeutils.tomorrow()
#search the error name, stack overflow has possible solution


#print(w)
#print(wind)
#print(temperature)
#print(tomorrow)

