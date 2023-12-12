import json

from flask import make_response, jsonify, request
from flask_restx import Resource,Namespace
from datetime import datetime

from ..services.cupons_ocr_service import get_cupons_pendentes_ocr
from ..utils.Serialize import Serialize

cupons_ocr_swagger = Namespace('cupons/ocr/pendentes', description='Endpoints para o serviço de OCR')

@cupons_ocr_swagger.route('/')
class CuponsPendentesOCR(Resource):
    def get(self):
        data, status = get_cupons_pendentes_ocr()

        if status:
            response_data = {
                "status_code": 200,
                "status": True,
                "message": "Sucesso",
                "result": data
            }
            response = make_response(json.dumps(response_data, default=Serialize.serialize), 200)
            response.headers["Content-Type"] = "application/json"
            return response

        else:
            response_data = {
                "status_code": 404,
                "status": False,
                "message": "Erro",
                "result": data
            }
            response = make_response(json.dumps(response_data), 404)
            response.headers['Content-Type'] = 'application/json'
            return response

