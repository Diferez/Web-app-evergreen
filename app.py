from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__, template_folder='templates')

variable_list =['Estres Hidrico','Nitrogeno foliar', 'Indice de cosecha', 'Dencidad volumetrica radial']

@app.route('/listarSensores',methods =['GET'])
def listarSensores():
    sensores_list =  requests.get('https://api-evergreen-846.azurewebsites.net/tipoSensores').json()
    return render_template('listarSensores.html', sensores = sensores_list)

@app.route('/crearSensor',methods=['GET'])
def crearSensor():
    return render_template('crearSensor.html', variables = variable_list)

@app.route('/guardarSensor', methods = ['POST'])
def guardarSensor():
    sensor = dict(request.values)
    sensor['prioridad'] = int(sensor['prioridad'])
    requests.post('https://api-evergreen-846.azurewebsites.net/tipoSensores', json = sensor)
    return(listarSensores())

