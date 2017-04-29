from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, FileField, HiddenField, PasswordField, BooleanField, validators
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed

class WishlistForm(FlaskForm):
    firstname = StringField('Firstname: ', validators=[InputRequired()])
    lastname = StringField('Lastname: ', validators=[InputRequired()])
    username = StringField('Username: ', validators=[InputRequired(), validators.Length(min=4, max=25)])
    email = StringField('Email Address', validators=[InputRequired(),validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match') ])
    confirm = PasswordField('Confirm Password')
    gender = SelectField('Gender: ', choices=[('', ''), ('Female', 'Female'),('Male', 'Male'),('Not Specified','Not Specified')])
    secretques=SelectField('Secret Question: ', choices=[('', ''), ('What is the first name of the person you first kissed?', 
    'What is the first name of the person you first kissed?'),('Select a number between 1020 and 3089', 'Select a number between 1020 and 3089'),
    ('What is your guilty pleasure','What is your guilty pleasure')])
    secretans=StringField('Answer: ', validators=[InputRequired()])
    accept_tos = BooleanField('I accept', [validators.DataRequired()])
    
class WishlistLoginForm(FlaskForm):
        email = StringField('Email Address', validators=[InputRequired(),validators.Length(min=6, max=35)])
        password = PasswordField('Password', [validators.DataRequired() ])
        

class ResetForm(FlaskForm):
        email = StringField('Email Address', validators=[InputRequired(),validators.Length(min=6, max=35)])
      
    
class AddToWishlistForm(FlaskForm):
        item_url = StringField('Item URL: ', validators=[InputRequired()])
        title= StringField('Title: ', validators=[InputRequired()])
        description= StringField('Description: ', validators=[InputRequired()])
        
    