import os
from cryptography.fernet import Fernet
from functools import wraps
from flask_login import current_user
from flask import jsonify, Blueprint, request, Response, render_template, redirect, url_for
from flask_login import current_user, login_required
from country_project.models import User as USERS


secure = Blueprint('secure', __name__)
# secret_key = os.getenv('SECRET_KEY')
secret_key = Fernet.generate_key()
cipher_suite = Fernet(secret_key.decode())


def encrypt_data(data):
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data.decode()


def decrypt_data(encrypted_data):
    decrypted_data = cipher_suite.decrypt(encrypted_data.encode())
    return decrypted_data.decode()


def check_auth(username, password):
    """Check if a username/password combination is valid."""
    user = USERS.get(username)
    if user and user.password == password:
        return user
    return None


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()

        user = check_auth(auth.username, auth.password)
        if not user:
            return authenticate()

        api_key = request.headers.get('x-api-key')
        if not api_key:
            return jsonify({"error": "API key is missing"}), 401

        if user.api_key != api_key:
            return jsonify({"error": "Invalid API key"}), 403

        return f(*args, **kwargs)
    return decorated_function


@secure.route('/secure/generate_api_key', methods=['GET', 'POST'])
@login_required
def generate_api_key():
    user = current_user
    user.generate_api_key()
    # return jsonify({'api_key': user.api_key}), 200\
    return redirect(url_for('secure.display_api_key'))


@secure.route('/display_api_key', methods=['GET'])
@login_required
def display_api_key():
    api_key = request.args.get('api_key')
    return render_template('display_api_key.html', api_key=api_key)


@secure.route('/generate_api_key')
@login_required
def secure_generate_api_key():
    return render_template('generate_api_key.html')
