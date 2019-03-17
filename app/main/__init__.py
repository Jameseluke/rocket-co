from flask import Flask, Blueprint
from yaml import safe_load
import os, sys
from .controller.launch_window_controller import api as launch_window_ns
from flask_restplus import Api

def create_app():
    app = Flask(__name__)
    with open('./app/main/resources/properties.yaml', 'r') as config_file:
        app.config.update(safe_load(config_file))
        if 'API_KEY' not in os.environ:
            app.logger.error("Open Weather API Key not found")
            sys.exit(1)

        app.config["API_KEY"] = os.environ.get("API_KEY")

    api = Api(
            title='RocketCo',
            version='1.0',
            description='API for Location, Weather and Launch Window Services'
            )

    api.add_namespace(launch_window_ns, path='/launch_window')
    api.init_app(app)
    return app
