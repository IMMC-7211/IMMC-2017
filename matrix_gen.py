import numpy as np
import json
from sklearn import kernel_ridge
from sklearn import svm
from sklearn import utils
from sklearn import metrics
import matplotlib.pyplot as plt

f1 = open("LAXtoNRT.txt", "r") # LAX to NRT
f2 = open("JFKtoLHR.txt", "r") # JFK to LHR

data1 = json.loads(f1.read())
data2 = json.loads(f2.read())

f1.close()
f2.close()

def mod_365(data):
	for price in data:
		price[0] = price[0] % 365
	return sorted(data, key=lambda price: price[0])

def avg_val(data):
	last = None
	i = 0
	while (i < len(data)):
		price = data[i]
		if last != None:
			if price[0] == last[0]:
				last.append(price[1])
				del data[i]
			else:
				last = price
				i+=1
		else:
			last = price
			i+=1
	for price in data:
		if len(price) > 2:
			price[1] = sum(price[1:])/(len(price)-1)
			for i in range(len(price)-1, 1, -1):
				del price[i]
				
def split_val(data):
	x = []
	x2 = []
	y = []
	for price in data:
		x.append([price[0]])
		x2.append(price[0])
		y.append(price[1])
	return x, y

data1 = mod_365(data1)
data2 = mod_365(data2)	
		
avg_val(data1)
avg_val(data2)

x1, y1 = split_val(data1)
x2, y2 = split_val(data2)

x1arr, y1arr = np.array(x1), np.array(y1)
x2arr, y2arr = np.array(x2), np.array(y2)

cut1 = int(x1arr.size * .75)
cut2 = int(x2arr.size * .75)

"""
x1train, y1train = x1arr[:cut1], y1arr[:cut1]
x2train, y2train = x2arr[:cut2], y2arr[:cut2]

x1test, y1test = x1arr[cut1:], y1arr[cut1:]
x2test, y2test = x2arr[cut2:], y2arr[cut2:]
"""

#svr1 = kernel_ridge.KernelRidge(kernel="rbf")
svr1 = svm.SVR(kernel="rbf")
alg = svr1.fit(x1arr, y1arr).predict(x1arr)
print(metrics.mean_squared_error(y1arr, alg))

plt.scatter(x1arr, y1arr, color="darkorange", label="data")
plt.plot(x1arr, alg, color="navy", label="RBF Model")
plt.xlabel("days after Jan 1")
plt.ylabel("avg price")
plt.title("seasonal flight prices from LAX to NRT")
plt.legend()
plt.show()


