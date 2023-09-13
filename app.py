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


@app.route("/success",methods=["POST"])
def success():
    global st1
    global en1
    global file
    st=int(request.form['start'])
    en=int(request.form['end'])
    st1=st-1
    en1=en-1
    print(st1)
    print(en1)
    f=request.files['file']
    file=f.filename
    f.save(file)
    return render_template("success.html",start=st,end=en,name=file)

@app.route("/convert")
def cropper():
    pdfsplitter.cropper(st1,en1,file)
    return render_template("download.html")



@app.route("/download")
def download():
    fnamestart = st1 +1
    fnameend = en1 +1
    filename=file.split(".")[0]+" Page "+str(fnamestart)+"-"+str(fnameend)+".pdf"
    return send_file(filename,as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
