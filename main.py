import os
from flask import Flask, render_template, request, redirect
from app import db
from api.pomodoro import bp as pomodoro_bp

collection = db.shoutouts

app = Flask(__name__)


def register_all_blueprints():
    app.register_blueprint(pomodoro_bp)


@app.route("/", methods=['GET'])
def index():
    return render_template('landingPage.html')


@app.route("/shouts", methods=['GET'])
def show_shouts():
    shouts = collection.find()
    return render_template('index.html', shouts=shouts)


@app.route("/post", methods=['POST'])
def post():
    shout = {
        "name": request.form['name'],
        "message": request.form['message']
    }
    collection.insert(shout)
    return redirect('/')


if __name__ == "__main__":
    register_all_blueprints()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
