import web
import json

urls = (
    '/alexa', 'index'
)

class index:
    def POST(self):
	data = json.loads(web.data())
	print data
        return """
	{"response": {
         "outputSpeech": {
         "type": "PlainText",
         "text": "Bitches be trippin"
         },
         "shouldEndSession": true
       }
} 
"""

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()


