from flask import Flask,jsonify,request,json
from flask_sqlalchemy import SQLAlchemy
import json
import calcinss as inss
import calcirrf as irrf

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    def __str__(self):
 
        return f'{self.content}'


def todo_serializer(todo):
    return {
        'id': todo.id,
        'content': todo.content
    }






@app.route('/api/create', methods=["POST"])
def create():
    request_data = json.loads(request.data)
    salario = float(request_data['content'])
    deep = float(request_data['teste'])
    
    totaldescontado = inss.calc(salario) + irrf.irrf(inss.calc(salario),salario,deep)
    salarioliquido =  salario-inss.calc(salario) - irrf.irrf(inss.calc(salario),salario,deep)
    valorinss = inss.calc(salario)
    valorirrf = irrf.irrf(inss.calc(salario),salario,deep)

    print("O salario liquido é igual a","{:.2f}".format(salarioliquido))
    print("O valor descontado pelo INSS foi de","{:.2f}".format(valorinss))
    print("O valor descontado pelo IRRF foi de","{:.2f}".format(valorirrf))
    print("Ao total foram descontados","{:.2f}".format(totaldescontado))


    return jsonify( {

        'salario': salarioliquido,
        'inss': valorinss
    })
        
   



@app.route('/api', methods=['GET'])
def index():
    return jsonify([*map(todo_serializer,Todo.query.all())])

if __name__ == '__main__':
    app.run(debug=True)