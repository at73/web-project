import webapp2, logging, main
from google.appengine.api import users
from math import sqrt
from models import *

class RecomHandler(webapp2.RequestHandler):
    def post(self):
        users = MyUser.query().fetch()
        user_c = MyUser.query(MyUser.id_ == main.current_id).get()
        list_current = Interests.query(Interests.id_ == main.current_id).fetch()
        similarity = {}
        for user in users:
            list_other = Interests.query(Interests.id_ == user.id_).fetch()
            count_common = 0
            for interest_current in list_current:
                for interest in list_other:
                    if interest.value == interest_current.value:
                        count_common += 1
            if sqrt(len(list_current)*len(list_other)) != 0:
                k = count_common/sqrt(len(list_current)*len(list_other))
            else:
                k = 0
            similarity[user.id_] = k

        weight = {}
        list_id = Interests.query(Interests.id_ != main.current_id).fetch()
        for interests in sorted(list_id):
                count = 0
                k = 0
                list_with_this_interest = \
                    Interests.query(Interests.value == interests.value,
                                    Interests.id_ != user_c.id_).fetch()
                for interest in list_with_this_interest:
                    count += 1
                    if interest.id_ in similarity:
                        k += similarity[interest.id_]
                if k > 0:
                    weight[interests.value] = k/count

        for interest_current in list_current:
            if interest_current.value in weight:
                del weight[interest_current.value]
        weight_sort = weight.items()
        weight_sort.sort(key=lambda item: item[1], reverse=True)
        user_c = MyUser.query(MyUser.id_ == main.current_id).get()
        values_to_render = {
            'user': user_c,
            'interests': list_current,
            'weight': weight_sort
        }
        template = main.jinja_env.get_template('templates/page_recom.html')
        self.response.write(template.render(values_to_render))
        main.check = "rec"