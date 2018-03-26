from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2): #longitude and latitude of the two points whose distance we need to find
    lon1 = radians(lon1)
    lat1 = radians(lat1)
    lon2 = radians(lon2)
    lat2 = radians(lat2)
    dlon = lon2 - lon1 #finding the difference between the long and lat
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1)* cos(lat2) * sin(dlon/2)**2
    distance= 2 * asin(sqrt(a)) * 6371 #radius of the Earth
    return distance
    
