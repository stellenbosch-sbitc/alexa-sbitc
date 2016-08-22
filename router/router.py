import web
import json
import Database
import coordinate
import Stations
import places
import Graph

urls = (
	'/alexa', 'index'
)

def build_response(text, endSession = True):
    response = """
		{ "response": {
			"outputSpeech": {
            "type": "PlainText",
            "text": " """ + text + """ "
        },
        "shouldEndSession": """
    
    if (endSession): response += "true"
    else: response += "false"
    
    return response + """
    }}"""

def build_instructions(route, stations):
    i = 0
    end = route[-1].EndID
    instruction = ""
    while (i < len(route)):
        startBus = route[i].Bus
        startStation = route[i].StartID
        while ((i < len(route)) and (route[i].Bus == startBus)):
            i += 1
        if (i < len(route)):
            instruction += "Take bus " + str(startBus) + " from "
            instruction += stations.getFromStationID(startStation)._name
            instruction += " to "
            startBus = route[i].Bus
            startStation = route[i].StartID
            instruction += stations.getFromStationID(startStation)._name + ". "
        else:
            instruction += "Take bus " + str(startBus) + " from "
            instruction += stations.getFromStationID(startStation)._name
            instruction += " to "
            instruction += stations.getFromStationID(end)._name + "."
    return instruction




class index:
    def POST(self):
        stations = Stations.StationList()
        db = Database.Database("localhost", "root", "P@ssw0rd1234", "ROUTER")
        stations.loadFromDatabase(db)
        
        data = json.loads(web.data())
        requestType = data["request"]["type"]
        if (requestType == "IntentRequest"):
            userID = data["session"]["user"]["userId"]
            station = stations.getFromAlexaID(userID)
            if station == None: return build_response("I do not know where you are")
            intent = data["request"]["intent"]["name"]
            if (intent == "Location"):
                return build_response("You are at " + station._name + " station.")
            elif (intent == "Directions"):
                address = \
                    data["request"]["intent"]["slots"]["Address"]["value"]
                coords = coordinate.fromAddress(address)
                closest = stations.getClosestStation(coords)
                if (closest == None):
                    return build_response("I am not sure where that is")
                Map = Graph.Graph();
                Map.loadFromDatabase(db)
                route = Map.Dijkstra(station._ID, closest._ID)
                instructions = build_instructions(route, stations)
                print instructions
                #return build_response("Go to " + closest._name + " station")
                return build_response(instructions)
            elif (intent == "Interest"):
                address = \
                    data["request"]["intent"]["slots"]["Address"]["value"]
                print address
                shopNames =  places.find_nearby_places(address)
                if len(shopNames) == 0:
                    return build_response("I could not find anything for you")
                print shopNames[0]
                return build_response("Why not try " + shopNames[0] + "?")
                #print shopLocations[0]
        return  build_response("")
	
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


