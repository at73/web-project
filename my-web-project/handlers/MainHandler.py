import webapp2, logging, main
from google.appengine.api import users
from models import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main.current_id = 0
        user = users.get_current_user()
        if user:
            nickname = user.nickname()
            main.current_id = nickname
            logout_url = users.create_logout_url('/')
            user = MyUser.query(MyUser.id_ == nickname).get()
            if user is None:
                main.current_id = nickname
                MyUser(id_=main.current_id, name_=nickname, age_=18).put()
            login = 1
            values_to_render = {
                'nickname': nickname,
                'logout_url': logout_url,
                'login': login,
            }
        else:
            login_url = users.create_login_url('/')
            login = 0
            values_to_render = {
                'login_url': login_url,
                'login': login,
            }
        template = main.jinja_env.get_template('templates/page_main.html')
        self.response.write(template.render(values_to_render))
        main.check = "main"