import requests
from functools import wraps
import string
import random
import os
from flask import abort
from flask_login import current_user
from dotenv import load_dotenv
import secrets
from PIL import Image
from flask import current_app
from werkzeug.utils import secure_filename


load_dotenv()

RANDOM_ORG_API_KEY = os.getenv('RANDOM_ORG_API_KEY')


# def admin_required(f):
#     @wraps(f)
#     def decorated_fuction(*args, **kwargs):
#         if current_user != 'admin':
#             abort(403)
#             return f(*args, **kwargs)
#         return decorated_fuction


# def teacher_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if current_user != 'teacher':
#             abort(403)
#         return f(*args, **kwargs)
#     return decorated_function


# def student_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if current_user != 'student':
#             abort(403)
#         return f(*args, **kwargs)
#     return decorated_function


# def principal_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if current_user != 'principal':
#             abort(403)
#         return f(*args, **kwargs)
#     return decorated_function


def generated_pin():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


def generate_pin():
    url = 'https://api.random.org/json-rpc/4/invoke'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": RANDOM_ORG_API_KEY,
            "n": 1,
            "min": 100000,
            "max": 999999,
            "replacement": True
        },
        "id": 42
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        result = response.json()
        return str(result['result']['random']['data'][0])
    else:
        raise Exception('Error generating PIN')


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


IMAGE = 'drive_project/static/images'
DOCUMENT = 'drive_project/static/documents'

if not os.path.exists(IMAGE):
    os.makedirs(IMAGE)
if not os.path.exists(DOCUMENT):
    os.makedirs(DOCUMENT)


def save_file(file):

    upload_folder = os.path.join(current_app.root_path, 'uploads')

    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    # Secure the file name and save the file
    filename = secure_filename(file.filename)
    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)

    return file_path


# def country_choices():
#     return [


        
#          ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('American Samoa', 'American Samoa'), ('Andorra', 'Andorra'), 
#          ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antarctica', 'Antarctica'), ('Antigua and Barbuda', 'Antigua and Barbuda'), ('Argentina', 'Argentina'), 
#          ('Armenia', 'Armenia'), ('Aruba', 'Aruba'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), 
#          ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), 
#          ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), 
#          ('Bolivia', 'Bolivia'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei Darussalam', 'Brunei Darussalam'), 
#          ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), 
#          ('Canada', 'Canada'), ('Cape Verde', 'Cape Verde'), ('Cayman Islands', 'Cayman Islands'), ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), 
#          ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), 
#          ('Congo, the Democratic Republic of the', 'Congo, the Democratic Republic of the'), ('Cook Islands', 'Cook Islands'), ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), 
#          ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), 
#          ('Dominican Republic', 'Dominican Republic'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guniea', 'Equatorial Guinea'), 
#          ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethopia', 'Ethiopia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), 
#          ('France', 'France'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), 
#          ('Ghana', 'Ghana'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guam', 'Guam'), ('Guatemala', 'Guatemala'), 
#          ('Guniea', 'Guinea'), ('Guniea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), 
#          ('Hong Kong', 'Hong Kong'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), 
#          ('Iran', 'Iran, Islamic Republic of'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Israel', 'Israel'), ('Italy', 'Italy'), 
#          ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), 
#          ('Kiribati', 'Kiribati'), ('North Korea', "North Korea, Democratic People's Republic of"), ('Korea', 'Korea, Republic of'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), 
#          ('Lao People Republic', "Lao People  Republic"), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), 
#          ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Macao', 'Macao'), 
#          ('Macedonia', 'Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), 
#          ('Mali', 'Mali'), ('Malta', 'Malta'), ('MH', 'Marshall Islands'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), 
#          ('MX', 'Mexico'), ('FM', 'Micronesia, Federated States of'), ('MD', 'Moldova, Republic of'), ('MC', 'Monaco'), ('MN', 'Mongolia'), 
#          ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), 
#          ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('NZ', 'New Zealand'), 
#          ('NI', 'Nicaragua'), ('NE', 'Niger'), ('Nigeria', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolk Island'), 
#          ('MP', 'Northern Mariana Islands'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), 
#          ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), 
#          ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RO', 'Romania'), 
#          ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('VC', 'Saint Vincent and the Grenadines'), 
#          ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), 
#          ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SK', 'Slovakia'), 
#          ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('ES', 'Spain'), 
#          ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SZ', 'Swaziland'), ('SE', 'Sweden'), 
#          ('CH', 'Switzerland'), ('SY', 'Syrian Arab Republic'), ('TW', 'Taiwan, Province of China'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania, United Republic of'), 
#          ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), 
#          ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), 
#          ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'), ('United States', 'United States'), ('UY', 'Uruguay'), 
#          ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela, Bolivarian Republic of'), ('VN', 'Viet Nam'), ('YE', 'Yemen'), 
#          ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')
#         ]

# def country_choices():
#     return country_list

#     ]



