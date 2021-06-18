import PyPDF2
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# creating a pdf file object 
pdfFileObj = open('sample-pdf-file.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

# creating a page object 
pageObj = pdfReader.getPage(0) 
    
# extracting text from page 
text = str(pageObj.extractText())

#creating wordcloud from text
wc = WordCloud().generate(text)

#showing wordcloud
plt.imshow(wc)
plt.axis("off")
plt.show()