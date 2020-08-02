from datetime import datetime
from flaskbyge import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    def __repr__(self):
        return f"user('{self.username}', '{self.email}', '{self.image.file}')"

class Post(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    pic = db.Column(db.String(20), nullable=False, default='')
    discription = db.Column(db.String(''), nullable=False)
    zone = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating =  db.Column(db.Integer, default='4', nullable=False)
def __repr__(self):
        return f"post('{self.pic}', '{self.discription}', '{self.zone}', '{self.price}')"