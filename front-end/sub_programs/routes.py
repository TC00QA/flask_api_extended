from sub_programs import app
from flask import request, render_template
import requests
import ast


@app.route('/', methods = ['GET'])
def home():
    random_colour = requests.get('http://colour-api:5000/colour')
    personality_table = requests.get('http://personality-api:5000/personality')


    handoff_dict = personality_table.text
    handoff_dict = ast.literal_eval(handoff_dict)
    handoff_dict['Colour'] = random_colour.text

    response = requests.post('http://back-end:5000/back-end', json = handoff_dict)

    return render_template('index.html', output=response.text)

