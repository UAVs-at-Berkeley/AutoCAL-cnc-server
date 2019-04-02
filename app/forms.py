from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, IntegerField
from wtforms.validators import DataRequired

class DataForm(FlaskForm):
    altitude = DecimalField('Altitude', validators=[DataRequired()])
    latitude = DecimalField('Latitude', validators=[DataRequired()])
    longitude = DecimalField('Longitude', validators=[DataRequired()])
    airspeed = IntegerField('Airspeed', validators=[DataRequired()])
    time = StringField('Time')
    submit = SubmitField('Enter')
