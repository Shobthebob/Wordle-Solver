from tkinter import *
from tkinter import ttk
from numpy import *
from PIL import Image, ImageTk, ImageOps

root = Tk( )
fobj = open("five-letter-words.txt", "r")

# Adding a background
back = Image.open("background.png")
back = back.transpose(Image.FLIP_LEFT_RIGHT)
background = ImageTk.PhotoImage(back)

# Initializing the frames
start_frame = Frame(root, bg="black")
eliminate_frame = Frame(root)
loading_frame = Frame(root)
green_tile_frame = Frame(root)
yellow_tile_frame = Frame(root)
output_frame = Frame(root)

# Everything in the start frame
back_l = Label(start_frame, image=background)
back_l.place(x=0, y=0)
img = ImageOps.expand(Image.open("start.png"), border=8, fill="black")
img = img.resize((200,100))
start_img = ImageTk.PhotoImage(img)
start = Button(master=start_frame, image=start_img, borderwidth=-10)
start.grid(row=50, column=50, padx=100, pady=75)
start_frame.pack(side=LEFT)

#Everything in the eliminate frame
enter = Label(master=eliminate_frame, text="Enter the letters that are NOT there")
comment = Label(master=eliminate_frame, text="[No Commas Required]")
letters_not_there = ttk.Entry(master=eliminate_frame, width=26)
enter.grid(row=0,column=0)
comment.grid(row=1,column=0)
letters_not_there.grid(row=2,column=0)
eliminate_frame.pack(side=BOTTOM)

root.mainloop( )
