from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Plan('{self.name}', '{self.price}', '{self.description}')"


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(10), nullable=False)
    about = db.Column(db.String(500), nullable=True)
    first_name = db.Column(db.String(20), nullable=True)
    last_name = db.Column(db.String(20), nullable=True)
    mobile_number = db.Column(db.String(10), unique=True, nullable=True)
    age = db.Column(db.Integer, unique=False, nullable=True)
    height = db.Column(db.Integer, unique=False, nullable=True)
    weight = db.Column(db.Integer, unique=False, nullable=True)

    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), nullable=True)
    plan = db.relationship('Plan', backref='users', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    reps = db.Column(db.String(120), nullable=False)
    video_id = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return f'<Workout {self.name}>'


class Nutrition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(50), nullable=False)
    meal = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String(255))
