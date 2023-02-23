from flask import *
import pdfsplitter
app=Flask(__name__)

st1 = None
en1 = None
file = None

@app.route("/fileupload")
def fileupload():
    return render_template("file_upload.html")


@app.route("/success",methods=["POST"])
def success():
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

@app.route("/convert/<st1>/<en1>/<file>")
def cropper(st1,en1,file):
    pdfsplitter.cropper(st1,en1,file)
    return render_template("download.html",st1=st1,en1 = en1,file=file)



@app.route("/download/<st1>/<en1>/<file>")
def download(st1,en1,file):
    fnamestart = int(st1) +1
    fnameend = int(en1) +1
    filename=file.split(".")[0]+"_Page_"+str(fnamestart)+"_"+str(fnameend)+".pdf"
    return send_file("/home/samieeee/PDF_Splitter/"+filename,as_attachment=True)

