from flask import abort, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
import json

from .. import db
from ..models import Properties,Users
from . import landlord
from .forms import PropertyRent

def calculate_rent(a):
	return a*a

'''All the routes that render webpages'''

#Page for calculating property rent
@landlord.route('/property', methods=['GET','POST'])
def add_property():
	form = PropertyRent()
	if form.validate_on_submit():
		rent = calculate_rent(2)
		property = Properties(property_name=form.name.data,
					 address=form.address.data,
					 rent=rent,
					 rooms=int(form.rooms.data),
					 landlord=1
					 )
		db.session.add(property)
		db.session.commit()
		return render_template('landlord/property.html', form=form)

	return(render_template('landlord/property.html', form=form))

#Page for showing previous properties
@landlord.route('/prevresults')
def prev_results():
	user = Users.query.get(1)
	properties = user.user_properties
	return render_template('landlord/lproperties.html',properties=properties)

#Give a custom page for every property
@landlord.route('/property/<user>/<property_id>')
def custom_property_page(user, property_id):
	property_details = Properties.query.get(property_id)
	return render_template('landlord/property_details.html',property=property_details)

@landlord.route('/lenquiries')
def enquiries():
	return render_template('landlord/lenquiries.html')

@landlord.route('/llogout')
def landlord_logout():
	return 'a'