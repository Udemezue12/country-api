from flask import jsonify, Blueprint, Response
from flask_login import login_required
from country_project.secure import require_api_key
import json
from country_project.country.country_list import country_choices
from country_project.states.state_list import states



state = Blueprint('state', __name__)


@state.route('/state/countries', methods=['GET'])
# @login_required
# @require_api_key
def get_countries():
    countries_list = country_choices() 
    return Response(json.dumps(countries_list), mimetype='application/json')
#     states_list = states.get(country, [])
#     return jsonify(states_list)


@state.route('/state/get_states/<country>', methods=['GET'])
# @login_required
# @require_api_key
def get_states(country):
    states_list = states.get(country, [])
    return Response(json.dumps(states_list), mimetype='application/json')
