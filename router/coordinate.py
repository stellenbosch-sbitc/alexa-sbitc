import requests

def get(address):
	my_api_key = 'AIzaSyC9ZPnhBLoe4SZmkghgQKUJrDKtm2Cu-iE'
	api_address = 'https://maps.googleapis.com/maps/api/geocode/json?address='+ address.replace(" ","+") + "+South+Africa" + '&key=' + my_api_key
	response = requests.get(api_address)
	resp_json_payload = response.json()
	if resp_json_payload['status'] == 'OK':
		lat = resp_json_payload['results'][0]['geometry']['location']['lat']
		lng = resp_json_payload['results'][0]['geometry']['location']['lng']
		return lat,lng
	else:
		print "Can not find location"
