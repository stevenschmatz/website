import os
from pymongo import MongoClient

# Open up MongoDB connection
MONGO_URL = os.environ.get('MONGOLAB_URI')
client = MongoClient(MONGO_URL)

# Specify the database
db = client.heroku_lk6xm4m6
