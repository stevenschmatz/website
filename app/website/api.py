"""The API for the front-facing website."""

from flask import Blueprint, render_template, redirect

blueprint = Blueprint("website", __name__)


@blueprint.route("/")
def landing_page():
    """Serves the landing page."""
    return render_template("landingPage.html")

@blueprint.route("/fb")
@blueprint.route("/facebook")
def facebook_redirect():
    """Redirects to Facebook."""
    return redirect("https://www.facebook.com/schmatzarella")
