import webapp2, logging, main
from google.appengine.api import users
from models import *

class ListHandler(webapp2.RequestHandler):
    def get(self):
        if main.current_id == 0:
            template = main.jinja_env.get_template('templates/page_error.html')
            self.response.out.write(template.render())
            main.check = "error"
        else:
            values_to_render = {
                'list': MyUser.query().fetch(),
            }
            template = main.jinja_env.get_template('templates/page_all_users.html')
            self.response.out.write(template.render(values_to_render))
            main.check = "all"