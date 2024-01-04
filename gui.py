import pandas as pd
import os
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog,messagebox
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
import csv
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\harsh\Downloads\build\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_file():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            file_content.set(file.read())

def save_as_csv():
    file_content_str = file_content.get()

    # Assuming the content is comma-separated values (CSV)
    csv_data = [line.split(',') for line in file_content_str.split('\n')]

    csv_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if csv_file_path:
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(csv_data)
            messagebox.showinfo("File Saved!!!1!")

window = Tk()
window.title("CSV Converter")
window.geometry("458x651")
window.configure(bg = "#FFFFFF")
file_content = tk.StringVar()

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
    command=open_file,
    relief="flat"
)
button_1.place(
    x=140.0,
    y=387.0,
    width=170.0,
    height=47.0
)
button_2 = Button(window,
    text="Convert File ",
    font=("KohSantepheap Regular", 20 * -1),
    borderwidth=0,
    highlightthickness=0,
    command=save_as_csv,
    relief="flat"
)
button_2.place(
    x=140.0,
    y=330.0,
    width=170.0,
    height=47.0
)


window.resizable(False, False)
window.mainloop()
