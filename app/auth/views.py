from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from .. import db
from ..models import Users
from .forms import LoginForm, RegistrationForm
from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = Users.query.filter_by(username=form.username.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user)
			if user.user_type == 'L':
				return redirect(url_for('landlord.add_property'))
			else:
				return redirect(url_for('tenant.search'))
		else:
			flash('Invalid email or password.')
	return render_template('auth/login.html', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = Users(email = form.email.data,
					name=form.name.data,
					user_type=form.user_type.data,
                    username = form.username.data,
                    password=form.password.data)

		db.session.add(user)
		db.session.commit()
		flash('Successfully Registered')
		return redirect(url_for('auth.login'))

	return render_template('auth/register.html', form=form)

@auth.route('/logout')
@login_required
def logout():

    logout_user()
    flash('You have successfully been logged out.')

    return redirect(url_for('auth.login'))