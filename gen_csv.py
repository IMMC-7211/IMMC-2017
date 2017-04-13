import json

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

def gen_csv_str(data):
	s = ""
	for price in data:
		s += str(price[0]) + "," + str(price[1]) + "\n"
	return s

data1 = mod_365(data1)
data2 = mod_365(data2)

avg_val(data1)
avg_val(data2)
		
csv1 = open("LAXtoNRT.csv", "w")
csv2 = open("JFKtoLHR.csv", "w")

csv1.write(gen_csv_str(data1))
csv2.write(gen_csv_str(data2))

csv1.close()
csv2.close()
