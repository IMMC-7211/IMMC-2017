import math
import random
import matplotlib.pyplot as plt

PI = math.pi				# Pi
D = 3.8e-3					# Delta
O = 1.4 * D					# Omega
K = 4.5 * D		 			# K
F = 3.5 * D					# F
N = 100					# Number of Neurons
S = (2 * PI)/24				# Sigma (Frequency of Circadian Rhythm)
DT = 0.075					# Change in t to use for Euler's integration
Z_ST_REAL = 0.798349		# Real Constant of z_st
Z_ST_IMAG = -0.344415		# Imaginary Coefficient of z_st
E = 0.5 					# Epsilon (distance from z_st at which stability is achieved)
R = 0.2						# Absolute distance from PI/12 that we choose natural frequencies from

def g(x):
	return D/(PI*((x-PI/12)**2+D**2))
	
def rand_list(list):
	return list[0] + random.random()*(list[1]-list[0])
	
def choose_dist(dist_func, domain, range):
	x, y = 100, 100
	while (y > dist_func(x)):
		x = rand_list(domain)
		y = rand_list(range)
	return x

def gen_neuron_freq():
	return choose_dist(g, [PI/12 - R, PI/12 + R], [0, g(PI/12)])
	
def gen_neurons():
	neurons = []
	for i in range(N):
		neurons.append(gen_neuron_freq())
	return neurons
	
def sum_neuron(neuron, neurons):
	s = 0
	for neuron0 in neurons:
		s += math.sin(neuron0-neuron)
	return s * K/N
	
def deriv(thetas, omegas, index, t, ang):
	return omegas[index] + sum_neuron(thetas[index], thetas) + F*math.sin(S*t - thetas[index] + ang)

def integrate(long_change):
	ang_real = math.cos(long_change)
	ang_imag = math.sin(long_change)
	new_real = ang_real * Z_ST_REAL - ang_imag * Z_ST_IMAG
	new_imag = ang_imag * Z_ST_REAL + ang_real * Z_ST_IMAG
	new_ang = math.atan(new_imag/new_real)
	thetas = [new_ang] * N
	omegas = [PI/12] * N
	dist = 100
	dist_list = []
	t = 0
	t_list = []
	while (dist > E):
		new_thetas = []
		for i in range(len(thetas)):
			new_thetas.append(thetas[i]+deriv(thetas, omegas, i, t, long_change)*DT)
		sum_real = 0
		sum_imag = 0
		thetas = new_thetas
		for theta in thetas:
			sum_real += math.cos(theta-S*t-long_change)
			sum_imag += math.sin(theta-S*t-long_change)
		avg_real = sum_real / len(thetas)
		avg_imag = sum_imag / len(thetas)
		dist = math.sqrt((avg_real-Z_ST_REAL)**2 + (avg_imag-Z_ST_IMAG)**2)
		t_list.append(t)
		dist_list.append(dist)
		print(dist)
		t += DT
	return t_list, dist_list
	
t1, list1 = integrate(math.pi*3/12)
t2, list2 = integrate(math.pi*6/12)
t3, list3 = integrate(math.pi*9/12)
t4, list4 = integrate(math.pi*-3/12)
t5, list5 = integrate(math.pi*-6/12)
t6, list6 = integrate(math.pi*-9/12)
plt.plot(t1, list1, color="red", label="+3hrs")
plt.plot(t2, list2, color="orange", label="+6hrs")
plt.plot(t3, list3, color="yellow", label="+9hrs")
plt.plot(t4, list4, color="green", label="-3hrs")
plt.plot(t5, list5, color="blue", label="-6hrs")
plt.plot(t6, list6, color="indigo", label="-9hrs")
plt.title("Jet Lag")
plt.xlabel("Relative Time")
plt.ylabel("R(t) - R_st (magnitude)")
plt.xlim(xmin=0)
plt.ylim(ymin=.3)
plt.legend()
plt.show()
	
