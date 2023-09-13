from flask import Flask, request, render_template, redirect
import pdfsplitter
app=Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")

@app.route("/welcomepage")
def welcomepage():
    return render_template("welcomepage.html")

@app.route("/checkform", methods=["POST"])
def checkform():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'via' and password == 'yellow':
            return redirect("/welcomepage")

    return redirect("/") 



if __name__ == "__main__":
    app.run(debug=True)
