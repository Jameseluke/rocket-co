"""
Simple service to return information regarding Locations

Replace with external data source (DB)
"""
LOCATIONS = [
     {
        "id": "7839805",
        "name": "Melbourne",
        "cloud_max": 50,
        "wind_max": 20
    },
    {
        "id": "2073124",
        "name": "Darwin",
        "cloud_max": 40,
        "wind_max": 15
    },
    {
        "id": "2163355",
        "name": "Hobart",
        "cloud_max": 60,
        "wind_max": 10
    },
    {
        "id": "2063523",
        "name": "Perth",
        "cloud_max": 30,
        "wind_max": 5
    }
]


# no support for country code
def get_location_id(location_name):
    '''
    Returns the location Id for a given name
    Returns None if not found
    '''
    return next( (x["id"] for x in LOCATIONS if x["name"]==location_name), None)

def get_location_by_name(location_name):
    '''
    Return a location for a given name
    Return None if None found
    '''
    return next( (x for x in LOCATIONS if x["name"]==location_name), None)

def get_location_by_id(id):
    '''
    Return a location for a given ID
    Return None if None found
    '''
    return next((x for x in LOCATIONS if x["id"]==Id), None)

def get_locations():
    return LOCATIONS
