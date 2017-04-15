import math

EARTH_CIRCUM = 40075.

def sphere_dist(v1, v2):
	dot = v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
	dist = math.acos(dot)
	return (dist/math.pi)

def lat_long_to_vector(lat, long):
	x = math.cos(lat) * math.cos(long)
	y = math.sin(lat)
	z = math.cos(lat) * math.sin(long)
	return (x, y, z)
	
def rad(deg):
	return math.pi*(deg/180)

'''
lat1 = 40.7128
long1 = 74.0059
lat2 = 41.8781
long2 = 87.6298

v1 = lat_long_to_vector(rad(lat1), rad(long1))
v2 = lat_long_to_vector(rad(lat2), rad(long2))

print(sphere_dist(v1, v2)) 
'''