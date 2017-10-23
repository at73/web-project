import webapp2, logging, main
from google.appengine.api import users
from models import *

class UserHandler(webapp2.RequestHandler):
    def get(self):
        if main.current_id == 0:
            template = main.jinja_env.get_template('templates/page_error.html')
            self.response.out.write(template.render())
            main.check = "error"
        else:
            user_id = self.request.get('id')
            user = MyUser.query(MyUser.id_ == user_id).get()
            l = Interests.query(Interests.id_ == user_id).fetch()
            values_to_render = {
                'user': user,
                'interests': l
            }
            template = main.jinja_env.get_template('templates/page_user.html')
            self.response.out.write(template.render(values_to_render))
            main.check = "user"

    def post(self):
        logout_url = ""
        if main.check == "reg":
            id = self.request.get("id")
            name = self.request.get("name")
            password = self.request.get("password")
            user = MyUser.query(MyUser.id_ == id).get()
            if user is None:
                main.current_id = id
                reg_user = MyUser(id_=main.current_id, name_=name, password_=password, age_=18)
                reg_user.put()
                main.check = "current"
            else:
                reg_error = 1
                values_to_render = {
                    'reg_error':reg_error,
                    'name':name,
                    'id': id
                }
                template = main.jinja_env.get_template('templates/page_reg.html')
                self.response.write(template.render(values_to_render))
                main.check = "reg"
        if main.check == "main":
            main_id = self.request.get('id')
            main_password = self.request.get("password")
            #logging.info("check" + " " + main_id + " " + main_password)
            user = MyUser.query((MyUser.id_ == main_id) and (MyUser.password_ == main_password)).get()
            google_user = users.get_current_user()
            if google_user:
                main.current_id = main_id
            else:
                if user is None:
                    template = main.jinja_env.get_template('templates/page_error.html')
                    self.response.out.write(template.render())
                    main.check = "error"
                else:
                    main.current_id = main_id
        if main.check is not "error" and main.check is not "reg":
            user = users.get_current_user()
            if user:
                logout_url = users.create_logout_url('/')
                main.current_id =  user.nickname()
            user = MyUser.query(MyUser.id_ == main.current_id).get()
            l = Interests.query(Interests.id_ == main.current_id).fetch()
            values_to_render = {
                'user': user,
                'interests': l,
                'logout': logout_url
            }
            template = main.jinja_env.get_template('templates/page_current_user.html')
            self.response.out.write(template.render(values_to_render))
            main.check = "current"