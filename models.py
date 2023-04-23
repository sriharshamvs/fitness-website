from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

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
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), nullable=True)
    about = db.Column(db.String(500), nullable=True)

    plan = db.relationship('Plan', backref='users', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
