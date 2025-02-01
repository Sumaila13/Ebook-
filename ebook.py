import pyttsx3
import PyPDF2

print(" YOU ARE WELCOME TO GAM EBOOK CONVERSION TO AUDIO (GEMA)")
print("We are here to make your work easy")

username= str(input("Enter your username : "))



book = open("Agricultural Technology.pdf", 'rb')
pdfReader = PyPDF2.PdfReader(book)
Pages = len(pdfReader.pages)
print(Pages)
Pages = pdfReader.pages[Pages-1]
text = Pages.extract_text()
speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()

