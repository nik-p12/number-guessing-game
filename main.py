from tkinter import Tk, Frame, Label, Entry, Button,PhotoImage,Toplevel
import random
from PIL import Image, ImageTk

trial = 5
nb = 0

def open_popup(value):
   top= Toplevel(root)
   top.geometry(f"250x30+{x_position  + 10}+{y_position + 30}")
   top.title("")
   Label(top, text= value, font=("Arial", 12), fg = "red").place(relx = 0.0, y = 0.0)
   top.after(5000, top.destroy, top)

def init_game():
    global trial ,nb
    trial = 5
    nb = random.randint(1,100)

def on_enter(event):
    if validate_input():
        main()
    entry.delete(0, "end") 

def process(value): 
    global trial,labels
    if trial > 0:
        if value == nb:
            open_popup("Congrat 👏🏽, you win")
        if value < nb:
            open_popup("Try again! You guessed too small")
        else:
            open_popup("Try again! You guessed too highed")
        label = labels[trial - 1]
        label.destroy()
        labels.pop()
        entry.delete(0,"end") 
        entry.insert(0, "Guess a number")
        entry.config(fg = "grey")
        trial -=1
        entry.delete
    else:
        open_popup("You lose")
        init_game()
        labels = [label1, label1, label3, label4, label5]

def validate_input():
    return entry.get().isdigit() or entry.get() == "Guess the number"

def main():
    if validate_input():
        process(int(entry.get()))
    else: 
        entry.delete(0,"end") 
        entry.insert(0, "Guess a number")
        entry.config(fg = "grey")

def on_entry_click(event):
    if entry.get() == "Guess the number":
        entry.delete(0,"end") 
        entry.config(fg = "black")

def on_focus_out(event):
    if entry.get() =="":
        entry.insert(0, "Guess a number")
        entry.config(fg = "grey")

init_game()

root = Tk()
x_position = int(root.winfo_screenwidth() *0.25)
y_position = int (root.winfo_screenheight() * 0.25)
root.title("Number Guessing game")
root.geometry(f"700x450+{x_position}+{y_position}")
root.config(bg = "#328f8a")

trial_frame = Frame(
    root,
    bg = "#ffffff",
    height = 30,
    width = 90
)
trial_frame.place(relx = 0.70, rely = 0.05, anchor = "nw")
image = Image.open("./assets/heart.png").convert("RGBA")
image = image.resize((30,30))
logo = ImageTk.PhotoImage(image)
label1 = Label(trial_frame, image = logo)
label1.pack(side = "right")
label2 = Label(trial_frame, image = logo)
label2.pack(side = "right")
label3 = Label(trial_frame, image = logo)
label3.pack(side = "right")
label4 = Label(trial_frame, image = logo)
label4.pack(side = "right")
label5 = Label(trial_frame, image = logo)
label5.pack(side = "right")
labels = [label1, label1, label3, label4, label5]

frame = Frame(root,
              bg = "#ffffff",
              width = 350,
              height = 400)
frame.place(relx = 0.5 ,rely = 0.5, anchor = "center")

title = Label(frame,text = "Game", font = ("Arial", 16, "bold"), bg ="#ffffff")
title.pack(pady = 20, fill = "x")

validate_commande = root.register(main)
entry = Entry(frame,validate = "key", validatecommand = (main, '%P'), width = 30, borderwidth = 1, relief = "solid")
entry.insert(0, "Guess a number")
entry.config(fg = "grey", justify = "center")
entry.bind("<Return>", on_enter)
entry.bind("<FocusIn>",on_entry_click)
entry.bind("<FocusOut>",on_focus_out)
entry.pack(padx = 15, pady = 25)

button = Button(frame, text = "Play", fg ="#ffffff", command = main, width= 20, bg= "#32de84")
button.pack(padx = 35, pady = 30)

root.mainloop()