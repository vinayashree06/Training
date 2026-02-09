from flask import Flask,jsonify
app=Flask(__name__)
students_data={
    101:{"name":"Dr.Ravi","dept":"DAA"},
    102:{"name":"Dr.Meena","dept":"DBMS"},
    103:{"name":"Dr.Arun","dept":"OS"}

}
@app.route("/students",methods=['GET'])
def get_all_students():
    try:
        return jsonify(students_data)
    except Exception as e:
        return jsonify({"error":str(e)}),500
    finally:
        print("GET ALL Staff called")
if __name__=="__main__":
    app.run(debug=True)
