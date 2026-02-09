from flask import Flask
from flask_smorest import Api, Blueprint
from flask.views import MethodView
from marshmallow import Schema, fields

app = Flask(__name__)

app.config["API_TITLE"] = "Student API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/api"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    dept = fields.Str(required=True)

blp = Blueprint(
    "students",
    __name__,
    description="Student CRUD operations"
)

students = []

@blp.route("/students")
class StudentList(MethodView):

    @blp.response(200, StudentSchema(many=True))
    def get(self):
        return students

    @blp.arguments(StudentSchema)
    @blp.response(201, StudentSchema)
    def post(self, student_data):
        student_data["id"] = len(students) + 1
        students.append(student_data)
        return student_data


@blp.route("/students/<int:student_id>")
class StudentResource(MethodView):

    @blp.arguments(StudentSchema)
    @blp.response(200, StudentSchema)
    def put(self, student_data, student_id):
        for student in students:
            if student["id"] == student_id:
                student.update(student_data)
                student["id"] = student_id
                return student
        return {"message": "Student not found"}, 404

    @blp.response(200)
    def delete(self, student_id):
        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                return {"message": "Student deleted successfully"}
        return {"message": "Student not found"}, 404


api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(debug=True)
