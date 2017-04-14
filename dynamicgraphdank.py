from graphics import *
import time
import numpy as np
import math
import random
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import fsolve

delta = 20
omega = 1.4 * delta
k = 4.5 * delta
f = 3.5 * delta
sigma = (2 * math.pi )/24
dt = 0.01
zst_real = 0.798349
zst_imag = -0.344415

def weight_summat(thetas, theta):
    total = 0
    for angle in thetas:
        total += math.sin(angle - theta)
    return total

def second_part(theta, distance, t):
    ans = f * math.sin(sigma * t + distance)
    return ans

def change(previous_theta, time, thetas, distance):
    total = omega + weight_summat(thetas, previous_theta) + second_part(previous_theta, distance, time)
    new_theta = previous_theta + (dt * total) 
    return new_theta

def randomly():
    export = []
    for i in range(1, 100):
        export.append(math.pi+np.random.standard_cauchy())
    return export


def start(angle):
	if (angle>0):
		angle = math.pi - angle
	else:
		angle = -(math.pi + angle)
	t = 0
	dif = 0
	t_tb = []
	points = []
	values = randomly()
	magnitude_dif = 5
	while (magnitude_dif>0.25):
		holder = []
		for item in values:
			new = change(item, t, values, angle)
			holder.append(new)
		average_sum_x = 0
		average_sum_y = 0
		for element in holder:
			exponent = element - (t * sigma) - angle
			ang_to_calculate = exponent / math.pi 
			average_sum_x += math.cos(ang_to_calculate)
			average_sum_y += math.sin(ang_to_calculate)
		average_x = average_sum_x / 100
		average_y = average_sum_y / 100
		z_dif_x = zst_real - average_x
		z_dif_y = zst_imag - average_y
		magnitude_dif = math.sqrt((z_dif_x)**2 + (z_dif_y)**2)
		points.append(magnitude_dif)
		t_tb.append(t)
		print(magnitude_dif)
		t += 0.01
	return t_tb, points
        
t1, list1=start(math.pi*3/12)
t2, list2=start(math.pi*6/12)
t3, list3 = start(math.pi*9/12)
t4, list4=start(math.pi*-3/12)
t5, list5=start(math.pi*-6/12)
t6, list6 = start(math.pi*-9/12)
t7, list7 = start(math.pi*12/12)
plt.plot(t1, list1, color="red", label="+3hrs")
plt.plot(t2, list2, color="orange", label="+6hrs")
plt.plot(t3, list3, color="yellow", label="+9hrs")
plt.plot(t4, list4, color="green", label="-3hrs")
plt.plot(t5, list5, color="blue", label="-6hrs")
plt.plot(t6, list6, color="indigo", label="-9hrs")
plt.plot(t7, list7, color="purple", label="+-12hrs")
plt.title("Jet Lag")
plt.xlabel("t (minutes)")
plt.ylabel("R(t) - R_st (magnitude)")
plt.xlim(xmin=0)
plt.ylim(ymin=.25)
plt.legend()
plt.show()