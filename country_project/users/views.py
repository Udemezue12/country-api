import random
import os
import string
from flask_mail import Message
from flask_bcrypt import generate_password_hash
import css_inline

from itsdangerous.exc import BadTimeSignature, BadSignature
from dotenv import load_dotenv
from flask import render_template, url_for, flash, redirect, request, Blueprint, current_app

from sqlalchemy.exc import IntegrityError
from flask_login import login_user, current_user, logout_user, login_required
from country_project.models import User
from country_project.users.forms import RegistrationForm, LoginForm, UpdateForm, ForgotPasswordForm, ResetPasswordForm
# from country_project.utils import save_picture
# from country_project.models import Teacher, Student, UserPin
from country_project.database import bcrypt, db
from config import mail, serializer, salt
from country_project.login import login_manager


load_dotenv()


senders_mail = os.getenv('MAIL_HOST_USER')


users = Blueprint('users', __name__)


# def generate_pin():
#     pin = ''.join(random.choices(string.digits, k=6))
#     new_pin = UserPin(pin_code=pin)
#     db.session.add(new_pin)
#     db.session.commit()
#     return pin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@users.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data + salt):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('core.index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))


# @users.route('/dashboard')
# @login_required
# def dashboard():
#     if current_user.role == 'admin':
#         return render_template('admin_dashboard.html')
#     elif current_user.role == 'passenger':
#         return render_template('passenger_dashboard.html')
#     elif current_user.role == 'driver':
#         return render_template('driver_dashboard.html')

#     else:
#         return render_template('index.html')


@users.route('/updating_profile', methods=['GET', 'POST'])
@login_required
def profile():
    if current_user.role == 'driver':
        return render_template('driver_update_profile.html')
    elif current_user.role == 'passeneger':
        return render_template('passenger_update_profile.html')
    else:
        return render_template('index.html')






def send_mail(to, template, subject, link, username, **kwargs):
    with current_app.app_context():
        sender = current_app.config['MAIL_USERNAME']  
        msg = Message(subject=subject, sender=sender, recipients=[to])
        html = render_template(template, username=username, link=link, **kwargs)
        inlined = css_inline.inline(html)
        msg.html = inlined
        mail.send(msg)


@users.route("/reset_password", methods=["POST", "GET"])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        email = form.email.data

        user = User.query.filter_by(email=email).first()
        if user:
            username = user.username
            hashCode = serializer.dumps(email, salt="reset-password")
            user.hashCode = hashCode
            server = current_app.config['SERVER_URL']
            link = f"{server}/{hashCode}"
            db.session.commit()
            send_mail(
                to=email,
                template="email.html",
                subject="Reset Password",
                username=username,
                link=link,
            )
            flash("A password reset link has been sent to your email!", "success")
            return redirect(url_for('users.login'))
        else:
            flash("User does not exist!", "danger")

    return render_template('forgot_password.html', title='Forgot Password', form=form)


@users.route("/<string:hashCode>", methods=["GET", "POST"])
def hashcode(hashCode):
    try:
        email = serializer.loads(hashCode, salt="reset-password", max_age=3600)
    except BadTimeSignature:
        flash("The password reset link has expired. Please request a new one.", "danger")
        return redirect(url_for("core.index"))
    except BadSignature:
        flash("Invalid password reset link. Please request a new one.", "danger")
        return redirect(url_for("core.index"))

    user = User.query.filter_by(email=email).first()
    if not user:
        flash("User does not exist!", "danger")
        return redirect(url_for("core.index"))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        if form.password.data == form.confirm_password.data:
            user.password = bcrypt.generate_password_hash(form.password.data + salt).decode('utf-8')
            user.hashCode = None
            db.session.commit()
            flash("Your password has been reset successfully!", "success")
            return redirect(url_for("users.login"))
        else:
            flash("Password fields do not match.", "danger")

    return render_template("reset_password.html", form=form, hashCode=hashCode)
