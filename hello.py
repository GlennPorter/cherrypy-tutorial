import cherrypy

class OnePage(object):
	def index(self):
		return "One page!"
	index.exposed = True

class HelloWorld:
	onepage = OnePage()
	
	def index(self):
		return "Hello world!"
	index.exposed = True

cherrypy.quickstart(HelloWorld())