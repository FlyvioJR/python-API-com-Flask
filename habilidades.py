from flask_restful import Resource

lista_habilidades = ['Python', "Assembly", "C#", 'Flask']

class Habilidade(Resource):
    def get(self):
        return lista_habilidades

