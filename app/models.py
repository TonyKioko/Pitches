
from . import db
from app import create_app
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    #creating relationship between users and pitches,One User can have many pitches
    pitches = db.relationship("Pitches", backref="user", lazy="dynamic")
    #creating relationship between users and comments,One User can have many comments
    comments = db.relationship("Comments", backref="user", lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'
    # pass_secure = db.Column(db.String(255))

class Pitches(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    body = db.Column(db.String)
    category = db.Column(db.String(255))
    published = db.Column(db.DateTime,default=datetime.utcnow)
    # Foreign key from users table to link pitches and users
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship("Comments", backref="pitches", lazy="dynamic")
    # user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitches.query.filter_by(id=id).all()
        return pitches

    @classmethod
    def get_category(cls, category):
        category = Pitches.query.filter_by(category=category).order_by('-id').all()
        return category

    @classmethod
    def get_all_pitches(cls):
        pitches = Pitches.query.order_by('-id').all()
        return pitches
    def __repr__(self):
        return f'Pitches {self.body}'

class Comments(db.Model):

    __tablename__ = 'comments'


    id = db.Column(db. Integer, primary_key=True)
    the_comment = db.Column(db.String(255))
    # date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

    def save_comment(self):

        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comments = Comments.query.filter_by(pitch_id=id).all()
        return comments

# class Category(db.Model):
   
#     __tablename__ = 'categories'


#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255))
#     description = db.Column(db.String(255))


#     def save_category(self):
#         '''
#         Function that saves a category
#         '''
#         db.session.add(self)
#         db.session.commit()

#     @classmethod
#     def get_categories(cls):
#         '''
#         Function that returns all the data from the categories after being queried
#         '''
#         categories = Category.query.all()
#         return categories





