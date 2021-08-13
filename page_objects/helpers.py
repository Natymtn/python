import json


class Helpers:

    def obtener_parametro(parametro):
        with open('config/jsons/portalAnalistas.json') as portalAnalistasJson:
            parametros = json.load(portalAnalistasJson)
            return parametros[parametro]
