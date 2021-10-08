from flask import Flask,request,jsonify 
from sqlalchemy import create_engine   
from flask_cors import CORS

app = Flask(__name__)
engine = create_engine('sqlite:///banco.db',echo=True)
CORS(app)
from api.admin import rotas