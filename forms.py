from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional
from wtforms import SelectField

class UserForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    nin = StringField('NIN', validators=[Optional(), Length(max=20)])
    phone_no = StringField('Phone Number', validators=[Optional(), Length(max=15)])
    next_of_kin_firstname = StringField('Next of Kin (FirstName)', validators=[DataRequired(), Length(max=50)])
    next_of_kin_lastname = StringField('Next of Kin (LastName)', validators=[DataRequired(), Length(max=50)])

    next_of_kin_phone_no = StringField('Next of Kin Phone Number', validators=[DataRequired(), Length(max=15)])
    district = StringField('District', validators=[DataRequired(), Length(max=50)])
    subcounty = StringField('Subcounty', validators=[Optional(), Length(max=50)])
    parish = StringField('Parish', validators=[Optional(), Length(max=50)])
    village = StringField('Village', validators=[Optional(), Length(max=50)])
    residence = StringField('Residence', validators=[DataRequired(), Length(max=50)])
    latitude = StringField('Latitude', validators=[DataRequired()])
    longitude = StringField('Longitude', validators=[DataRequired()])
    nationality = SelectField('Nationality', choices=[
        ('ugandan', 'Ugandan'),
        ('kenyan', 'Kenyan'),
        ('tanzanian', 'Tanzanian'),
        ('rwandese', 'Rwandese'),
        ('south_sudanese', 'South Sudanese')
    ], validators=[DataRequired()])
    submit = SubmitField('Save')
