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
words = array(fobj.readlines())
gstr = ""

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
	if(curr_frame=="green_tile_frame"):
		back.grid_forget( )
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

# Everything in the frame that asks for grey tiled letters
def eliminate(frm):

	hide_show("eliminate_frame")
	frm.grid_forget( )
	root.geometry(f"{220}x{134}")

	global curr_frame
	curr_frame = "eliminate_frame"

	enter = CTkLabel(master=eliminate_frame, text="Enter the letters that are NOT there")
	comment = CTkLabel(master=eliminate_frame, text="[GREY TILED LETTERS]")
	letters_not_there = CTkEntry(master=eliminate_frame, placeholder_text="No Commas Required")

	back.configure(command=lambda: start(eliminate_frame))
	nextt.configure(command=lambda: greenTile(eliminate_frame))
	
	enter.grid(row=0, column=0, ipadx=10)
	comment.grid(row=1, column=0)
	letters_not_there.grid(row=2, column=0, ipadx=25, pady=10)

	eliminate_frame.grid(row=0, column=0, columnspan=2)
	return

# Everything in the frame that asks for green tiled chars
def greenTile(frm):

	def ver(ch1, ch2, ch3, ch4, ch5):

		st = ""

		val1 = len(ch1.get( ))
		val2 = len(ch2.get( ))
		val3 = len(ch3.get( ))
		val4 = len(ch4.get( ))
		val5 = len(ch5.get( ))
		if(val1>1) or (val2>1) or (val3>1) or (val4>1) or (val5>1):
			label = CTkLabel(master=green_tile_frame, text="[ONLY 1 CHAR/BLANKSPACE PER ENTRY]")
			label.grid(row=4, column=0, columnspan=5)
		else:
			li = [ch1.get( ),ch2.get( ),ch3.get( ),ch4.get( ),ch5.get( )]
			for i in li:
				if(i==""):
					st+="."
				else:
					st+=f"{i}"
			global gstr
			gstr = st
			verify.grid_forget( )
			nextt.configure(command=lambda: greenTile(eliminate_frame))
			nextt.grid(row=1, column=1, ipadx=10)
			

	hide_show("green_tile_frame")
	frm.grid_forget( )
	nextt.grid_forget( )
	# root.geometry( )

	enter1 = CTkLabel(master=green_tile_frame, text="Type in the letters with green tiles")
	enter2 = CTkLabel(master=green_tile_frame, text="Leave the rest blank")
	comment = CTkLabel(master=green_tile_frame, text="[1 Block = 1 Char]")

	c1 = CTkEntry(master=green_tile_frame, width=25, justify=CENTER)
	c2 = CTkEntry(master=green_tile_frame, width=25, justify=CENTER)
	c3 = CTkEntry(master=green_tile_frame, width=25, justify=CENTER)
	c4 = CTkEntry(master=green_tile_frame, width=25, justify=CENTER)
	c5 = CTkEntry(master=green_tile_frame, width=25, justify=CENTER)

	enter1.grid(row=0, column=0, columnspan=5)
	enter2.grid(row=1, column=0, columnspan=5)
	comment.grid(row=2, column=0, columnspan=5)
	c1.grid(row=3,column=0,sticky="nsew", ipady=5)
	c2.grid(row=3,column=1,sticky="nsew")
	c3.grid(row=3,column=2,sticky="nsew")
	c4.grid(row=3,column=3,sticky="nsew")
	c5.grid(row=3,column=4,sticky="nsew")

	verify = CTkButton(master=root, text="Verify", width=10, command=lambda: ver(c1,c2,c3,c4,c5))
	verify.grid(row=1, column=1, ipadx=10)

	green_tile_frame.grid(row=0, column=0, columnspan=3)
	return

start(hide_frame)

root.mainloop( )
