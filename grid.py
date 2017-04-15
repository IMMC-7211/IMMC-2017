import requests
import urllib.request as urllib
import math
import io
import PIL, PIL.Image
from fitness import *
from sphere_dist import *

DELTA_ANG = 5
EARTH_CIRCUM = 40075.

def is_water(coord):
	url = "https://maps.googleapis.com/maps/api/staticmap?center=" + str(coord[0]) + "," + str(coord[1]) + "&zoom=13&size=600x300&maptype=roadmap&key=AIzaSyCVaHpRqBL8CkewfGgKh5n-LaS5T2D_zcE"
	fd = urllib.urlopen(url)
	image_file = io.BytesIO(fd.read())
	img = PIL.Image.open(image_file)
	img = img.convert("RGB")
	total_pix = 600 * 300
	colors = img.getcolors(total_pix)
	for color in colors:
		if color[1][0] == 163 and color[1][1] == 204 and color[1][2] > 250 and color[0] >= total_pix * .9:
			return True
	return False

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

def create_grid(coords):
	min_lat, min_long, max_lat, max_long = bounds(coords)
	grid = []
	print(str(math.ceil((max_lat-min_lat)/DELTA_ANG)*math.ceil((max_long-min_long)/DELTA_ANG)), "total grid points")
	for lat in range(math.ceil((max_lat-min_lat)/DELTA_ANG)):
		for long in range(math.ceil((max_long-min_long)/DELTA_ANG)):
			coord = [min_lat + lat*DELTA_ANG, min_long + long*DELTA_ANG]
			w = is_water(coord)
			print("Coordinate", coord, "is water:", w)
			if not w:
				grid.append(coord)
	return grid
	
def distance(coord1, coord2):
	return sphere_dist(lat_long_to_vector(rad(coord1[0]), rad(coord1[1])), lat_long_to_vector(rad(coord2[0]), rad(coord2[1])))
	
def cost(coord1, coord2, x):
	c = 440.83952879941756 - 0.9230346529037582*x + 0.012759488691416044*x**2 + 0.0030480935312014686*x**3 - 0.00011838651457851168*x**4 + 0.00000183290116609483*x**5 - 1.490920950571e-8*x**6 + 6.935176753e-11*x**7 - 1.8584496e-13*x**8 + 2.6731e-16*x**9 - 1.6e-19*x**10
	ratio = c / 457.924811603
	dist = distance(coord1, coord2) * EARTH_CIRCUM / 2
	return ratio*(dist*.177 + 50)

scenario1 = ["Monterey", "Zutphen", "Melbourne", "Shanghai", "Hong Kong", "Moscow"]
scenario2 = ["Boston", "Boston", "Singapore", "Beijing", "Hong Kong", "Hong Kong", "Moscow", "Utrecht", "Warsaw", "Copenhagen", "Melbourne"]

people = scenario2

t = 16
coords = []
for city in people:
	coords.append(get_city_coords(add_plus(city)))

grid = create_grid(coords)

fit = []

for coord1 in grid:
	min_cost = 10000000
	max_cost = 0
	fitnesses = []
	for coord2 in coords:
		c = cost(coord1, coord2, t)
		min_cost = min(min_cost, c)
		max_cost = max(max_cost, c)
		x = rad(coord1[1]) - rad(coord2[1])
		if abs(x) > math.pi:
			x = (2*math.pi - abs(x)) * -x/abs(x)
		jl = -0.0014*x**6 - 0.0002*x**5 + 0.0264*x**4 + 0.0022*x**3 - 0.2153*x**2 - 0.0074*x + 0.8368
		d = 1 - distance(coord1, coord2)
		print(c, x, jl, d)
		fitnesses.append([coord2, jl, d, c])
	final_fitness = 0
	for f in fitnesses:
		c = 1 - (f[3] - min_cost) / (max_cost - min_cost)
		final_fitness += .6 * f[1] + .2 * f[2] + .2 * c
	fit.append([coord1, final_fitness / len(fitnesses)])

sorted_fit = sorted(fit, key=lambda f: f[1], reverse=True)

print(sorted_fit)
	
	
		





