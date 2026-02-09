from flask import Flask
from flask_smorest import Api
from db import db

from resources.customers import blp as CustomerBlueprint
from resources.accounts import blp as AccountBlueprint
from resources.transactions import blp as TransactionBlueprint
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:Vinaya!123shree@localhost/bank_db"

)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["API_TITLE"] = "Bank Account Management API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/api"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

db.init_app(app)
api = Api(app)

api.register_blueprint(CustomerBlueprint)
api.register_blueprint(AccountBlueprint)
api.register_blueprint(TransactionBlueprint)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
