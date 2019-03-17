# RocketCo API

## What is this
A simple FLASK based api that uses the Flask-restful framework. This API pulls weather data from OpenWeatherMap to calculate the best launch windows for a rocket launch in the next 5 days. 

## Requirements
- Python >= 3.6

## How To Use This
- Go to https://openweathermap.org/ and sign up for an API key
- Install the libraries from requirements.txt with `pip install -r requirements.txt`
- Run `API_KEY=<API KEY from OpenWeatherMap> python manage.py run`
- Access `http://127.0.0.1:5000/` to view Swagger UI

## How to run dockerised app
- Run `docker build .`
- Run `docker run -e API_KEY=<API KEY from OpenWeatherMap> -p80:8000 <docker image id>`
- Access `localhost` to view Swagger UI

Note that config can be mounted at /app/app/main/resources/properties.yaml to allow for env specific config
