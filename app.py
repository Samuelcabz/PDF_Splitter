from flask import Flask, request, render_template, redirect, session, flash
import pdfsplitter
app = Flask(__name__)
app.secret_key = 'diaryyellowz'



@app.route("/")
def login():
    if session.get('logged_in'):
        session.clear() 
    return render_template("login.html")

@app.route("/welcomepage")
def welcomepage():
    if 'logged_in' in session and session['logged_in']:
        return render_template("welcomepage.html")
    else:
        return redirect("/")

@app.route("/checkform", methods=["POST"])
def checkform():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == 'yellow':
            session['logged_in'] = True
            return redirect("/welcomepage")
        else:
            flash('Incorrect username or password. Please try again.', 'error')

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
