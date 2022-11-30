import os

basedir = os.path.abspath(os.path.dirname(__file__))

# creating a configuration class
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') 

BASE_URI = os.environ.get('BASE_URI') 
SAFEPAY_URI = os.environ.get('SAFEPAY_URI') 
API_KEY = os.environ.get('API_KEY') 
#MONGO_URI = os.environ.get('MONGO_URI') 
USSD_username = os.environ.get('USSD_username') or "sandbox"
USSD_api_key = os.environ.get('USSD_api_key') or "0cbda1984b50fae5e1a89ef6586906c28983e2fb64a65e020d0d7c25887394cd"