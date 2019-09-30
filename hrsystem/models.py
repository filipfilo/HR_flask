from datetime import datetime
from hrsystem import db
import flask_whooshalchemy as wa


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class Employee(db.Model):
    __searchable__ = ['id', 'first_name', 'last_name']
    id = db.Column(db.String(20), unique=True, primary_key=True)
    citizenship = db.Column(db.String(20), unique=False, nullable=False)
    city = db.Column(db.String(20), unique=True, nullable=False)
    country_of_residence = db.Column(
        db.String(20), unique=False, nullable=False)
    date_of_birth = db.Column(db.String(20), unique=False, nullable=False)
    first_name = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
    national_id = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    state = db.Column(db.String(20), unique=False, nullable=False)
    street_address = db.Column(db.String(20), unique=False, nullable=False)
    telephone_number = db.Column(db.String(20), unique=True, nullable=False)
    zipcode = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    band = db.Column(db.String(20), unique=False, nullable=False)
    contract_beginning = db.Column(db.String(20), unique=False, nullable=False)
    contract_end = db.Column(db.String(20), unique=False, nullable=False)
    contract_type = db.Column(db.String(20), unique=False, nullable=False)
    department = db.Column(db.String(20), unique=False, nullable=False)
    employment_status = db.Column(db.String(20), unique=False, nullable=False)
    fte = db.Column(db.String(20), unique=False, nullable=False)
    salary = db.Column(db.String(20), unique=False, nullable=False)
    is_manager = db.Column(db.String(20), unique=False, nullable=False)
    job_title = db.Column(db.String(20), unique=False, nullable=False)
    manager = db.Column(db.String(20), unique=False, nullable=False)
    subsidiary = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return f"Post('{self.username}', '{self.password}')"
