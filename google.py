import requests
with open('Cities.txt') as f:
    content = f.read().splitlines()
content.remove('\ufeffTokyo')
content.append('Tokyo')
count = 0
for site in content[:]:
    content.remove(site)
    content.append(site.replace(" ", "+"))
for site in content[:]:
    if site == '':
        content.remove(site)
    count += 1
test = ['Chicago', 'New+York', 'Atlanta']
coordinates = {}
for city in content:
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + city + '&key=AIzaSyDrMWc153_fGhQhmmsYLOzJUKNAp3kFBJ8')
    
    fag = r.json()
    fag2 = fag['results']
    fag3 = fag2[0]
    fag4 = fag3['geometry']
    fag5 = fag4['location']
    print(city +  ': ')
    print(fag5)
