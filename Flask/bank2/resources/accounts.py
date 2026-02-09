from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import Account, Customer
from schemas import AccountSchema

blp = Blueprint("accounts", __name__, description="Account APIs")

@blp.route("/accounts")
class AccountList(MethodView):

    @blp.arguments(AccountSchema)
    @blp.response(201, AccountSchema)
    def post(self, data):
        if not Customer.query.get(data["customer_id"]):
            return {"message": "Customer not found"}, 404

        account = Account(**data)
        db.session.add(account)
        db.session.commit()
        return account
