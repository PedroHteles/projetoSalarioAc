from flask import Flask,request,jsonify 
from sqlalchemy.sql import select
from api import app,engine
from api.admin.models import inss,irrf
from api.admin.calcinss import calc
from api.admin.calcirrf import calculaIrrf
import json

@app.route('/api/calculaSalario', methods=["POST"])
def create():
    request_data = json.loads(request.data)
    salario = float(request_data['salario'])
    deep = float(request_data['dependentes'])

    totaldescontado = calc(salario) + calculaIrrf(calc(salario),salario,deep)
    salarioliquido =  salario-calc(salario) - calculaIrrf(calc(salario),salario,deep)
    valorinss = calc(salario)
    valorirrf = calculaIrrf(calc(salario),salario,deep)

    print("O salario liquido é igual a","{:.2f}".format(salarioliquido))
    print("O valor descontado pelo INSS foi de","{:.2f}".format(valorinss))
    print("O valor descontado pelo IRRF foi de","{:.2f}".format(valorirrf))
    print("Ao total foram descontados","{:.2f}".format(totaldescontado))
    return  json.dumps({'salario': salarioliquido,'inss': valorinss}),200
        
   