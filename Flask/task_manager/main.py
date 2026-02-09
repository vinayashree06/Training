import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from flask_smorest import Api
from config import Config
from extensions import db, jwt, migrate
from api.auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)

db.init_app(app)
jwt.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(auth_bp)

@app.route("/")
def home():
    return {"message": "Task Management API Running"}

if __name__ == "__main__":
    app.run(debug=True)
