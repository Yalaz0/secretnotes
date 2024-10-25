import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Secret Notes")
window.config(padx=20,pady=20)
window.minsize(width=340,height=670)
window.maxsize(width=340,height=670)
window.focus()

resim = PhotoImage(file="download.png")
resim_label = tkinter.Label(window, image=resim,)
resim_label.pack()

label1 = tkinter.Label(text="Enter your title")
label1.pack()

entry1 = tkinter.Entry()
entry1.pack()

label2 = tkinter.Label(text="Enter your secret")
label2.config()
label2.pack()

txt = tkinter.Text()
txt.config(height=15)
txt.pack()

label3 = tkinter.Label(text="Enter master key")
label3.pack()

entry3 = tkinter.Entry()
entry3.pack()

button1 = tkinter.Button(text="Save & Encrypt")
button1.pack()

button2 = tkinter.Button(text="Decrypt")
button2.pack()

window.mainloop()