"""The API for the front-facing website."""

from flask import Blueprint, render_template

blueprint = Blueprint("website", __name__)


@blueprint.route("/")
def landing_page():
    """Serves the landing page."""
    return render_template("landingPage.html")
