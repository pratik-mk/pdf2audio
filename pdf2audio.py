#imports
import pyttsx3
import PyPDF2

#pdf read
book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)

#number of pages
pages = pdfReader.numPages

#initialize speaker
speaker = pyttsx3.init()

#iterate pages
for num in range(pages):
    page = pdfReader.getPage(num)
    print("page no:",+page)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()