from flask import Flask,jsonify
app=Flask(__name__)
students_data={
    1:{"name":"Anu","dept":"CSE","year":3},
    2:{"name":"Annupama","dept":"ISE","year":4},
    3:{"name":"Anupama parameshwaran","dept":"ECE","year":1}

}
@app.route("/students",methods=['GET'])
def get_all_students():
    try:
        return jsonify(students_data)
    except Exception as e:
        return jsonify({"error":str(e)}),500
    finally:
        print("GET ALL Students called")
if __name__=="__main__":
    app.run(debug=True)
