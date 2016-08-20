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
         "text": "We can't reach it Sarah"
         },
         "shouldEndSession": true
       }
} 
"""

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()


