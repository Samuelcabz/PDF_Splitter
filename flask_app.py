from flask import *
import pdfsplitter
app=Flask(__name__)


@app.route("/")
def upload():
    return render_template("file_upload.html")


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
    filename=file.split(".")[0]+"_Page_"+str(fnamestart)+"_"+str(fnameend)+".pdf"
    return send_file(filename,as_attachment=True)

