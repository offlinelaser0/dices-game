import os

import tkinter

from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import Tk, Button, BOTTOM, X, Entry
from tkinter.ttk import Label

from dices import roll_dice


root = Tk() 
root.title('ИГРА В КОСТИ')
root.geometry('1200x600')
root.attributes('-fullscreen',True)

choice_label = Label(text="Выберите число от 1 до 3")
choice_label.pack()
choice_input = Entry(root, width=20)
choice_input.pack()

def make_dice():
    dice_tuple = roll_dice(choice_input.get())

    for dice_number in dice_tuple:
        # Create a photoimage object of the image in the path
        image1 = Image.open(f"{os.getcwd()}/game_images/dice{dice_number}.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(root, image=test)
        label1.image = test
        # Position image

        label1.pack()

    return True

submit_button = ttk.Button(root, text='Submit', command=lambda: make_dice())
submit_button.pack()

btn = Button(text='Пиратка', command=root.destroy)
btn.pack(fill=X, padx=[20, 60], pady=30)

quit_button = ttk.Button(root, text='Выйти', command=root.destroy)
quit_button.pack(side=BOTTOM)

root.mainloop()
