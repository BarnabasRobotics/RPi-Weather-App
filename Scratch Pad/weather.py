from requests import get #fetch web pages from the web
import json #read data 
from pprint import pprint #presents text clearer

url= 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
stations= get(url).json()['items']
