import Database
import coordinate

class Station:
	def __init__(self, ID, name, AlexaID, Longitude, Latitude):
		self._ID = ID
		self._name = name
		self._AlexaID = AlexaID
		self.coordinates = coordinate.Coordinate(Latitude, Longitude)
	
class StationList:
	def __init__(self):
		self.stations = {}
	def loadFromDatabase(self, database):
		for item in database.fetchall(\
			"SELECT * FROM Stations;"):
			self.stations[int(item[0])] = Station(\
				int(item[0]), item[1], item[2], float(item[3]), float(item[4]))
	def getClosestStation(self, coords):
		minDist = None
		minID = None
		for ID in self.stations:
			dist = coords.distance(self.stations[ID].coordinates)
			print ID
			print self.stations[ID]._name
			print dist
			if (minDist == None) or (dist < minDist):
				minDist = dist
				minID = ID
		return self.stations[minID]
	def getFromAlexaID(self, AlexaID):
		for ID in self.stations:
			if self.stations[ID]._AlexaID == AlexaID:
				return self.stations[ID]
		return None
