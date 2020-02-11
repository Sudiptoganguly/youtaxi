from geopy.distance import geodesic


def CalculateDistance():
    kolkata = (22.5726, 88.3639) 
    delhi = (28.7041, 77.1025)
    distance = geodesic(kolkata, delhi).km
    
    return distance