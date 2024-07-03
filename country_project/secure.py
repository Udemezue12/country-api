import os
from cryptography.fernet import Fernet
from functools import wraps
from flask_login import current_user
from flask import jsonify, Blueprint, request, render_template, redirect, url_for
from flask_login import current_user, login_required


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


def require_api_key(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if not api_key:
            return jsonify({"error": "API key is missing"}), 401
        
        if current_user.is_anonymous:
            return jsonify({"error": "User not logged in"}), 401

        if current_user.api_key != api_key:
            return jsonify({"error": "Invalid API key"}), 403

        return func(*args, **kwargs)
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