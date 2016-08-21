import web
import json

urls = (
    '/alexa', 'index'
)

# Hardcoded responses in the format
# "IntentName" : "Desired Response"
responses = {
}

class index:
    def build_response(text):
        return """
        { "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": " """ + text + """ "
            },
            "shouldEndSession": true
        }}"""

    def POST(self):
        data = json.loads(web.data())
        if data["request"]["type"] == "IntentRequest":
            intent = data["request"]["intent"]["name"]
            return build_response(responses[intent])
        return build_response("")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
