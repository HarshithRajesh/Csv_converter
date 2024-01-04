import pandas as pd
import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk,Image
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\harsh\Downloads\build\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def fileread():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),filetypes=(("Text File","*.txt"),("All file","*.*")))
    data = pd.read_csv(filename)
    print(filename)
    file = filename.split(".txt")

    data.to_csv(f'{filename}.csv',index=None)


window = Tk()

window.geometry("458x651")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 651,
    width = 458,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

frame1 = Frame(window, highlightbackground="blue", highlightthickness=2)
frame1.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    458.0,
    651.0,
    fill="#D9D9D9",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    229.0,
    325.0,
    image=image_image_1
)
# img = (Image.open("d.png"))
# new_img = img.resize((50,50), Image.ANTIALIAS)
# image1 = ImageTk.PhotoImage(new_img)
# canvas.create_image(200,500,image=image1)


canvas.create_text(
    70.0,
    20.0,
    anchor="nw",
    text="Srishti Institute of Art, Design",
    fill="#29138F",
    font=("KohSantepheap Regular", 25 * -1)
)
canvas.create_text(
    135.0,
    50.0,
    anchor="nw",
    text="and Technology",
    fill="#29138F",
    font=("KohSantepheap Regular", 25 * -1)
)
# text1 = canvas.create_text(
#     136.0,
#     500.0,
#     anchor="nw",
#     text="Select File",
#     fill="#29148B",
#     font=("KohSantepheap Regular", 20 * -1)
# )
# canvas.tag_raise(text1)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = Button(window,
    text="Select File ",
    font=("KohSantepheap Regular", 20 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=fileread,
    relief="flat"
)
button_1.place(
    x=140.0,
    y=487.0,
    width=150.0,
    height=47.0
)


window.resizable(False, False)
window.mainloop()
