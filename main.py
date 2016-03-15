"""Web app for steven.party."""

from flask import Flask
from app.create_app import init_web_app

flask_app = Flask(__name__)

if __name__ == "__main__":
    init_web_app(flask_app)
