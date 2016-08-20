import web
import json

urls = (
    '/alexa', 'index'
)

preferences = {"Dylan" : "None please",
	"Lisa" : "Two please", 
	"Sarah" : "One please",
	"Trandon" : "I don't drink coffee"}

def build_response(text):
	return """
	{"response": {
         "outputSpeech": {
         "type": "PlainText",
         "text": " """ + text + """ "
         },
         "shouldEndSession": true
       }
} 
"""

class index:
    def POST(self):
		data = json.loads(web.data())
		print data["request"]["type"] == "IntentRequest"
		if data["request"]["type"] == "IntentRequest":
			intent = data["request"]["intent"]["name"]
			print intent
			if intent == "Speak":
				return build_response("Hello")
			elif intent == "Sugar":
				name = data["request"]["intent"]["slots"]["name"]["value"]
				if name in preferences:
					return build_response(preferences[name])
				else:
					return build_response("I do not know who that is.")
			elif intent == "Beauty":
				return build_response("Beauty comes from within")
		return build_response("")
	

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()


