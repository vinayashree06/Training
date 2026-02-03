from flask import Flask, jsonify, request
import base64

app = Flask(__name__)

products = []

@app.route("/register/product", methods=['POST'])
def register_product():
    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "No data provided"
        }), 400

    required_fields = [
        "Cat_ID",
        "Sub_ID",
        "Product_Name",
        "Price",
        "GST",
        "offer",
        "image"
    ]

   
    missing = [field for field in required_fields if field not in data or data[field] in (None, "")]

    if missing:
        return jsonify({
            "status": "error",
            "message": f"Missing fields: {', '.join(missing)}"
        }), 400

   
    try:
        image_data = data["image"].split(",")[-1]
        base64.b64decode(image_data)
    except Exception:
        return jsonify({
            "status": "error",
            "message": "Invalid base64 Image"
        }), 400

    products.append(data)

    return jsonify({
        "status": "success",
        "message": "Product registered",
        "product": data
    }), 201


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)