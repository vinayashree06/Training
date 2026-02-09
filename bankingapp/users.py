from flask import Flask,request
from accounts import register_account_routes
from loans import register_loan_routes

app=Flask(__name__)
user={
1:{"username":"Vinaya","password":"Vini@12"},
2:{"username":"Teju","password":"Teju@12"},
3:{"username":"Vidya","password":"Vidh@12"},
4:{"username":"Shra","password":"shra@12"},
5:{"username":"Dhanush","password":"dhanu@12"}
}
register_loan_routes(app)

register_account_routes(app)
@app.route('/',methods=['GET','POST','PUT','DELETE'])
def login():
    if request.method=='GET':
        return user
    elif request.method=='POST':
        data=request.json
        username=data.get('username')
        password=data.get('password')
        new_id=len(user)+1
        user[new_id]={
            "username":username,
            "password":password
        }
        return {
            "message":"User created Successfully",
            "user_id":new_id,
            "user":user[new_id]
        },201
    elif request.method=='PUT':
        data=request.json
        user_id=data.get('id')
        if user_id not in user:
            return {"error":"User not found"},404
        
        if 'username' in data:
            user[user_id]['username'] = data['username']
        if 'password' in data:
            user[user_id]['password'] = data['password']

        return {
            "message": "User updated successfully",
            "user": user[user_id]
        }, 200

    elif request.method=='DELETE':
        data=request.json
        user_id=int(data.get('id'))
        if user_id not in user:
            return {"error":"User not found"},404
        deleted_user=user.pop(user_id)
        
        return{
            "message":"User deleted successfully",
            "deleted user":deleted_user
        },200
 
if __name__=="__main__":
    app.run(debug=True)
