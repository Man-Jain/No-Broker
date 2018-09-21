from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from app import db, login_manager

class Users(UserMixin, db.Model):
	__tablename__ = 'users'

	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(60), index=True, unique=True)
	name = db.Column(db.String(50))
	user_type = db.Column(db.String(1))
	password_hash = db.Column(db.String(128))
	user_properties = db.relationship('Properties', backref = 'user_property', lazy='dynamic')

	@property
	def password(self):

		raise AttributeError('password is not a readable attribute.')

	@password.setter
	def password(self, password):

		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):

		return check_password_hash(self.password_hash, password)

	def __repr__(self, username):
		return '<User: {}>'.format(username)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Properties(db.Model):
	__tablename__ = 'properties'

	property_id = db.Column(db.Integer, primary_key=True)
	property_name = db.Column(db.String(255))
	address = db.Column(db.String(255))
	rent = db.Column(db.Integer)
	rooms = db.Column(db.Integer)
	landlord = db.Column(db.Integer, db.ForeignKey('users.user_id'))

	def __repr__(self, property_id):
  		return '<Property: {}>'.format(property_id)