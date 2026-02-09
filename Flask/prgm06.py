from flask import Flask, redirect, url_for
from prgm05 import register_routes

app = Flask(__name__)

# 🔴 Register routes from prgm05
register_routes(app)

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

if __name__ == "__main__":
    app.run(debug=True)
