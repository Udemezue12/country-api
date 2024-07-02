from flask import Flask
from country_project import app
# from flask_sslify import SSLify
   

if __name__ == '__main__':
    # sslify = SSLify(app)

    # app.run(debug=True, ssl_context='adhoc', port=200)
    app.run(debug=True, port=100)
