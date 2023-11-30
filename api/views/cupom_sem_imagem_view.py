import json

from flask import make_response
from flask_restx import Resource,Namespace
from api.services import cupons_service
from ..services.cupons_sem_imagem_service import get_cupom_sem_foto

from ..utils.Serialize import Serialize



cupons_sem_imagem_swagger = Namespace('cupons/sem_imagem', description='Endpoints para cupons sem imagens')

@cupons_sem_imagem_swagger.route('/')
class CuponsSemFotoList(Resource):
    def get(self):
        data, status = get_cupom_sem_foto()
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

