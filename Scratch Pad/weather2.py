from requests import get
import json
from pprint import pprint
from haversine import haversine

stations= 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather= 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

my_lat= 34.155351
my_lon= -118.091471

all_stations= get(stations).json()['items']

def find_closest():
    smallest = 20036
    
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        #print(distance)
        
        if distance< smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station

closest_stn = find_closest()
weather= weather +str(closest_stn)
my_weather = get(weather).json()['items']
pprint(my_weather)

#try putting the data into a text file and reading the specific line
#that has only the air_quality
#how to print data from the internet into a text file in python



        
    