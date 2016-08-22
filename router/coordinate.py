import requests
import math

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
		self.long = longitude

	def distance(self, other):
		#www.movable-type.co.uk/scripts/latlong.html
		R = 6371*10**3
		p1 = self.lat*math.pi/180
		p2 = other.lat*math.pi/180
		d1 = (other.lat-self.lat)*math.pi/180
		d2 = (other.long-self.long)*math.pi/180
		a =	math.sin(d1/2)*math.sin(d1/2)+math.cos(p1)*math.cos(p2)*math.sin(d2)*math.sin(d2)
		c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
		d =	R*c
		return	d

	def toString(self):
		return "(" + str(self.long) + ", " + str(self.lat) + ")"
