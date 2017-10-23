from google.appengine.ext import ndb

class MyUser(ndb.Model):
    id_ = ndb.StringProperty()
    password_ = ndb.StringProperty()
    name_ = ndb.StringProperty()
    age_ = ndb.IntegerProperty(default = 18)


class Interests(ndb.Model):
    id_ = ndb.StringProperty()
    value = ndb.StringProperty()