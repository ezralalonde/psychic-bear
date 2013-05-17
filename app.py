import webapp2
import os

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!\n\n')

        path = os.path.join(os.path.split(__file__)[0], 'static/hi.txt')
        self.response.out.write(open(path).readlines()[0])

application = webapp2.WSGIApplication([('/.*', MainPage)])
