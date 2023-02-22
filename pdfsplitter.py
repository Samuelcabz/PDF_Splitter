from PyPDF2 import PdfFileWriter,PdfFileReader

def cropper(start,end,file):
    inputPdf = PdfFileReader(open(file,"rb"))
    outPdf = PdfFileWriter()
    fnamestart = "{}".format(int(start)+1)
    fnameend = "{}".format(int(end)+1)
    ostream=open(file.split(".")[0]+"_Page_"+str(fnamestart)+"_"+str(fnameend)+".pdf","wb")

    while start <= end:
        outPdf.addPage(inputPdf.getPage(start))
        outPdf.write(ostream)
        start+=1
    
    ostream.close()
    
