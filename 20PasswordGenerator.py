from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk
import random
import datetime
window = ThemedTk(theme="ubuntu")
window.geometry("600x130")
window.title("Password Generator")
#window.configure(bg="#E0E0E0")
window.resizable(False, False)
x=datetime.datetime.now()
day=x.day
month=x.month
key=(int(day)+int(month))+2
print(key)
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
password = ""
Password=StringVar()
Encryption = StringVar()


def copy(entry_widget):
    window.clipboard_clear()
    window.clipboard_append(entry_widget.get())

def generate():
    global password
    password = ""
    mikos=combo.get()
    diskolia=diff.get()
    print(int(combo.get()))

    if diskolia==3:
        for i in range (int(combo.get())):
            x=random.choice(digits)
            password=password+x
            print(password)
        Password.set(password)

    elif diskolia == 2:
        for i in range(int(combo.get())):
            x = random.choice(upper)
            password = password + x
            print(password)
        Password.set(password)

    elif diskolia == 1:
        for i in range(int(combo.get())):
            x = random.choice(lower)
            password = password + x
            print(password)
        Password.set(password)


def encrypt():
    global password
    newpass = ""
    for grammata in password:
        place = digits.index(grammata)
        newpass= newpass + digits[(place+key) %72]
        print(newpass)
    Encryption.set(newpass)


def decrypt():
    encrypted = Encryption.get()
    oldpass = ""
    for grammata in encrypted:
        place = digits.index(grammata)
        oldpass = oldpass + digits[(place - key) % 72]
    Encryption.set(oldpass)


lbl1 =Label(window,text="Password:")
lbl1.grid(column=1,row=1)
lbl2 =Label(window,text="Length :")
lbl2.grid(column=1,row=2)
lbl3 =Label(window,text="Encrypt")
lbl3.grid(column=1,row=3)
entry1=Entry(window,text=Password)
entry1.grid(column=2,row=1,)
entry3=Entry(window,text=Encryption)
entry3.grid(column=2,row=3,)
copy=Button(window,text="Copy",width=10,command=copy)
copy.grid(column=3,row=1,)
generate=Button(window,text="Generate",width=10,command=generate)
generate.grid(column=4,row=1,)
diff=IntVar()
diff.set(2)
button1 = Radiobutton(window,text="Weak",variable=diff, value=1)
button2 = Radiobutton(window,text="Normal",variable=diff, value=2)
button3 = Radiobutton(window,text="Strong",variable=diff, value=3)
button1.grid(column=3,row=2)
button2.grid(column=4,row=2)
button3.grid(column=5,row=2)
copy2=Button(window,text="Copy",width=10)
copy2.grid(column=3,row=3,)
encrypt=Button(window,text="Encrypt",width=10,command=encrypt)
encrypt.grid(column=4,row=3,)
decrypt=Button(window,text="Decrypt",width=10,command=decrypt)
decrypt.grid(column=5,row=3,)
combo = Combobox(window,)
combo['values'] = (5,6,7,8,9)
combo.current(1)
combo.grid(column=2, row=2)
footer = Label(window, text="created by thanos katsifis", font=("Segoe UI", 9, "italic"))
footer.grid(column=0, row=4, columnspan=6, pady=(10, 0))
window.mainloop()