from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from flask_jwt_extended import JWTManager
import secrets

from api.services import cupom_service
from api.views.cupom_view import CuponsList, CuponsSemFotoList, CuponsDetails
from api.views.login import LoginList
from PIL import Image
import io
app = Flask(__name__)

# Dados de conexão
api = Api(app)

api.add_resource(CuponsList, "/cupons")
api.add_resource(CuponsDetails,"/cupons/<int:id>")
api.add_resource(CuponsSemFotoList, "/cupons/sem-imagem")
api.add_resource(LoginList,"/login")


CORS(app, resources={r"/*": {"origins": "*"}})
app.config['JWT_SECRET_KEY'] = secrets.token_hex(32)
app.config.from_object('config')

jwt = JWTManager(app)

# def teste_blob(imagem):


# cupom_obj = cupom_service.get_by_id(7)
# primeiro_cupom = cupom_obj[0]  # Acessa o primeiro elemento da lista
# imagem_teste = primeiro_cupom['imagem']
# teste_blob(imagem_teste)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port="3036", debug=True)


