import os
from flask import Flask, render_template
from app import db
from api.pomodoro import bp as pomodoro_bp
from app.weather import get_weather_description

collection = db.shoutouts

app = Flask(__name__)


def register_all_blueprints():
    app.register_blueprint(pomodoro_bp)


@app.route("/")
def index():
    return render_template('landingPage.html')


@app.route("/weather")
def weather():
    return get_weather_description()


if __name__ == "__main__":
    register_all_blueprints()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
