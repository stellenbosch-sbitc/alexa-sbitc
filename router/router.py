import web
import json

urls = (
	'/alexa', 'index'
)

class index:
	def POST(self):
		return "{}"
	
if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()

