import webapp2, logging, main
from google.appengine.api import users
from models import *

class DataHandler(webapp2.RequestHandler):
    def get(self):
        user = MyUser.query(MyUser.id_ == main.current_id).get()
        values_to_render = {
            'user': user,
        }
        template = main.jinja_env.get_template('templates/page_user_data.html')
        self.response.out.write(template.render(values_to_render))
        main.check = "data"

    def post(self):
        function = self.request.get("function")
        user = MyUser.query(MyUser.id_ == main.current_id).get()
        if function == "name":
            name = self.request.get("name")
            user.name_=name
            user.put()
        if function == "age":
            age = self.request.get("age")
            user.age_ = int(age)
            user.put()
        values_to_render = {
            'user': user,
        }
        template = main.jinja_env.get_template('templates/page_user_data.html')
        self.response.out.write(template.render(values_to_render))
        main.check = "data"