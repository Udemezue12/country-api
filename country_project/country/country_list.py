from flask import Blueprint, Response, json
from flask_login import current_user, login_required
from country_project.states.state_list import states as nation
from country_project.secure import require_api_key


country = Blueprint('country', __name__)
my_state = Blueprint('my_state', __name__)


@my_state.route('/states/states/', methods=['GET'])
# @login_required
# @require_api_key
def states():
    return Response(json.dumps(nation), mimetype='application/json')


@country.route('/country/countries', methods=['GET'])
# @login_required
# @require_api_key

def country_choices():
    return [



        ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria',
                                                                 'Algeria'), ('American Samoa', 'American Samoa'), ('Andorra', 'Andorra'),
        ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antarctica', 'Antarctica'), (
            'Antigua and Barbuda', 'Antigua and Barbuda'), ('Argentina', 'Argentina'),
        ('Armenia', 'Armenia'), ('Aruba', 'Aruba'), ('Australia',
                                                     'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'),
        ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh',
                                                         'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'),
        ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin Repbulic',
                                                       'Benin Repbulic'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'),
        ('Bolivia', 'Bolivia'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Botswana',
                                                                                       'Botswana'), ('Brazil', 'Brazil'), ('Brunei Darussalam', 'Brunei Darussalam'),
        ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi',
                                                                     'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'),
        ('Canada', 'Canada'), ('Cape Verde', 'Cape Verde'), ('Cayman Islands', 'Cayman Islands'), (
            'Central African Republic', 'Central African Republic'), ('Chad Republic', 'Chad Republic'),
        ('Chile', 'Chile'), ('China', 'China'), ('Colombia',
                                                 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'),
        ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'), ('Cook Islands',
                                                                                           'Cook Islands'), ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'),
        ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Denmark',
                                                                     'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'),
        ('Dominican Republic', 'Dominican Republic'), ('Ecuador', 'Ecuador'), ('Egypt',
                                                                               'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guniea', 'Equatorial Guinea'),
        ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethopia',
                                                         'Ethiopia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'),
        ('France', 'France'), ('Gabon', 'Gabon'), ('The Gambia',
                                                   'The Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'),
        ('Ghana', 'Ghana'), ('Greece', 'Greece'), ('Grenada',
                                                   'Grenada'), ('Guam', 'Guam'), ('Guatemala', 'Guatemala'),
        ('Guniea', 'Guinea'), ('Guniea-Bissau', 'Guinea-Bissau'), ('Guyana',
                                                                   'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'),
        ('Hong Kong', 'Hong Kong'), ('Hungary', 'Hungary'), ('Iceland',
                                                             'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'),
        ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland',
                                                                  'Ireland'), ('Israel', 'Israel'), ('Italy', 'Italy'),
        ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan',
                                                     'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'),
        ('Kiribati', 'Kiribati'), ('North Korea', "North Korea"), (
            'South Korea', 'South Korea'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'),
        ('Lao People Republic', "Lao People Republic"), ('Latvia', 'Latvia'), ('Lebanon',
                                                                                'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'),
        ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania',
                                                                 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Macao', 'Macao'),
        ('Macedonia', 'Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi',
                                                                   'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'),
        ('Mali', 'Mali'), ('Malta', 'Malta'), ('Marshall Islands',
                                               'Marshall Islands'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'),
        ('Mexico', 'Mexico'), ('Micronesia, Federated States of', 'Micronesia, Federated States of'), (
            'Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'),
        ('Montenegro', 'Montenegro'), ('Montserrat', 'Montserrat'), ('Morocco',
                                                                      'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'),
        ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal',
                                                     'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'New Zealand'),
        ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria',
                                                         'Nigeria'), ('Niue', 'Niue'), ('Norfolk Island', 'Norfolk Island'),
        ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Norway',
                                                                   'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palau', 'Palau'),
        ('Panama', 'Panama'), ('Papua New Guniea', 'Papua New Guinea'), ('Paraguay',
                                                                          'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'),
        ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto Rico',
                                                         'Puerto Rico'), ('Qatar', 'Qatar'), ('Romania', 'Romania'),
        ('Russia', 'Russian'), ('Rawanda', 'Rwanda'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), (
            'Saint Lucia', 'Saint Lucia'), ('Saint Vincent and the Grenadine', 'Saint Vincent and the Grenadines'),
        ('Samoa', 'Samoa'), ('San Marino', 'San Marino'), ('Sao Tome and Principe',
                                                           'Sao Tome and Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'),
        ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone',
                                                             'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'),
        ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia',
                                                                           'Somalia'), ('South Africa', 'South Africa'), ('Spain', 'Spain'),
        ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('South Sudan', 'South Sudan'), (
            'Suriname', 'Suriname'), ('Swaziland', 'Swaziland'), ('Sweden', 'Sweden'),
        ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Taiwan',
                                                             'Taiwan'), ('TJ', 'Tajikistan'), ('Tanzania', 'Tanzania'),
        ('Thailand', 'Thailand'), ('Timor-Leste', 'Timor-Leste'), ('Togo',
                                                                   'Togo'), ('Togo', 'Tonga'), ('Trinidad and Tobago', 'Trinidad and Tobago'),
        ('TN', 'Tunisia'), ('Turkiye(Formerly Turkey)', 'Turkiye(Turkey)'), ('Turkmenistan',
                                                                              'Turkmenistan'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'),
        ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('GB',
                                                                                    'United Kingdom'), ('United States', 'United States'), ('Uruguay', 'Uruguay'),
        ('Uzbekistan', 'Uzbekistan'), ('Vanuatu', 'Vanuatu'), ('Venezuela',
                                                               'Venezuela'), ('Vietnam', 'Vietnam'), ('Yemen', 'Yemen'),
        ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')
    ]
