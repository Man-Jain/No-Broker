from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, IntegerField, FileField
from wtforms.validators import DataRequired

class PropertyRent(FlaskForm):

	name = StringField('Property Name', validators=[DataRequired()])
	address = StringField('Address', validators=[DataRequired()])
	rooms = StringField('No of Rooms', validators=[DataRequired()])
	submit = SubmitField('Submit')