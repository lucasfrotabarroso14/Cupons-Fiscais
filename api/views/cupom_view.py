import json
import base64
from flask import make_response, jsonify, request
from flask_restx import Resource
from api.services import cupom_service
from datetime import datetime
from ..utils.Serialize import Serialize


class CuponsList(Resource):
    def get(self):
        data, status = cupom_service.get_all()

        if status:
            response_data = {
                "statusCode": 200,
                "status": True,
                "message": "Sucesso",
                "result": data
            }
            response = make_response(json.dumps(response_data, default=Serialize.serialize), 200)
            response.headers["Content-Type"] = "application/json"
            return response

        else:
            response_data = {
                "statusCode": 404,
                "status": False,
                "message": "Erro",
                "result": data
            }
            response = make_response(json.dumps(response_data), 404)
            response.headers['Content-Type'] = 'application/json'
            return response

    def post(self):
        data = request.get_json()
        bandeira_cartao = data.get('bandeira_do_cartao')
        imagem = data.get('imagem',None)
        forma_de_pagamento = data.get('forma_de_pagamento')

        if not bandeira_cartao or not forma_de_pagamento:
            response_data = {
                "statusCode": 404,
                "status": False,
                "message": "Campos obrigatórios estão faltando na solicitação.",
                "result": data
            }
            response = make_response(json.dumps(response_data), 404)
            response.headers['Content-Type'] = 'application/json'
            return response


        cupom_obj = {
            'bandeira_do_cartao':bandeira_cartao,
            'imagem':imagem,
            'forma_de_pagamento': forma_de_pagamento,
            'codigo_pedido_interno': 'CXA178243HJ',
            'status':'A',
            'nsu':'20105952',
            'autorizacao':'00000000041010',
            'codigo_filial': '02',
            'codigo_gerente':'999055',
            'codigo_vendedor':'023456',
            'data_hora_upload': datetime.today(),
            'data_hora_aceite': datetime.today()

        }
        res, status = cupom_service.registrar_cupom(cupom_obj)
        if status:
            response_data = {
                "statusCode": 200,
                "status": True,
                "message": "Sucesso",
                "result": res
            }
            response = make_response(json.dumps(response_data, default=Serialize.serialize), 200)
            response.headers["Content-Type"] = "application/json"
            return response

class CuponsDetails(Resource):
    def delete(self, id):
        data, status = cupom_service.deletar_cupom(id)
        if status:
            response_data = {
                "statusCode": 200,
                "status": True,
                "message": "Sucesso",
                "result": data
            }
            response = make_response(json.dumps(response_data, default=Serialize.serialize), 200)
            response.headers["Content-Type"] = "application/json"
            return response

        else:
            response_data = {
                "statusCode": 404,
                "status": False,
                "message": "Sucesso",
                "result": data
            }
            response = make_response(json.dumps(response_data), 404)
            response.headers['Content-Type'] = 'application/json'
            return response

    def get(self,id):
        data, status = cupom_service.get_by_id(id)
        if status:
            response_data = {
                "statusCode": 200,
                "status": True,
                "message": "Sucesso",
                "result": data
            }
            response = make_response(json.dumps(response_data, default=Serialize.serialize), 200)
            response.headers["Content-Type"] = "application/json"
            return response

        else:
            response_data = {
                "statusCode": 404,
                "status": False,
                "message": "Sucesso",
                "result": data
            }
            response = make_response(json.dumps(response_data), 404)
            response.headers['Content-Type'] = 'application/json'
            return response

    def put(self,id):
        data = request.get_json()
        bandeira_cartao = data.get('bandeira_do_cartao')
        imagem = data.get('imagem', None)
        forma_de_pagamento = data.get('forma_de_pagamento')
        if not bandeira_cartao or not forma_de_pagamento:
            response_data = {
                "statusCode": 404,
                "status": False,
                "message": "Campos obrigatórios estão faltando na solicitação.",
                "result": data
            }
            response = make_response(json.dumps(response_data), 404)
            response.headers['Content-Type'] = 'application/json'
            return response

        cupom_obj = {
            'bandeira_do_cartao': bandeira_cartao,
            'imagem': imagem,
            'forma_de_pagamento': forma_de_pagamento,
            'codigo_pedido_interno': 'CXA178243HJ',
            'status': 'A',
            'nsu': '20105952',
            'autorizacao': '00000000041010',
            'codigo_filial': '02',
            'codigo_gerente': '999055',
            'codigo_vendedor': '023456',
            'data_hora_upload': datetime.today(),
            'data_hora_aceite': datetime.today()

        }

        data, status =cupom_service.update(id,cupom_obj)
        if status:
            response_data = {
                "statusCode": 200,
                "status": True,
                "message": "Sucesso",
                "result": data
            }
            response = make_response(json.dumps(response_data, default=Serialize.serialize), 200)
            response.headers["Content-Type"] = "application/json"
            return response

        else:
            response_data = {
                "statusCode": 404,
                "status": False,
                "message": "Sucesso",
                "result": data
            }
            response = make_response(json.dumps(response_data), 404)
            response.headers['Content-Type'] = 'application/json'
            return response








class CuponsSemFotoList(Resource):
    def get(self):
        data, status = cupom_service.get_cupom_sem_foto()
        if status:
            response_data = {
                "statusCode": 200,
                "status": True,
                "message": "Sucesso",
                "result": data
            }
            response = make_response(json.dumps(response_data, default=Serialize.serialize), 200)
            response.headers["Content-Type"] = "application/json"
            return response

        else:
            response_data = {
                "statusCode": 404,
                "status": False,
                "message": "Sucesso",
                "result": data
            }
            response = make_response(json.dumps(response_data), 404)
            response.headers['Content-Type'] = 'application/json'
            return response

