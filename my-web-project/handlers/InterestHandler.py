import webapp2, logging, main
from google.appengine.api import users
from models import *

class InterestHandler(webapp2.RequestHandler):
    def get(self):
        user = MyUser.query(MyUser.id_ == main.current_id).get()
        l = Interests.query(Interests.id_ == main.current_id).fetch()
        values_to_render = {
            'user': user,
            'interests': l
        }
        template = main.jinja_env.get_template('templates/page_interests.html')
        self.response.out.write(template.render(values_to_render))
        main.check = "interests"

    def post(self):
        function = self.request.get("function")
        if function == "add":
            add = 1
            new_interest = self.request.get("interest")
            list_current = Interests.query(Interests.id_ == main.current_id).fetch()
            for interest_current in list_current:
                if interest_current.value == new_interest:
                    add = 0
            if add:
                interest = Interests(id_=main.current_id, value=new_interest)
                interest.put()
        if function == "delete":
            values = self.request.arguments()
            if values is not None:
                for value in values:
                    delete_interest = Interests.query(Interests.value == value).fetch()
                    if delete_interest:
                        logging.info("deleting" + " " + delete_interest[0].value)
                        delete_interest[0].key.delete()
        user = MyUser.query(MyUser.id_ == main.current_id).get()
        l = Interests.query(Interests.id_ == user.id_).fetch()
        values_to_render = {
            'user': user,
            'interests': l
        }
        template = main.jinja_env.get_template('templates/page_interests.html')
        self.response.out.write(template.render(values_to_render))
        main.check = "interest"