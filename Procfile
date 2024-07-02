web: waitress-serve  country_project.run:application

web: gunicorn country_project.wsgi:application --bind 0.0.0.0:$PORT