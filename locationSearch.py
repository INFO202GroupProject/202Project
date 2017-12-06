import math
import pandas as pd 
import numpy as np 
import geocoder

df = pd.read_csv('beer_database_final.csv', encoding='ISO-8859-1')

beer_names = list(df.Beer_Name)
lats = list(df.latitude)
longs = list(df.longitude)

ptList = zip(beer_names, lats, longs)

points_list = [entry for entry in ptList if entry[1] != 'nan' and entry[0] != 'nan']

#This Function is from Stackerflow:
#https://stackoverflow.com/questions/40452759/pandas-latitude-longitude-to-distance-between-successive-rows
def haversine_np(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)

    All args must be of equal length.    

    """
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2

    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    miles = km * 0.621371
    return miles

#Naive (euclidean distance between points)
def dist(p1, p2):
	return math.sqrt( math.pow(p1.x - p2.x) + math.pow(p1.y - p2.y) )

def filterByDist(pList, point, radius):
	""" Given a list of beers/locations, a point, and a radius, return the beers within that radius of the point """
	closeBy = []

	for guess in pList:
		#print( guess)
		distance = haversine_np(point[0], point[1], guess[1], guess[2])
		#print(distance)
		if (distance < radius):
			#print(guess)
			closeBy.append([guess, distance])

	return closeBy

#Get User inputted address/city/zipcode 
def BreweriesNearby(loc, radius):
	"""Given a string containing address/city/zipcode the function returns beers within the given radius"""
	g = geocoder.google(loc);
	coords = g.latlng

	results = filterByDist(points_list, coords , radius)


	results.sort(key = lambda x: x[1], reverse=False )

	#print()
	if len(results) > 0:

		print("Beers brewed nearby to " + loc + ": \n")
		
		for res in results[:10]:
			#dist = math.trunc(haversine_np(coords[0], coords[1], res[1], res[2]));
			m = str(res[1])
			ind = m.index('.')
			mres = m[0:ind]
			print(res[0][0] + " (" + mres + " miles)" )
	else:
		print("No beers found brewed near this location!")


def searchBreweriesNearby():
	searchMore = True
	print("Want to search for beers brewed near you?") 
	while searchMore:
		prompt = "Enter an address: "
		loc = str(input(prompt))
		BreweriesNearby(loc, 50)

		nextprompt = "Want to search for more? [y/n]"
		response = str(input(nextprompt))
		if response == "y":
			searchMore = True
		else:
			searchMore = False
		
#searchBreweriesNearby()