from flask import Flask, jsonify, request
import json

app = Flask(__name__)

devs = [
    {'id': '0',
     'nome': 'Flavio',
     'habilidade': ['python', 'C#']
     },
    {'id': '1',
     'nome': 'Junior',
     'habilidade': ['django', 'flask']
     }
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        dev = devs[id]
        return jsonify(dev)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro excluido'})


@app.route('/dev/', methods=['GET', 'POST'])
def lista_devs():
    if request.method == 'POST':
        dados = json.loads(request.data)
        devNovo_id = len(devs)
        dados['id'] = devNovo_id
        devs.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro inserido'})
    elif request.method == 'GET':
        return jsonify(devs)


if __name__ == '__main__':
    app.run(debug=True)
