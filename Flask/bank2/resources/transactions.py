from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import Account, Transaction
from schemas import TransactionSchema

blp = Blueprint("transactions", __name__, description="Transaction APIs")

@blp.route("/transactions")
class TransactionList(MethodView):

    @blp.arguments(TransactionSchema)
    @blp.response(201, TransactionSchema)
    def post(self, data):
        account = Account.query.get(data["account_number"])
        if not account:
            return {"message": "Account not found"}, 404

        if data["type"] == "Withdraw" and account.balance < data["amount"]:
            return {"message": "Insufficient balance"}, 400

        if data["type"] == "Deposit":
            account.balance += data["amount"]
        else:
            account.balance -= data["amount"]

        transaction = Transaction(**data)
        db.session.add(transaction)
        db.session.commit()
        return transaction
