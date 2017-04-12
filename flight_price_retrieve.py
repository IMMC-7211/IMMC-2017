import numpy
import requests
import json
import math

YEAR = 2017

DPM = [
	31,
	28,
	31,
	30,
	31,
	30,
	31,
	31,
	30,
	31,
	30,
	31
]

def num_to_day(num):
	month = 1
	day = (num + 1) % 365
	year = 2017 + math.floor((num+1) / 365)
	while (day > DPM[month-1]):
		day -= DPM[month-1]
		month += 1
	month = str(month)
	day = str(day)
	year = str(year)
	if len(month) == 1:
		month = "0" + month
	if len(day) == 1:
		day = "0" + day
	return year, month, day

API_KEY = "su293493194092138670806993660989"
		
def get_flight_prices(num):
	year, month, day = num_to_day(num)
	link = "http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/US/USD/en-US/JFK/LHR/"+year+"-"+month+"-"+day+"?apiKey=" + API_KEY
	r = requests.get(link)
	data = json.loads(r.text)
	prices = []
	for quote in data["Quotes"]:
		prices.append([num, quote["MinPrice"]])
	return prices
	
price_list = []

for i in range(102, 467):
	print(i)
	try:
		price_list += get_flight_prices(i)
	except:
		print("error")

file = open("JFKtoLHR.txt", "w")
file.write(json.dumps(price_list))
file.close()
	