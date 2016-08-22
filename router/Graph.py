import Database
import Stations
import Queue

class Time:
	def __init__(self, s="00:00"):
		index = s.index(":")
		self.hours = int(s[:index])
		self.minutes = int(s[index+1:])
	def before(self, other):
		if self.hours < other.hours: return True
		if self.hours == other.hours:
			self.minutes < other.minutes
		return False
	def add(self, other):
		ans = Time()
		ans.hours = self.hours + other.hours
		ans.minutes = self.minutes + other.minutes
		ans.hours += ans.minutes // 60
		ans.minutes %= 60
	def dif(self, other):
		if self.before(other):
			return self.add(Time("24:00")).dif(other)
		else:
			ans = Time()
			ans.hours = self.hours
			ans.minutes = self.minutes
			if self.minutes < other.minutes:
				ans.hours -= 1
				ans.minutes += 60
			ans.hours -= other.hours
			ans.minutes -= other.minutes
			return ans
	def toInt(self):
		return 60 * self.hours + self.minutes

class Edge:
	def __init__(self, RouteID, BusNum, StartStation, EndStation, DepartTime, \
		EndTime):
		self.ID = RouteID
		self.Bus = BusNum
		self.StartID = StartStation
		self.EndID = EndStation
		self.StartTime = Time(DepartTime)
		self.EndTime = Time(EndTime)

class Graph:
	def __init__(self, stations=None):
		self.Stations = stations
		self.Edges = {}
	def loadFromDatabase(self, database):
		self.Stations = Stations.StationList()
		self.Stations.loadFromDatabase(database)
		for item in database.fetchall("SELECT * FROM Routes;"):
			link = Edge(int(item[0]), int(item[1]), int(item[2]), \
				int(item[3]), item[4], item[5])
			if (link.StartID in self.Edges):
				self.Edges[link.StartID] += [link]
			else:
				self.Edges[link.StartID] = [link]
	def Dijkstra(self, start, end):
		distances = {}
		distances[start] = 0;
		toVisit = Queue.PriorityQueue()
		toVisit.put((0, start))
		linkUsed = {}
		linkUsed[start] = None
		while not toVisit.empty():
			node = toVisit.get()
			soFar = node[0]
			From = node[1]
			for link in self.Edges[From]:
				cost = soFar + link.EndTime.dif(link.StartTime).toInt()
				if link.EndID in distances:
					if cost < distances[link.EndID]:
						distances[link.EndID] = cost
						toVisit.put((cost, link.EndID))
						linkUsed[link.EndID] = link
				else:
					distances[link.EndID] = cost
					toVisit.put((cost, link.EndID))
					linkUsed[link.EndID] = link
		Connections = []
		curr = linkUsed[end] #Assuming that there is a path
		while curr != None:
			Connections += [curr]
			curr = linkUsed[curr.StartID]
		return Connections[::-1]

		
