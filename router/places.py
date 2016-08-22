import coordinate
import requests

def find_nearby_places(address):
	my_api = 'AIzaSyBtqFCeJlUQAE8Y9zY2grfOXmFouGcJZGI'
	coords = coordinate.fromAddress(address)
	lat = coords.lat
	lng = coords.long
	placeType = 'restaurant'
	url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={0},{1}&radius=500&type={2}&key={3}'.format(lat,lng,placeType,my_api)
	response = requests.get(url)
	resp_json_payload = response.json()
	place_coords = []
	
	name_of_shop=[] #for the name of the shop
	numShops = len(resp_json_payload['results'])
	if numShops > 5: numShops = 5
	for i in range(0,numShops):
		latitude = resp_json_payload['results'][i]['geometry']['location']['lat']
		longitude = resp_json_payload['results'][i]['geometry']['location']['lng']
		place_coords.append([latitude,longitude])
		name_of_shop.append(resp_json_payload['results'][i]['name'])
	
	#locations = [] #address of the shops respectively
	#for k in range(0,len(place_coords)):
	#	places = ""
	#	new_url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={0},{1}&key=AIzaSyC9ZPnhBLoe4SZmkghgQKUJrDKtm2Cu-iE'.format(place_coords[k][0],place_coords[k][1])
	#	new_response = requests.get(new_url)
	#	new_resp = new_response.json();
	#	for j in range(0,3):
	#		places = places + " " + new_resp['results'][0]['address_components'][j]['long_name']
	#	locations.append(places)
	return name_of_shop#, locations
			
