from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "secret123"   # required for flash messages

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Try again'
        else:
            flash("You were successfully logged in")
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/index')
def index():
    return "Welcome Admin! Login Successful"

if __name__ == "__main__":
    app.run(debug=True)
