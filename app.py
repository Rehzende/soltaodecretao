from crypt import methods
from email import message
from flask import Flask, make_response, jsonify, render_template, request
import json, requests, datetime, random
app = Flask(__name__)
@app.route('/api')
def hello_world():
    if request.method == 'GET':
        response = make_response(jsonify(gera_motivo()),200,)
        return response

@app.route("/", methods=['GET'])
def index():
    if request.method == 'GET':
        res = requests.get(request.url_root + '/api')
        data = json.loads(res.text)
    return render_template("index.html", message=data['mensagem'])


def gera_motivo():
    day_of_week = datetime.datetime.today().isoweekday()
    currentDateAndTime = datetime.datetime.now()
    f = open('motivos.json')
    data = json.load(f)
    day_valid = [5, 6, 7]
    if  day_of_week in day_valid:
        if day_of_week == 5:
            print(day_of_week)
            if currentDateAndTime.hour < 18:
                motivo = random.choice(data['dias_liberados']['resposta_muito_cedo'])
                return  { "decreto_liberado": "true",  "mensagem": motivo, "gif": "https://tenor.com/23323" }
            else:
                motivo = random.choice(data['dias_liberados']['resposta_padrao'])
                return  { "decreto_liberado": "true",  "mensagem": motivo, "gif": "https://tenor.com/23323" }
        else:
            motivo = random.choice(data['dias_liberados']['resposta_padrao'])
            return  { "decreto_liberado": "true",  "mensagem": motivo, "gif": "https://tenor.com/23323" }
    else:
        motivo = random.choice(data['dias_nao_liberados']['resposta_padrao'])
        return  { "decreto_liberado": "false",  "mensagem": motivo, "gif": "https://tenor.com/23323" }

