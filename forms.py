from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class UserForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    nin = StringField('NIN', validators=[Optional(), Length(max=20)])
    phone_no = StringField('Phone Number', validators=[Optional(), Length(max=15)])
    next_of_kin = StringField('Next of Kin', validators=[DataRequired(), Length(max=50)])
    next_of_kin_phone_no = StringField('Next of Kin Phone Number', validators=[DataRequired(), Length(max=15)])
    district = StringField('District', validators=[DataRequired(), Length(max=50)])
    subcounty = StringField('Subcounty', validators=[DataRequired(), Length(max=50)])
    parish = StringField('Parish', validators=[DataRequired(), Length(max=50)])
    village = StringField('Village', validators=[DataRequired(), Length(max=50)])
    residence = StringField('Residence', validators=[DataRequired(), Length(max=50)])
    latitude = StringField('Latitude', validators=[DataRequired()])
    longitude = StringField('Longitude', validators=[DataRequired()])
    submit = SubmitField('Save')
