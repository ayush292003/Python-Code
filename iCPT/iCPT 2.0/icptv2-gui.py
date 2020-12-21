'''
    PASSWORD GENERATOR
'''

import random
import string
import pyperclip
from tkinter import *
from tkinter import messagebox
import secrets


def passwordMain(lengthOG, num=False, strength='weak', copy=False):
    letters = string.ascii_letters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    punct = string.punctuation

    letter = lower + upper
    length = lengthOG

    # empty string to store password
    paswd = ''

    if strength == 'weak':
        if num:
            length -= 2
            for n in range(2):
                paswd += random.choice(digit)
        for i in range(length):
            paswd += random.choice(lower)
        paswd = list(paswd)

    elif strength == 'medium':
        if num:
            key = (random.randint(1, length) % length) // 2
            if key <= 2:
                key += length % (key+4)
            length -= key
            for n in range(int(key)):
                paswd += random.choice(digit)
        for i in range(length-1):
            paswd += random.choice(letter)
        paswd += random.choice(punct)
        paswd = list(paswd)

    elif strength == 'strong':
        if num:
            key = int((random.randint(2, length) % length - 2))
        if key > length / 2:
            key = int(random.randint(1, key % length))
        length -= key
        for n in range(int(key)):
            paswd += secrets.choice(digit)
        key2 = int(random.randint(2, (length+1)//2))
        for i in range(key2):
            paswd += secrets.choice(letters)
        length -= key2
        for k in range(length):
            paswd += secrets.choice(punct)
        paswd = list(paswd)
        if len(paswd) > lengthOG:
            paswd = paswd[:(lengthOG+1)]
        for r in range(int(((length * random.randint(1, 100)) % (lengthOG)))):
            random.shuffle(paswd)

    random.shuffle(paswd)
    paswd = ''.join(paswd)
    if copy:
        pyperclip.copy(paswd)
        print('copied to clipboard...')
    return paswd


win = Tk()
win.config(bg='black')
win.geometry('400x400')
label1 = Label(win, text='', fg='orange',
               bg='black', font=("ROGFonts-Regular"))
label1.pack()
label2 = Label(win, text='', fg='green', bg='black', font=("ROGFonts-Regular"))
label2.pack()
label3 = Label(win, text='', fg='red', bg='black', font=("ROGFonts-Regular"))
label3.pack()


def update_weak():
    length = len_scale.get()
    length = int(length)
    res = passwordMain(length, num=True, strength='weak', copy=False)
    label1.configure(text=res)


def update_medium():
    length = len_scale.get()
    length = int(length)
    res = passwordMain(length, num=True, strength='medium', copy=False)
    label2.configure(text=res)


def update_strong():
    length = len_scale.get()
    length = int(length)
    res = passwordMain(length, num=True, strength='strong', copy=False)
    label3.configure(text=res)
    yesno = messagebox.askyesno("iCPT", "WANNA COPY PASSWORD TO CLIPBOARD ?")
    if yesno:
        pyperclip.copy(res)


len_label = Label(win, text="LENGTH : ").pack(pady=15, padx=15)
len_scale = Scale(win, from_=6, to=18, orient=HORIZONTAL)
len_scale.pack(pady=2)
btn1 = Button(win, text="PASSWORD_WEAK", command=update_weak)
btn1.pack(pady=15)
btn2 = Button(win, text="PASSWORD_MEDIUM", command=update_medium)
btn2.pack(pady=15)
btn3 = Button(win, text="PASSWORD_STRONG", command=update_strong)
btn3.pack(pady=15)
win.mainloop()
