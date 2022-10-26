from tkinter import *
from tkinter import ttk
from numpy import *
from PIL import Image

root = Tk( )
fobj = open("five-letter-words.txt", "r")

# Initializing the frames
start_frame = Frame(root, bg="white")
eliminate_frame = Frame(root)
loading_frame = Frame(root)
green_tile_frame = Frame(root)
yellow_tile_frame = Frame(root)
output_frame = Frame(root)

# Everything in the start frame
img = Image.open("start.png")
img = img.resize((200,100), Image.ANTIALIAS)
img.show("sss")
start_img = PhotoImage(img)
start = Button(master=start_frame, image=start_img)
start.grid(row=50, column=50, padx=150, pady=150)
start_frame.pack( )

root.mainloop( )
