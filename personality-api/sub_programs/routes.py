from sub_programs import app
from flask import Response
import random

@app.route('/personality', methods = ['GET'])
def personality():
    emotions = {"Angry":random.randint(0,100), "Intelligent":random.randint(0,100), "Egotistical":random.randint(0,100)}
    return Response(str(emotions), mimetype='text/plain')

