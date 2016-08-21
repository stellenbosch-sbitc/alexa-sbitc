import web
import json

urls = (
    '/alexa', 'index'
)

# Hardcoded responses in the format
# "IntentName" : "Desired Response"
responses = {
	"Address" :	"The closest bus stop to thirty long street is Upper loop", 
	"Route" :	"You should take bus number thirty four which arrives in fifteen minutes",
	"Cost" :	"It will cost twelve rand",
	"Time" :	"The bus will arrive in fifteen minutes",
	"Payment":	"You can purchase a ticket at the nearest Pick and Pay"
}

def build_response(text):
	return """
	{ "response": {
		"outputSpeech": {
			"type": "PlainText",
			"text": " """ + text + """ "
		},
		"shouldEndSession": true
	}}"""
	
class index:
    def POST(self):
        data = json.loads(web.data())
        if data["request"]["type"] == "IntentRequest":
            intent = data["request"]["intent"]["name"]
            if intent in responses:
				return build_response(responses[intent])
            else:
                return build_response("I did not understand what you asked me.")
		return build_response("")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
