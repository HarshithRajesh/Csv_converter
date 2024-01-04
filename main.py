import os
from tkinter import *
from tkinter import filedialog
# import keyboard
import pandas as pd
from PIL import ImageTk,Image

windows = Tk()
windows.title(" SHRISHTI CSV ")
windows.config(pady = 50,padx = 50, bg = '#F1EB90')

def fileread():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),filetypes=(("Text File","*.txt"),("All file","*.*")))
    data = pd.read_csv(filename)
    print(filename)
    file = filename.split(".txt")

    data.to_csv(f'{filename}.csv',index=None)


canvas = Canvas(width=400,height=400,bg="#F1EB90",highlightthickness=0)
canvas.grid(row=1,column=1)
img = ImageTk.PhotoImage(Image.open("download.jpeg"))
canvas.create_image(200,200,image=img)
canvas.grid(column=1,row = 1)
title_label = Label(text = "TEXT TO CVS",fg='#9FBB73',bg='#F1EB90',font=("Ariel",26,"bold"))
title_label.grid(column=1,row=0)
btn = Button(text="Select File",command=fileread)
btn.grid(row=2,column=1)

windows.mainloop()
