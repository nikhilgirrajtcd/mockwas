from flask import Flask, request, make_response
from flask_cors import CORS
from datetime import datetime
import re
from flask import jsonify
import numpy as np

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "API for Adaptive Applications by Team James!"


# Weird URI to prevent accidental 
@app.route("/user/register", methods=['POST'])
def register():
    return make_response({"userId": np.random.randint(1000)})