from flask import request

accounts = {}

VALID_ACCOUNT_TYPES = ["Savings", "FD", "Recurring"]

def register_account_routes(app):

    @app.route("/account_creation", methods=['POST', 'GET'])
    def account_creation():
        if request.method == 'GET':
            return accounts
        elif request.method == 'POST':
            data = request.json

            acc_no = data.get('account_no')   
            account_type = data.get('account_type')

           
            if account_type not in VALID_ACCOUNT_TYPES:
                return {"error": "Invalid account type"}, 400

            account_details = {
                "name": data.get('name'),
                "balance": data.get('balance'),
                "aadhaar": data.get('aadhaar'),
                "pan": data.get('pan'),
                "phone": data.get('phone'),
                "account_type": account_type
            }

            if account_type == "FD":
                account_details["amount"] = data.get('amount')
                account_details["duration"] = data.get('duration')

            elif account_type == "Recurring":
                account_details["monthly_amount"] = data.get('monthly_amount')
                account_details["duration"] = data.get('duration')

            accounts[acc_no] = account_details

            return {
                "message": "Account created successfully",
                "account_number": acc_no,
                "account": accounts[acc_no]
            }, 201
