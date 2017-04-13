import numpy as np
import math
import random
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import fsolve
plt.style.use('ggplot')

delta = 0.0038
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
    for i in range(1, 101):
        export.append(2 * math.pi * random.random())
    return export

def start(angle):
    t = 0
    values = randomly()
    while True:
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
        print(magnitude_dif)
        t += 0.01

start(0.5)
