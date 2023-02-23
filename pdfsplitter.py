from PyPDF2 import PdfFileWriter,PdfFileReader

def cropper(start,end,file):
    inputPdf = PdfFileReader(open(file,"rb"))
    outPdf = PdfFileWriter()
    fnamestart = str(int(start)+1)
    fnameend = str(int(end)+1)
    ostream=open("/home/samieeee/PDF_Splitter/"+file.split(".")[0]+"-Page-"+str(fnamestart)+"-"+str(fnameend)+".pdf","wb")

    start = int(start)
    end = int(end)
    while start <= end:
        outPdf.addPage(inputPdf.getPage(start))
        outPdf.write(ostream)
        start+=1
    
    ostream.close()
    
