import requests
import math

DELTA_ANG = 5

def get_city_coords(city):
	r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + city + '&key=AIzaSyDrMWc153_fGhQhmmsYLOzJUKNAp3kFBJ8')
	info = r.json()
	coords = info["results"][0]["geometry"]["location"]
	return [coords["lat"], coords["lng"]]
	
def add_plus(s):
	return s.replace(" ", "+")

def bounds(coords):
	lat_order = sorted(coords, key=lambda coord: coord[0])
	long_order = sorted(coords, key=lambda coord: coord[1])
	min_lat = lat_order[0][0]
	min_long = long_order[0][1]
	max_lat = lat_order[len(lat_order)-1][0]
	max_long = long_order[len(long_order)-1][1]
	return min_lat, min_long, max_lat, max_long

def create_grid(cities):
	coords = []
	for city in cities:
		coords.append(get_city_coords(add_plus(city)))
	min_lat, min_long, max_lat, max_long = bounds(coords)
	grid = []
	for lat in range(math.ceil((max_lat-min_lat)/DELTA_ANG)):
		for long in range(math.ceil((max_long-min_long)/DELTA_ANG)):
			grid.append([min_lat + lat*DELTA_ANG, min_long + long*DELTA_ANG])
	return grid
	
print(create_grid(["Los Angeles", "New York City"]))