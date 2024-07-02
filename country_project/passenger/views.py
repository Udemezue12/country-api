import os
import requests
from werkzeug.security import generate_password_hash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from sqlalchemy.exc import IntegrityError
from flask import Flask, render_template, redirect, url_for, flash, request, jsonify, Blueprint
from country_project.forms import APIUserForm, APIUserRegistrationForm
from country_project.models import User, APIUser
from country_project.login import login_manager
from country_project.database import db
from country_project.utils import IMAGE, DOCUMENT
import logging
from country_project.code.states import states
from country_project.country.country_list import country_choices
# import pycountry
from dotenv import load_dotenv

load_dotenv()

MAPBOX_KEY = os.getenv('MAPBOX_KEY')

passenger = Blueprint('passenger', __name__)


@login_manager.user_loader
def load_user(user):
    return User.query.get(int(user))


def validate_password(password):
    if not password:
        raise ValueError('Password cannot be empty or None.')
    if len(password) < 8:
        raise ValueError('Password must be at least 12 characters long.')


# @passenger.route('/api/nigeria', methods=['GET'])
# def get_nigeria_data():
#     response = requests.get(
#         'https://locationsng-api.herokuapp.com/api/v1/lgas')
#     if response.status_code == 200:
#         return jsonify(response.json())
#     else:
#         return jsonify({'error': 'Failed to fetch data'}), 500
# @principal.route('/generate_pin')
# def generate_pin_view():
#     pin = generate_pin()
#     return render_template('display_pin.html', pin=pin)


@passenger.route('/dashboard')
@login_required
def passenger_dashboard():
    return render_template('passenger_dashboard.html')


@passenger.route('/passenger_form/<int:user_id>', methods=['GET', 'POST'])
def passenger_form(user_id):
    form = APIUserForm()
    form.country.choices = country_choices()
    if request.method == 'POST':
        selected_country = request.form.get('country')
        form.state.choices = [(state, state)
                              for state in states.get(selected_country, [])]
    if form.validate_on_submit():
        #     picture_filename = secure_filename(form.picture.data.filename)
        #     id_document_filename = secure_filename(form.id_document.data.filename)

        #     form.picture.data.save(os.path.join(IMAGE, picture_filename))
        #     form.id_document.data.save(
        #         os.path.join(DOCUMENT, id_document_filename))
        try:
            passenger = APIUser(



                user_id=user_id,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                date_of_birth=form.date_of_birth.data,
                phone_number=form.phone_number.data,
                country=form.country.data,
                state=form.state.data,

            )
            db.session.add(passenger)
            db.session.commit()
            flash('Passenger information submitted successfully!', 'success')
            return redirect(url_for('users.login'))
        except ValueError as e:
            flash(str(e), 'danger')
        except IntegrityError as e:
            db.session.rollback()
            logging.error("IntegrityError occurred: %s", e)
            flash("An error occurred during submission. Please try again.", 'danger')
    return render_template('passenger_form.html', form=form)


@passenger.route('/passenger/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('users.login'))

    form = APIUserRegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash(
                'Username already exists. Please choose a different username.', 'danger')
            return redirect(url_for('passenger.register'))

        try:
            password = form.password.data
            validate_password(password)

            user = User(
                role=form.role.data,
                email=form.email.data,
                username=form.username.data,
                password=password,
            )

            db.session.add(user)
            db.session.commit()

            if user.role == 'api-user':
                return redirect(url_for('passenger.passenger_form', user_id=user.id))

            flash('Thanks for registering!', 'success')
            return redirect(url_for('users.login'))
        except ValueError as e:
            flash(str(e), 'danger')
        except IntegrityError as e:
            db.session.rollback()
            logging.error("IntegrityError occurred: %s", e)
            flash("An error occurred during registration. Please try again.", 'danger')

    return render_template('passenger_register.html', form=form)