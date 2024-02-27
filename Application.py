# this is not even a little close to done.


import tkinter as tk
from tkinter import filedialog
from PIL import Image
import numpy as np


bg_path = ""
an_path = ""


def open_bg():
    global bg_path
    file_path = filedialog.askopenfilename()
    bg_path = file_path


def open_an():
    global an_path
    file_path = filedialog.askopenfilename()
    an_path = file_path


win = tk.Tk()
win.title("Animal localizer and classifier")

lbl = tk.Label(win, text='Choose background and picture of an animal', width=100, height=6, fg='Black')
lbl.pack()

button = tk.Button(text="Choose background Image", command=open_bg)
button.pack()

button2 = tk.Button(text="Choose animal Image", command=open_an)
button2.pack()

win.mainloop()

print(bg_path)
print(an_path)

print("now choose where the animal will be printed on the background")
x = int(input("Enter X location: "))
y = int(input("Enter Y location: "))

bg = Image.open(bg_path)
an = Image.open(an_path)

bg = np.array(bg)
an = np.array(an)
