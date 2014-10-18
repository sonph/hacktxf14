import pdb
import logging
import cgi
import os

import webapp2
import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

JINJA_ENV = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = True
)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENV.get_template('templates/home.html')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', HomeHandler),
], debug=True)
