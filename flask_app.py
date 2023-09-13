from flask import *
import pdfsplitter
app = Flask(__name__)
app.secret_key = 'diaryyellowz'

@app.route("/")
def login():
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

        if username == 'via' and password == 'yellow':
            session['logged_in'] = True  # Set a session variable to indicate login status.
            return redirect("/welcomepage")

    return redirect("/")

    return redirect("/") 


