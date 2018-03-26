from requests import get
import json
from pprint import pprint
from haversine import haversine
stations= 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather= 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'
my_lat=34.155489
my_lon= -118.091491