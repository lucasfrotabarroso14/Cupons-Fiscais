from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from flask_jwt_extended import JWTManager
import secrets

from api.utils.celery_config import make_celery
from api.views.cupom_view import CuponsList, CuponsSemFotoList, CuponsDetails
from api.views.login import LoginList


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



app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)







if __name__ == '__main__':
    app.run(host="0.0.0.0", port="3036", debug=True)


