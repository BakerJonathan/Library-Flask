from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

from flask_login import UserMixin,LoginManager
from flask_marshmallow import Marshmallow

db =SQLAlchemy()

login_manager=LoginManager()
ma=Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    id=db.Column(db.String,primary_key=True)
    first_name=db.Column(db.String(150),nullable=True,default='')
    last_name=db.Column(db.String(150),nullable=True,default='')
    email=db.Column(db.String(150),nullable=False)
    password=db.Column(db.String,nullable=True,default='')
    g_auth_verify=db.Column(db.Boolean,default=False)
    token=db.Column(db.String, default='', unique=True)
    date_created=db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    def __init__(self, email, first_name='', last_name='', id='', password='', token='', g_auth_verify=False):
        self.id=self.set_id()
        self.email=email
        self.first_name=first_name
        self.last_name=last_name
        self.password=self.set_password(password)
        self.token=self.set_token(24)
        self.g_auth_verify=g_auth_verify

    def set_token(self,length):
        return secrets.token_hex(length)
    
    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self,password):
        self.pw_hash=generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f'User {self.email} was added to the database'
    


class Book(db.Model):
    id=db.Column(db.String, primary_key=True)
    book_title=db.Column(db.String(150))
    ISBN=db.Column(db.Numeric(precision=20, scale=0))
    author=db.Column(db.String(150))
    publisher=db.Column(db.String(150))
    book_length=db.Column(db.Numeric(precision=10,scale=0))
    cover_type=db.Column(db.String(70))
    rental_status=db.Column(db.String(100))
    renter=db.Column(db.String(150))
    language=db.Column(db.String(100))
    user_token=db.Column(db.String, db.ForeignKey('user.token'), nullable=False) 


    def __init__(self, book_title, ISBN, author, publisher, book_length, cover_type, rental_status, renter, language, user_token, id=''):
        self.id=self.set_id()
        self.book_title=book_title
        self.ISBN=ISBN
        self.author=author
        self.publisher=publisher
        self.book_length=book_length
        self.cover_type=cover_type
        self.rental_status=rental_status
        self.renter= renter
        self.language=language
        self.user_token=user_token

    def __repr__(self):
        return f'The following book was added: {self.book_title}'
    
    def set_id(self):
        return (secrets.token_urlsafe())
    
class BookSchema(ma.Schema):
    class Meta:
        fields=['id','book_title','ISBN', 'author','publisher','publisher','book_length','cover_type','rental_status','renter','language']

book_schema= BookSchema()
books_schema= BookSchema(many=True)
