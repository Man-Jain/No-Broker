from flask import abort, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
import json

from .. import db
from ..models import *
from . import tenant
from .forms import *

'''All the routes that render webpages.'''
#Route for tenant dashboard
@tenant.route('/tdash')
def tdash():
	return render_template('index.html')

#List of properties user enquired for
@tenant.route('/userenquiries')
def user_enquiries():
	return render_template('property.html')

'''Routes for from posting'''
#Search for property
@tenant.route('/searchprop', methods=['GET','POST'])
def search_property():
	form_data = request.form
	return json.dumps({'status':'OK','data':form_data})