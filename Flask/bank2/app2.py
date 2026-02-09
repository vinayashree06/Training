import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, request, jsonify
from db import db
from models import Customer, Account, Transaction

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:Vinaya!123shree@localhost/bank_db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/customers", methods=["GET", "POST"])
def customers():
    if request.method == "GET":
        customers = Customer.query.all()
        return jsonify([
            {"id": c.id, "name": c.name, "email": c.email, "phone": c.phone}
            for c in customers
        ])

    if request.method == "POST":
        data = request.json
        customer = Customer(
            name=data["name"],
            email=data["email"],
            phone=data["phone"]
        )
        db.session.add(customer)
        db.session.commit()
        return jsonify({"message": "Customer created", "id": customer.id}), 201

@app.route("/accounts", methods=["POST", "GET"])
def accounts():
    if request.method == "GET":
        accounts = Account.query.all()
        return jsonify([
            {
                "account_number": a.account_number,
                "customer_id": a.customer_id,
                "account_type": a.account_type,
                "balance": a.balance
            }
            for a in accounts
        ])

    if request.method == "POST":
        data = request.json

        customer = Customer.query.get(data["customer_id"])
        if not customer:
            return jsonify({"error": "Customer not found"}), 404

        account = Account(
            account_number=data["account_number"],
            customer_id=data["customer_id"],
            account_type=data["account_type"],
            balance=data["balance"]
        )
        db.session.add(account)
        db.session.commit()

        return jsonify({"message": "Account created"}), 201

@app.route("/transactions", methods=["POST"])
def transactions():
    data = request.json
    account = Account.query.get(data["account_number"])

    if not account:
        return jsonify({"error": "Account not found"}), 404

    if data["type"] == "Withdraw":
        if account.balance < data["amount"]:
            return jsonify({"error": "Insufficient balance"}), 400
        account.balance -= data["amount"]

    elif data["type"] == "Deposit":
        account.balance += data["amount"]

    transaction = Transaction(
        account_number=data["account_number"],
        type=data["type"],
        amount=data["amount"],
        date=data["date"]
    )

    db.session.add(transaction)
    db.session.commit()

    return jsonify({"message": "Transaction successful"}), 201


if __name__ == "__main__":
    app.run(debug=True)
