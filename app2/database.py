from google.appengine.ext import db

class Blacklisttable(db.Model):
   useremail = db.StringProperty()
#end class Blacklisttable ...
class Userstable(db.Model):
   useremail = db.StringProperty()
   profileimage = db.BlobProperty()
#end class Userstable ...
class Needitstable(db.Model):
   need = db.StringProperty()
   urgency = db.StringProperty()
   offer = db.IntegerProperty()
   location = db.StringProperty()
   userphonenumber = db.StringProperty()
   useremail = db.StringProperty()
   username = db.StringProperty()
   timestamp = db.IntegerProperty()
   views = db.IntegerProperty()
#end class Needitstable ...
