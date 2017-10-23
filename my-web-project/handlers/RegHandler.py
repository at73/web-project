import webapp2, logging, main
from google.appengine.api import users
from models import *

class RegHandler(webapp2.RequestHandler):
    def get(self):
        reg_error = 0
        values_to_render = {
            'reg_error':reg_error
        }
        template = main.jinja_env.get_template('templates/page_reg.html')
        self.response.write(template.render(values_to_render))
        main.check = "reg"