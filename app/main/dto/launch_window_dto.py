from flask_restplus import Namespace, fields

class LaunchWindowDto:
    api = Namespace('launch window', description='launch window related operations')
    launch_window = api.model('launch_window', {
        'location': fields.String(required=True, description='location name'),
        'datetime': fields.String(required=True, description='time of launch period'),
        'score': fields.Integer(required=True, description='heuristic score for the window'),
})
