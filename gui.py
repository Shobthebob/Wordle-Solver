from tkinter import *
from tkinter import ttk
from customtkinter import *
from numpy import *
import warnings

warnings.filterwarnings("ignore")

root = CTk( )
root.title("Wordle Solver")
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

# Declaring and postitioning the back and next buttons
back = CTkButton(master=root, text="Back", width=80)
nextt = CTkButton(master=root, text="Next", width=80)

# To hide/show the next & back buttons
def hide_show(curr_frame):
	if(curr_frame=="start_frame"):
		back.grid_forget( )
		nextt.grid_forget( )
	else:
		back.grid(row=1, column=0, ipadx=10)
		nextt.grid(row=1, column=1, ipadx=10)


# Everything in the start frame (main frame)
def start(frm):

	hide_show("start_frame")
	frm.grid_forget( )
	root.geometry(f"{220}x{133}")

	global curr_frame
	curr_frame = "start_frame"

	start = CTkButton(master=start_frame, text="Start", width=60, command=lambda: eliminate(start_frame)) 
	leave = CTkButton(master=start_frame, text="Exit", width=60, command=root.destroy)
	
	start.grid(row=1, column=0, padx=35, pady = 50)
	leave.grid(row=1, column=1)

	start_frame.grid(row=0, column=0, ipadx=32, ipady=43)
	return

#Everything in the frame that asks for grey tiled letters
def eliminate(frm):

	hide_show("eliminate_frame")
	frm.grid_forget( )
	root.geometry(f"{220}x{134}")

	global curr_frame
	curr_frame = "eliminate_frame"

	enter = CTkLabel(master=eliminate_frame, text="Enter the letters that are NOT there")
	comment = CTkLabel(master=eliminate_frame, text="[GREY TILED LETTERS]")
	letters_not_there = CTkEntry(master=eliminate_frame, placeholder_text="No Commas Required")
	# back.config(state="disabled")
	
	enter.grid(row=0, column=0, ipadx=10)
	comment.grid(row=1, column=0)
	letters_not_there.grid(row=2, column=0, ipadx=25, pady=10)

	eliminate_frame.grid(row=0, column=0, columnspan=2)
	return

start(hide_frame)

root.mainloop( )
