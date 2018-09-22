from flask import abort, render_template, flash, redirect, url_for, request
from flask_login import current_user

#Preceding dots represents the going backward in dirs.
from .. import db
from ..models import Users
from app.auth.forms import RegistrationForm
#Imports home from __init__.py file in home directory
from . import home

@home.route('/', methods=['GET','POST'])
@home.route('/index', methods=['GET','POST'])
def index():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = Users(email = form.email.data,
					name=form.name.data,
					user_type=form.user_type.data,
                    mobile_no = form.mobile_no.data,
                    password=form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Successfully Registered')
		return redirect(url_for('auth.login'))
	return render_template('/home/index.html', form= form)

@home.route('/services')
def services():
	return render_template('services.html')

@home.route('/about')
def about():
	return render_template('property.html')

@home.route('/contact', methods=['GET','POST'])
def contact():
	return render_template('home/contact.html')