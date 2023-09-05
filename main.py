from tkinter import *
from PIL import Image, ImageTk # pip install pillow
import tkinter.messagebox
from encryptprocess import EncryptWork, decrypt_process

def getEncDictionary():
    encDictionary = {
        "title": str(titleEntry.get()),
        "text": str(textEntry.get("1.0", END)),
        "masterkey": masterEntry.get()
    }

    return encDictionary
def inputControl():
    encDictionary = getEncDictionary()

    masterkey = encDictionary["masterkey"]
    text = encDictionary["text"]

    if masterkey.strip() == "":
        tkinter.messagebox.showerror("Empty Value", "Masterkey should not be empty.")
        return False
    elif text.strip() == "":
        tkinter.messagebox.showerror("Empty Value", "Text should not be empty.")
        return False
    else:
        return True
def encryptProcess():
    encDictionary = getEncDictionary()

    if(inputControl()):
        encObject = EncryptWork(encDictionary, "my_secret_text")
        encObject.saveEncryptMessage()
        masterEntry.delete(0, "end")
        textEntry.delete("1.0", END)
        titleEntry.delete(0, "end")

def decryptProcess():
    if(inputControl()):
        original_text = decrypt_process(masterEntry, textEntry)
        masterEntry.delete(0, "end")
        textEntry.delete("1.0", END)
        textEntry.insert("1.0", original_text)


window = Tk()
window.title("Secret Notes")
window.geometry("500x700")

image = Image.open("encrypt.jpg")
img = ImageTk.PhotoImage(image.resize((300, 200)))

imageLabel = Label(image=img)
imageLabel.pack(pady=10)

titleLabel = Label(text="Enter your title")
titleLabel.pack(pady=10)

titleEntry = Entry(width=30)
titleEntry.pack()

textLabel = Label(text="Enter your secret")
textLabel.pack(pady=10)

textEntry = Text(width=50, height=10)
textEntry.pack()

masterLabel = Label(text="Enter master key")
masterLabel.pack(pady=10)

masterEntry = Entry(width=30)
masterEntry.pack()

buttonEncrypt = Button(text="Save & Encrypt", command=encryptProcess)
buttonEncrypt.pack(pady=10)

buttonDecrypt = Button(text="Decrypt", command=decryptProcess)
buttonDecrypt.pack(pady=10)


window.mainloop()
