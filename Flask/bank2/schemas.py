from marshmallow import Schema, fields

class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)

class AccountSchema(Schema):
    account_number = fields.Int(required=True)
    customer_id = fields.Int(required=True)
    account_type = fields.Str(required=True)
    balance = fields.Float(required=True)

class TransactionSchema(Schema):
    id = fields.Int(dump_only=True)
    account_number = fields.Int(required=True)
    type = fields.Str(required=True)
    amount = fields.Float(required=True)
    date = fields.Str(required=True)
