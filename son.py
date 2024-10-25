import tkinter
from tkinter import *
from tkinter import messagebox  # Uyarı pencereleri için

def encrypt_message():
    title = entry1.get()
    message = txt.get("1.0", "end-1c")
    key = entry3.get()

    if not title or not message or not key:
        messagebox.showwarning("Warning", "Please enter a title, a secret message, and a master key.")
        return

    # XOR Şifreleme
    encrypted_message = "".join([chr(ord(char) ^ ord(key[i % len(key)])) for i, char in enumerate(message)])

    # Şifreli mesajı gösterme
    txt.delete("1.0", "end")
    txt.insert("1.0", encrypted_message)
    messagebox.showinfo("Info", "Message encrypted successfully!")

    # Şifrelenmiş mesajı dosyaya yazma
    try:
        with open("encrypted_messages.txt", "a") as file:
            file.write(f"Title: {title}\n")
            file.write(f"Encrypted Message: {encrypted_message}\n")
            file.write("=" * 40 + "\n")  # Ayırıcı çizgi
    except Exception as e:
        messagebox.showerror("Error", f"Could not save to file: {e}")

def decrypt_message():
    encrypted_message = txt.get("1.0", "end-1c")
    key = entry3.get()

    if not encrypted_message or not key:
        messagebox.showwarning("Warning", "Please enter both an encrypted message and the master key.")
        return

    # XOR Çözme
    decrypted_message = "".join([chr(ord(char) ^ ord(key[i % len(key)])) for i, char in enumerate(encrypted_message)])

    # Şifre çözülmüş mesajı gösterme
    txt.delete("1.0", "end")
    txt.insert("1.0", decrypted_message)
    messagebox.showinfo("Info", "Message decrypted successfully!")

# Tkinter Arayüzü
window = tkinter.Tk()
window.title("Secret Notes")
window.config(padx=20, pady=20)
window.minsize(width=340, height=670)
window.maxsize(width=340, height=670)
window.focus()

resim = PhotoImage(file="download.png")
resim_label = tkinter.Label(window, image=resim)
resim_label.pack()

label1 = tkinter.Label(text="Enter your title")
label1.pack()

entry1 = tkinter.Entry()
entry1.pack()

label2 = tkinter.Label(text="Enter your secret")
label2.pack()

txt = tkinter.Text()
txt.config(height=15)
txt.pack()

label3 = tkinter.Label(text="Enter master key")
label3.pack()

entry3 = tkinter.Entry(show="*")
entry3.pack()

button1 = tkinter.Button(text="Save & Encrypt", command=encrypt_message)
button1.pack()

button2 = tkinter.Button(text="Decrypt", command=decrypt_message)
button2.pack()

window.mainloop()
