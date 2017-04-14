from graphics import *
import time
import numpy as np
import math
import random
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import fsolve
plt.style.use('ggplot')

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
    dif=0
    points = []
    values = randomly()
    magnitude_dif = 5
    while (magnitude_dif>0.3):
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
        print(magnitude_dif)
        t += 0.01
    return points


def graph(list1,list2, list3, list4):
    win = GraphWin('Graph', 1000, 1000)
    win.setBackground('white')
    pty1 = Point(50, 100)
    pty2 = Point(50, 600)
    ylabel1 = Text(Point(40,300), 1)
    ylabel1.draw(win)
    ylabel2 = Text(Point(40,100), 2)
    ylabel2.draw(win)
    xlabel1 = Text(Point(237.5,510), 8)
    xlabel1.draw(win)
    xlabel2 = Text(Point(475,510), 16)
    xlabel2.draw(win)
    xlabel3 = Text(Point(712.5,510), 24)
    xlabel3.draw(win)
    xlabel4 = Text(Point(900,510), 32)
    xlabel4.draw(win)
    yaxis = Line(pty1, pty2)
    ptx1 = Point(50, 500)
    ptx2 = Point(900, 500)
    xaxis= Line(ptx1, ptx2)
    xaxis.draw(win)
    yaxis.draw(win)
    ptq1 = Point(50,440)
    ptq2 = Point(900,440)
    linq = Line(ptq1, ptq2)
    linq.draw(win)
    for y in list1:
        pt = Point(50+(list1.index(y)+1)/3,500-y*200)
        pt.setFill('red')
        pt.draw(win)
    for y in list2:
        pt = Point(50+(list2.index(y)+1)/3,500-y*200)
        pt.setFill('green')
        pt.draw(win)
    for y in list3:
        pt = Point(50+(list3.index(y)+1)/3,500-y*200)
        pt.setFill('blue')
        pt.draw(win)
    for y in list4:
        pt = Point(50+(list4.index(y)+1)/3,500-y*200)
        pt.setFill('purple')
        pt.draw(win)
    pause = win.getMouse()
    win.close()

        
yvals1=start(-math.pi*3/12)
yvals2=start(-math.pi*6/12)
yvals3 = start(-math.pi*9/12)
yvals4 = start(-math.pi*12/12)
graph(yvals1, yvals2, yvals3, yvals4)