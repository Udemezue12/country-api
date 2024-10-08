import os
from dotenv import load_dotenv
import stripe
from flask import render_template, Blueprint, request, url_for, redirect, jsonify, flash
from country_project.database import db
from country_project.models import User
from flask_login import current_user, login_required
# from country_project.states import states


# @login_manager.user_loader
# def load_user(user):
#     return User.query.get(int(user))


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
load_dotenv()

core = Blueprint('core', __name__)

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
public_key = os.getenv('STRIPE_PUBLIC_KEY')


@core.route('/')
def index():
    return render_template('index.html')


@core.route('/flask/instructions', methods=['GET'])
@login_required
def dashboard():
    # if current_user.role != 'api-user':
    #     flash('Unauthorized access!', 'danger')
    #     return redirect(url_for('core.index'))
    return render_template('dashboard.html')


@login_required
@core.route('/skip')
def skip():
    return redirect(url_for('users.login'))


@core.route('/info')
def info():
    return render_template('info.html')


@core.route('/payment', methods=['POST'])
def payment():

    # CUSTOMER INFORMATION
    customer = stripe.Customer.create(email=request.form['stripeEmail'],
                                      source=request.form['stripeToken'])

    # CHARGE/PAYMENT INFORMATION
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=1999,
        currency='usd',
        description='Donation'
    )

    return redirect(url_for('core.thankyou'))
