from sub_programs import app
from flask import Response, request

colours_dict = {"Red":"Angry","Green":"Egotistical","Blue":"Intelligent"}

@app.route('/back-end', methods = ['POST'])
def back_end():
    dict_in = request.get_json()
    colour = dict_in['Colour']

    dict_in.pop('Colour')

    for key, value in dict_in.items():
        value = int(value)
        if key == colour:
            value += 10
            dict_in[key] = value
            break

    main_trait = max(dict_in, key=dict_in.get)
    score = int(dict_in[main_trait])

    if score >= 100:
        score = 100

    output = f"You have a {colour} core, with a {main_trait} personality, scoring {score}/100 {dict_in}"

    return Response(str(output), mimetype='text/plain')

