import requests

def fromAddress(address):
	my_api_key = 'AIzaSyC9ZPnhBLoe4SZmkghgQKUJrDKtm2Cu-iE'
	api_address = 'https://maps.googleapis.com/maps/api/geocode/json?address='+\
		address.replace(" ","+") + "Western+Cape+South+Africa" + '&key=' + my_api_key
	response = requests.get(api_address)
	resp_json_payload = response.json()
	if resp_json_payload['status'] == 'OK':
		lat = resp_json_payload['results'][0]['geometry']['location']['lat']
		lng = resp_json_payload['results'][0]['geometry']['location']['lng']
		return Coordinate(lat, lng)
	else:
		return None

class Coordinate:
	def __init__(self, latitude=0, longitude=0):
		self.lat = latitude
		sel.long = longitude

	def distance(self, other):
		#Cape Town is flat :P
		return ((self.lat-other.lat)**2 + (self.long-other.long)**2)**0.5
