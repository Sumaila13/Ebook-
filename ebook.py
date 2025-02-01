import pyttsx3
import PyPDF2

print(" YOU ARE WELCOME TO GAM EBOOK CONVERSION TO AUDIO (GEMA)")
print("We are here to make your work easy")

name= input("Enter your name : ")
Company= input("Enter your company or institution name : ")


def signUp():
    print("Sign up to  GEMA")
    try:
        name=str(input("Enter your name : "))
        emial=input("Enter your email : ")
        password=input("Enter your password : ")
        contact=int(input("Enter your contact : "))
    except ValueError:
        print("Invalid input")
    except TypeError:
        print("Enter a valid name")
    except Exception as e:
        print("Invalid input")
    else:
        print("Login success")
        ebook()


def ebook():
    book = open("Agricultural Technology.pdf", 'rb')
    pdfReader = PyPDF2.PdfReader(book)
    Pages = len(pdfReader.pages)
    print(Pages)
    Pages = pdfReader.pages[Pages-1]
    text = Pages.extract_text()
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()


def main():
    signUp()  
if __name__=="__main__":
    main()
