import requests
def timezone(lat, lng):
    r = requests.get("http://api.geonames.org/timezoneJSON?lat=" + str(lat) + "&lng=" + str(lng) + "&username=nkim")
    data = r.json()
    return data['dstOffset']
print(timezone(36.86857, 56.3849238))
