# from country_project.models import User as USERS
# from flask import Response


# def check_auth(username, password):
#     """Check if a username/password combination is valid."""
#     user = USERS.get(username)
#     if user and user.password == password:
#         return user
#     return None

# def authenticate():
#     """Sends a 401 response that enables basic auth"""
#     return Response(
#         'Could not verify your access level for that URL.\n'
#         'You have to login with proper credentials', 401,
#         {'WWW-Authenticate': 'Basic realm="Login Required"'})