from db import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

    accounts = db.relationship("Account", backref="customer", lazy=True)


class Account(db.Model):
    account_number = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    account_type = db.Column(db.String(20), nullable=False)
    balance = db.Column(db.Float, default=0)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(
        db.Integer, db.ForeignKey("account.account_number"), nullable=False
    )
    type = db.Column(db.String(10), nullable=False)  # Deposit / Withdraw
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(30), nullable=False)
