# import pycountry
import os
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from flask import request, jsonify
# from wtforms_components import SelectField
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField, FileField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp
import requests
from country_project import app
from country_project.country.country_list import country_choices
# from country_project.states import get_countries

load_dotenv()
# country_choices = get_countries()
USERNAME = os.getenv('GEONAME_USERNAME')


class UserRegistrationForm(FlaskForm):
    role = SelectField(
        'Role', choices=[('passenger', 'Passenger')], validators=[DataRequired()], default='passenger')

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'password2', message='Passwords do not match')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class APIUserRegistrationForm(FlaskForm):
    role = SelectField(
        'Role', choices=[('api-user', 'User')], validators=[DataRequired()], default='api-user')

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'password2', message='Passwords do not match')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class APIUserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    date_of_birth = DateField(
        'Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
    country = SelectField('Country',
                          validators=[DataRequired()])
    # country = SelectField('Country', validators=[DataRequired()])
    state = SelectField('State', choices=[], validators=[DataRequired()])

    phone_number = StringField('Phone Number', validators=[
        DataRequired(),
        Regexp(r'^(\+234\d{10}|0\d{10})$',
               message="Invalid phone number. Must be in the format +234XXXXXXXXXX or 0XXXXXXXXXX")
    ])
    submit = SubmitField('Register')

