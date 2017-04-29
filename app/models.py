from . import db

class UserProfile(db.Model):
    __table__name = 'user_profile'
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    userid = db.Column(db.Integer, unique=True,primary_key=True)
    email = db.Column(db.String(80))
    password = db.Column(db.String(255))
    hash_number = db.Column(db.String(180))
    secretques=db.Column(db.String(255))
    secretans=db.Column(db.String(180))
    gender = db.Column(db.String(20))
    image = db.Column(db.String(255))
    accept_tos=db.Column(db.String(6))
    created = db.Column(db.DateTime())

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.userid)  # python 2 support
        except NameError:
            return str(self.userid)  # python 3 support
            
    def __init__(self, first_name, last_name, username, userid, email, password, hash_number, secretques, secretans, gender, image, accept_tos, created):
         self.first_name = first_name
         self.last_name = last_name
         self.username = username
         self.userid=userid
         self.email=email
         self.password=password
         self.hash_number = hash_number
         self.secretques=secretques
         self.secretans=secretans
         self.gender = gender
         self.image = image
         self.accept_tos=accept_tos
         self.created= created

    def __repr__(self):
        return '<User %r>' % (self.userid)
        
class Wishlist(db.Model):
    __table__name = 'wishlist'
    userid = db.Column(db.Integer)
    itemid = db.Column(db.Integer, unique=True,primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(2500))
    item_url = db.Column(db.String(255))
    image_url = db.Column(db.String(300))
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.userid)  # python 2 support
        except NameError:
            return str(self.userid)  # python 3 support    
            
    def __init__(self, userid, itemid, title,  description, item_url, img_url):
        self.userid = userid
        self.itemid = itemid
        self.title = title 
        self.description = description 
        self.item_url = item_url
        self.image_url = img_url
       
        
    def __repr__(self):
        return '<User %r>' % (self.userid)
        
        