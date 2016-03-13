import os
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
import datetime

# Open up MongoDB connection
MONGO_URL = os.environ.get('MONGOLAB_URI')
client = MongoClient(MONGO_URL)

# Specify the database
db = client.heroku_lk6xm4m6
collection = db.shoutouts

app = Flask(__name__)


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


@app.route("/api/pomodoro", methods=['POST'])
def log_pomodoro():
    # Return forbidden error if token is incorrect
    if os.environ.get('SLACK_TOKEN') != request.form['token']:
        return redirect('/'), 403

    # Insert the pomodoro
    pomodoro = {
        "text": request.form['text'],
        "time": datetime.datetime.utcnow()
    }
    db.pomodoro.insert(pomodoro)

    return "Pomodoro logged successfully!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
