import pyttsx3
import PyPDF2
import time

print(" YOU ARE WELCOME TO GAM EBOOK CONVERSION TO AUDIO (GEMA)")
print("We are here to make your work easy")


def signUp():
    print("Sign up to  GEMA")
    try:
        name=str(input("Enter your name : "))
        email=input("Enter your email : ")
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
    start_time = time.time()
    speaker.say(text)
    speaker.runAndWait()
    end_time = time.time()

    duration = end_time - start_time
    print(f"Audio Duration: {duration:.2f} seconds")





def main():
    signUp()  
if __name__=="__main__":
    main()
