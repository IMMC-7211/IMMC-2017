import requests
with open('Cities.txt') as f:
    content = f.read().splitlines()
content.remove('\ufeffTokyo')
content.append('Tokyo')
for site in content[:]:
    content.remove(site)
    content.append(site.replace(" ", "+"))
for site in content[:]:
    if site == '':
        content.remove(site)
test = ['Chicago', 'New+York', 'Atlanta']
coordinates = {}
for city in content:
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + city + '&key=AIzaSyDrMWc153_fGhQhmmsYLOzJUKNAp3kFBJ8')
    
    info_all = r.json()
    results = info_all['results']
    list_item = results[0]
    geometry = list_item['geometry']
    location = geometry['location']
    lat = location['lat']
    lng = location['lng']

    print(city +  ': ')
    print(lat)
    print(lng)
