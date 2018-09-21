from flask import abort, render_template, flash, redirect, url_for, request
from flask_login import current_user

#Preceding dots represents the going backward in dirs.
from .. import db
#from ..models import Feedback
#from .forms import FeedbackForm
#Imports home from __init__.py file in home directory
from . import home

@home.route('/')
@home.route('/index')
def index():
	return render_template('/home/index.html')

@home.route('/services')
def services():
	return render_template('services.html')

@home.route('/about')
def about():
	return render_template('property.html')

@home.route('/contact', methods=['GET','POST'])
def contact():
	return render_template('home/contact.html')