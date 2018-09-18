from flask import abort, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
import json

from .. import db
from ..models import *
from . import users
from .forms import *

@users.route('/')
@users.route('/index')
def index():
	return render_template('index.html')

@users.route('/property')
def add_property():
	return render_template('property.html')

@users.route('/subprop', methods=['GET','POST'])
def submit_property():
	form_data = request.form
	return json.dumps({'status':'OK','data':form_data})