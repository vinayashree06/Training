from flask import Flask
from flask_migrate import Migrate
from Database.database import db
from API.login import auth_bp

app = Flask(__name__)

# DB config
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Vinaya!123shree@localhost:3306/jaya"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init db & migrate
db.init_app(app)
migrate = Migrate(app, db)

# register blueprint
app.register_blueprint(auth_bp)

@app.route("/")
def home():
    return {"message": "restAPI app running"}

if __name__ == "__main__":
    app.run(debug=True)
