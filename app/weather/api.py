from utils import get_weather_description
from flask import Blueprint

blueprint = Blueprint('weather', __name__, url_prefix='/api')


@blueprint.route("/weather")
def weather():
    """Returns a description of the weather for the day."""
    return get_weather_description()
