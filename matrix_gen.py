import json
import matplotlib.pyplot as plt

f1 = open("LAXtoNRT.txt", "r") # LAX to NRT
#f2 = open("JFKtoLHR.txt", "r") # JFK to LHR

data1 = json.loads(f1.read())
#data2 = json.loads(f2.read())

f1.close()
#f2.close()

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
	y = []
	for price in data:
		if not(price[0] < 133 and price[1] > 500):
			x.append(price[0])
			y.append(price[1])
	return [x, y]

data1 = mod_365(data1)
#data2 = mod_365(data2)	
		
avg_val(data1)
#avg_val(data2)
	
def interp(data):
	int_data = []
	for x in range(365):
		int_data.append([x, (440.83952879941756 - 0.9230346529037582*x + 0.012759488691416044*x**2 + 0.0030480935312014686*x**3 - 0.00011838651457851168*x**4 + 0.00000183290116609483*x**5 - 1.490920950571e-8*x**6 + 6.935176753e-11*x**7 - 1.8584496e-13*x**8 + 2.6731e-16*x**9 - 1.6e-19*x**10)])
	return int_data

int_data1 = interp(data1)

print(int_data1)

plt.scatter(*split_val(data1), color="darkorange", label="LAX to NRT")
#plt.plot(range(365), [1] * 365, color="orange", label="Mean")
plt.plot(*split_val(int_data1), color="navy", label="LAX to NRT Regression")
plt.xlabel("Days after Janurary 1 in a Year")
plt.ylabel("Average Flight Cost (USD)")
plt.title("Average Flight Cost from LAX to NRT vs. Days into the Year")
plt.legend()
plt.xlim([0, 363])
plt.ylim([410, 610])
plt.show()

