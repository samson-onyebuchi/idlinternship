import os
from flask import Flask
from config import Config, MONGO_URI
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
CORS(app)


from app import error, q4