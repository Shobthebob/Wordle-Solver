from tkinter import *
from tkinter import ttk
from turtle import bgcolor
from numpy import *

root = Tk( )
fobj = open("five-letter-words.txt", "r")

# Initializing the frames
start_frame = ttk.Frame(root, style="#ffffff")
eliminate_frame = ttk.Frame(root)
loading_frame = ttk.Frame(root)
green_tile_frame = ttk.Frame(root)
yellow_tile_frame = ttk.Frame(root)
output_frame = ttk.Frame(root)

start = ttk.Button(master=start_frame, text="Start")
start.pack( )
start_frame.pack(padx=100,pady=100)

root.mainloop( )
