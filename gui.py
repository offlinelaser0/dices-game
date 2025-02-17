import os
import tkinter as tk

from tkinter import ttk

from playsound import playsound

from PIL import Image, ImageTk
from dices import roll_dice

# Initialize the main window
root = tk.Tk()
root.title('ИГРА В КОСТИ')
root.geometry('1200x600')
root.attributes('-fullscreen', True)

# Custom styling
root.configure(bg='#2E3440')  # Dark background

# Create a custom style for rounded buttons
style = ttk.Style()
style.configure('Rounded.TButton', font=('Helvetica', 14), padding=10, background='#4C566A', foreground='black', borderwidth=5, focusthickness=3, focuscolor='none', relief='flat')
style.map('Rounded.TButton', background=[('active', '#5E81AC')])  # Change color on hover

style.configure('TLabel', font=('Helvetica', 16), background='#2E3440', foreground='#ECEFF4')
style.configure('TCombobox', font=('Helvetica', 14), padding=10)

# Frame for dice images
dice_frame = ttk.Frame(root)
dice_frame.pack(pady=20)

# Label for instructions
choice_label = ttk.Label(root, text="Выберите число от 1 до 3")
choice_label.pack(pady=10)

# Drop-down menu for user input
choice_var = tk.StringVar()
choice_dropdown = ttk.Combobox(root, textvariable=choice_var, width=20, state='readonly')
choice_dropdown['values'] = (1, 2, 3)  # Available choices
choice_dropdown.current(0)  # Set default selection to the first option
choice_dropdown.pack(pady=10)

# Label for error messages
error_label = ttk.Label(root, text="", foreground='#BF616A')  # Red color for errors
error_label.pack(pady=5)

def play():
    playsound(f"{os.getcwd()}/game_sounds/dices-sound.mp3")

# Function to roll dice and display images
def make_dice():
    try:
        user_choice = int(choice_var.get())  # Get selected value from drop-down
        if user_choice < 1 or user_choice > 3:
            error_label.config(text="Пожалуйста, выберите число от 1 до 3.")
            return

        error_label.config(text="")  # Clear any previous errors
        dice_tuple = roll_dice(user_choice)

        # Clear previous dice images
        for widget in dice_frame.winfo_children():
            widget.destroy()

        # Display new dice images
        for dice_number in dice_tuple:
            image_path = f"{os.getcwd()}/game_images/dice{dice_number}.png"
            if os.path.exists(image_path):
                image = Image.open(image_path)
                image = image.resize((100, 100))  # Resize for consistency
                photo = ImageTk.PhotoImage(image)
                dice_label = ttk.Label(dice_frame, image=photo)
                dice_label.image = photo  # Keep a reference to avoid garbage collection
                dice_label.pack(side=tk.LEFT, padx=10)
            else:
                error_label.config(text=f"Изображение для кости {dice_number} не найдено.")
                return
    except ValueError:
        error_label.config(text="Пожалуйста, выберите корректное число.")

# Submit button with rounded corners
image_path = f"{os.getcwd()}/game_images/button.jpg"
button_img = ImageTk.PhotoImage(file=image_path)
pirate_button = ttk.Button(root, image=button_img, style='Rounded.TButton', command=lambda: [play(), make_dice()])
pirate_button.pack(pady=10)
submit_button = ttk.Button(root, text='Бросить кости', style='Rounded.TButton', command=lambda: [play(), make_dice()])
submit_button.pack(pady=10)

# Fullscreen toggle button with rounded corners
def toggle_fullscreen():
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

fullscreen_button = ttk.Button(root, text='Полный экран', style='Rounded.TButton', command=toggle_fullscreen)
fullscreen_button.pack(pady=10)

# Quit button with rounded corners
quit_button = ttk.Button(root, text='Выйти', style='Rounded.TButton', command=root.destroy)
quit_button.pack(side=tk.BOTTOM, pady=20)

# Run the application
root.mainloop()
