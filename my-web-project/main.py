import jinja2, os, webapp2
from handlers.MainHandler import *
from handlers.RegHandler import *
from handlers.UserHandler import *
from handlers.InterestHandler import *
from handlers.RecomHandler import *
from handlers.DataHandler import *
from handlers.ListHandler import *

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

check = "main"
current_id = 0
my_url = "https://my-web-project-9.appspot.com/"


app = webapp2.WSGIApplication([
                                ('/', MainHandler),
                                ('/reg', RegHandler),
                                ('/user_main', UserHandler),
                                ('/recom', RecomHandler),
                                ('/interests', InterestHandler),
                                ('/user_data', DataHandler),
                                ('/all_users', ListHandler),
                                ('/user', UserHandler),
                            ], debug = True)
