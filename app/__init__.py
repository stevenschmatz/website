import os
import yaml
from pymongo import MongoClient

with open('config.yaml', 'r') as f:
    config = yaml.load(f)

# Open up MongoDB connection
MONGO_URL = os.environ.get('MONGOLAB_URI') or config['mongolab']['uri']
client = MongoClient(MONGO_URL)

# Specify the database
db = client.heroku_p04lqbk2
