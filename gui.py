from tkinter import *
from tkinter import ttk
from customtkinter import *
from numpy import *
import warnings

warnings.filterwarnings("ignore")

root = CTk( )
root.title("Wordle Solver")
root.geometry(f"{200}x{200}")
set_appearance_mode("System")
set_default_color_theme("green")

fobj = open("five-letter-words.txt", "r")

# Initializing the frames
hide_frame = CTkFrame(root)
start_frame = CTkFrame(root)
eliminate_frame = CTkFrame(root)
loading_frame = CTkFrame(root)
green_tile_frame = CTkFrame(root)
yellow_tile_frame = CTkFrame(root)
output_frame = CTkFrame(root)

# Everything in the start frame
def start(frm):

	frm.grid_forget( )

	start = CTkButton(master=start_frame, text="Start", borderwidth=0, command=lambda: eliminate(start_frame)) # image=start_img, 
	
	start.grid(row=0, column=0)
	start_frame.grid(row=1,column=1)

#Everything in the eliminate frame
def eliminate(frm):

	frm.grid_forget( )

	enter = CTkLabel(master=eliminate_frame, text="Enter the letters that are NOT there")
	comment = CTkLabel(master=eliminate_frame, text="[No Commas Required]")

	letters_not_there = CTkEntry(master=eliminate_frame, placeholder_text="Enter:", width=1)
	
	enter.grid(row=0,column=0)
	comment.grid(row=1,column=0)
	letters_not_there.grid(row=2,column=0)
	eliminate_frame.grid(row=1, column=1)

start(hide_frame)

root.mainloop( )
