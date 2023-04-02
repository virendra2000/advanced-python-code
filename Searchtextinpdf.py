import PyPDF2
import os
import textract
x = os.listdir()
text = input("Search Your Text");
for i in range(1,7):
    reader = PyPDF2.PdfFileReader(x[i])
    st = ''
    for y in range(0,2000):
        try:
            st = st + reader.getPage(y).extractText()
        except:
            break
if name in st:
    print("True")
else:
    pass
        
