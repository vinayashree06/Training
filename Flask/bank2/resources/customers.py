from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import Customer
from schemas import CustomerSchema

blp = Blueprint("customers", __name__, description="Customer APIs")

@blp.route("/customers")
class CustomerList(MethodView):

    @blp.response(200, CustomerSchema(many=True))
    def get(self):
        return Customer.query.all()

    @blp.arguments(CustomerSchema)
    @blp.response(201, CustomerSchema)
    def post(self, data):
        customer = Customer(**data)
        db.session.add(customer)
        db.session.commit()
        return customer
