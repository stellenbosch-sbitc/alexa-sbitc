import web
import json
import Database
import coordinate
import Stations

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

class index:
    def POST(self):
        stations = Stations.StationList()
        db = Database.Database("localhost", "root", "P@ssw0rd1234", "ROUTER")
        stations.loadFromDatabase(db)
        
        data = json.loads(web.data())
        requestType = data["request"]["type"]
        if (requestType == "IntentRequest"):
            intent = data["request"]["intent"]["name"]
            if (intent == "Location"):
                userID = data["session"]["user"]["userId"]
                station = stations.getFromAlexaID(userID)
                if station == None: return build_response("I do not know where you are")
                return build_response("You are at " + station._name + " station.")
            elif (intent == "Directions"):
                address = \
                    data["request"]["intent"]["slots"]["Address"]["value"]
                print address
                coords = coordinate.fromAddress(address)
                print str(coordinate.fromAddress(address).toString())
                print stations.getClosestStation(coords)._name
        return  build_response("")
	
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


