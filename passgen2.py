'''
    PASSWORD GENERATOR
'''

import random
import string
import pyperclip
import tkinter as tk


def weakPass():
    pass


def mediumPass():
    pass


def strongPass():
    pass


def passwordMain(lengthOG, num=False, strength='weak', copy=False):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    punct = string.punctuation

    letter = lower + upper

    # empty string to store password
    paswd = ''
    length = lengthOG
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
            key = (random.randint(2, length) % length - 2)
            if key > length / 2:
                key = random.randint(1, key % length)
            length -= key
            for n in range(int(key)):
                paswd += random.choice(digit)
        key2 = random.randint(2, length//2)
        for i in range(key2):
            paswd += random.choice(letter)
        length -= key2
        for k in range(length):
            paswd += random.choice(punct)
        paswd = list(paswd)
        for r in range(((length * random.randint(1, 100)) // 5) % (lengthOG)):
            print("::")
            random.shuffle(paswd)

    random.shuffle(paswd)
    paswd = ''.join(paswd)
    if copy:
        pyperclip.copy(paswd)
        print('copied to clipboard...')
    return paswd


def main():
    win = tk.Tk()
    win.title("PASSGEN 2.0")
    print('weak : ')
    res = passwordMain(8, num=True, strength='weak', copy=False)
    print(res)
    label1 = tk.Label(win, text=res, fg='green', font=("Helvetica"))
    label1.pack()
    print('medium : ')
    res2 = passwordMain(8, num=True, strength='medium', copy=True)
    print(res2)
    label2 = tk.Label(win, text=res2, fg='blue', font=("Helvetica"))
    label2.pack()
    print('strong : ')
    res3 = passwordMain(8, num=True, strength='strong', copy=False)
    print(res3)
    label3a = tk.
    label3p = tk.Label(win, text=res3, fg='red', font=("Helvetica"))
    label3p.pack()
    win.mainloop()


if __name__ == "__main__":
    main()
