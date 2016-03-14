import os
import yaml
from pymongo import MongoClient

# Open up MongoDB connection
MONGO_URL = os.environ.get('MONGOLAB_URI')
client = MongoClient(MONGO_URL)

with open('config.yaml', 'r') as f:
    config = yaml.load(f)

# Specify the database
db = client.heroku_lk6xm4m6
