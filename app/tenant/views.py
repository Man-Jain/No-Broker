from flask_login import current_user, login_required
from flask import abort, render_template, flash, redirect, url_for, request
import json

from .. import db
from ..models import Enquiries, Properties, Users
from . import tenant
from .forms import *

'''All the routes that render webpages.'''
#Route for tenant dashboard
@tenant.route('/search', methods=['GET','POST'])
@login_required
def search():
	form = Search()
	if form.validate_on_submit():
		user_data = {'location':form.location.data,'rooms':form.rooms.data}
		return json.dumps(user_data, indent=2)
	return render_template('tenant/search.html', form=form)

#List of properties user enquired for
@tenant.route('/userenquiries')
@login_required
def user_enquiries():
	user = Users.query.get(current_user.user_id)
	enquiries = user.user_enquiries
	return render_template('tenant/uenquiries.html', enquiries=enquiries)