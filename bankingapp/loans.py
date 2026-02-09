from flask import request

def register_loan_routes(app):

    @app.route("/loan_eligibility", methods=['POST'])
    def loan_eligibility():
        data = request.json

        salary = data.get('salary')

        if salary is None:
            return {"error": "Salary is required"}, 400

        if salary > 30000:
            return {
                "salary": salary,
                "eligible": True,
                "loan_amount": 50000
            }, 200
        else:
            return {
                "salary": salary,
                "eligible": False,
                "loan_amount": 0
            }, 200
