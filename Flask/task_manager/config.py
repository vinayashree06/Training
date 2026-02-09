class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Vinaya!123shree@localhost:3306/task_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "PASTE_YOUR_GENERATED_SECRET_KEY"

    API_TITLE = "Task Management API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
