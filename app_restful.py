from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidade
import json

app = Flask(__name__)
api = Api(app)


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


class Dev(Resource):
    def get(self, id):
        try:
            response = devs[id]
        except IndexError:
            mensagem = f'Densenvolvedor de ID {id} nao existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = f'Erro desconhecido'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def post(self, id):
        dados = json.loads(request.data)
        devs[id] = dados
        return dados

    def delete(self, id):
        devs.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}


class Devs(Resource):
    def get(self):
        return devs

    def post(self):
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        return devs[posicao]


api.add_resource(Dev, '/dev/<int:id>/')
api.add_resource(Devs, '/dev/')
api.add_resource(Habilidade, '/habilidades/')


if __name__ == '__main__':
    app.run(debug=True)
