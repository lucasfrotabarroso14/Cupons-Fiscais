import json
import base64
from flask import make_response, jsonify
from flask_restx import Resource
from api.services import cupom_service
from datetime import datetime

class Serialize():

    def serialize_datetime(obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        raise TypeError("Object of type {} is not JSON serializable".format(type(obj).__name__))

    def serialize_memoryview(obj):
        if isinstance(obj, memoryview):
            return base64.b64encode(obj).decode('utf-8')
        raise TypeError("Object of type {} is not JSON serializable".format(type(obj).__name__))

    def serialize(obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, memoryview):
            return Serialize.serialize_memoryview(obj)
        else:
            return obj