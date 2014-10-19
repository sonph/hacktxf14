import pdb
import logging
import cgi
import os

import webapp2
import jinja2
import blpapi

JINJA_ENV = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENV.get_template('templates/index.html')
        self.response.write(template.render(template_values))
        opts = blpapi.SessionOptions()

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()
