from flask import request, current_app
from flask_restplus import Resource, reqparse

from ..service.location_service import get_locations, get_location_by_name

from ..dto.launch_window_dto import LaunchWindowDto

import requests

api = LaunchWindowDto.api
_launch_window = LaunchWindowDto.launch_window

parser = reqparse.RequestParser()
parser.add_argument('location', required=False, location='args')

@api.route('/')
class LaunchWindowList(Resource):
    @api.doc('list_of_best_launch_windows')
    @api.expect(parser, validate=False)
    @api.marshal_list_with(_launch_window, envelope='launchWindows')
    def get(self):
        args = parser.parse_args()
        if args["location"]:
            location = get_location_by_name(args["location"])
            if (not location):
                # No matching location, so no launch windows
                return []
            all_locations = [location]
        else:
            all_locations = get_locations()

        scored_windows = []
        for location in all_locations:
            launch_windows = get_5_day_3_hour_forecast(location["id"], 
                                                       current_app.config["OPEN_WEATHER"],
                                                       current_app.config["API_KEY"])
            valid_windows = [x for x in launch_windows if is_valid_window(x, location)]
            for window in valid_windows:
                window.update({
                    "score": score_launch_window(window, current_app.config["LAUNCH_WINDOWS"]),
                    "location": location["name"]
                })
            scored_windows += valid_windows
        scored_windows.sort(key=(lambda x: x["score"]))
        return scored_windows[:current_app.config["LAUNCH_WINDOWS"]["RETURN_SIZE"]]


def score_launch_window(launch_window, config):
    return abs(config["DESIRED_TEMP"]-launch_window["temperature"]) \
        + launch_window["wind_speed"] \
        + abs(config["DESIRED_DEG"] - launch_window["wind_direction"]) * config["DEG_MODIFIER"]

def is_valid_window(launch_window, location):
    return (launch_window["cloud"] < location["cloud_max"] and launch_window["wind_speed"] < location["wind_max"])

def get_5_day_3_hour_forecast(location_id, config, api_key):
    uri = config["HOST"] + config["BASE_PATH"] + config["FORECAST_PATH"]
    r = requests.get(uri, params={
                        "id": location_id,
                        "units": config["UNITS"],
                        "APPID": api_key
                    })
    return [{
        "datetime": x["dt"],
        "cloud": x["clouds"]["all"],
        "wind_speed": x["wind"]["speed"],
        "temperature": x["main"]["temp"],
        "wind_direction": x["wind"]["deg"]
    } for x in r.json()["list"]]
    
