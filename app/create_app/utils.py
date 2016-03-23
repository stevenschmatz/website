"""Performs setup for the Flask web app."""

import os
from app.ava import launch_bot


def register_all_blueprints(flask_app):
    """Registers all blueprints across the web app."""

    from app.pomodoro import blueprint as pomodoro_bp
    from app.weather import blueprint as weather_bp
    from app.website import blueprint as website_bp

    flask_app.register_blueprint(pomodoro_bp)
    flask_app.register_blueprint(weather_bp)
    flask_app.register_blueprint(website_bp)


def init_flask(flask_app):
    """Initializes the web app object."""
    port = int(os.environ.get("PORT", 5000))
    if os.environ.get("DEBUG") is not None:
        debug = False
    else:
        debug = True
    flask_app.run(host='0.0.0.0', port=port, debug=debug)


def init_web_app(flask_app):
    register_all_blueprints(flask_app)
    launch_bot()
    init_flask(flask_app)
