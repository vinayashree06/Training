from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"message": "Returning list of users"})

@app.route('/users', methods=['POST'])
def create_users():
    new_user = request.json
    return jsonify({
        "message": "User created",
        "user": new_user
    })

@app.route('/users/<int:id>',methods=['PUT'])
def update_user(id):
    updated_user=request.json
    return jsonify({
        "message":f"User with ID {id} updated",
        "updated_user":updated_user
    })

@app.route('/users/<int:id>',methods=['DELETE'])
def delete_user(id):
    return jsonify({
        "message":f"User with ID {id} deleted"
    })
if __name__ == '__main__':
    app.run(port=5000,debug=True)