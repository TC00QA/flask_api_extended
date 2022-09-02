from sub_programs import app
from flask import Response
import random

@app.route('/colour', methods = ['GET'])
def colour():
    colours = ["Red","Green","Blue"]
    return Response(random.choice(colours), mimetype='text/plain')

