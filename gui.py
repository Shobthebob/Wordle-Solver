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

global gstr
gstr = " "

# Initializing the frames
hide_frame = CTkFrame(root)
start_frame = CTkFrame(root)
eliminate_frame = CTkFrame(root)
loading_frame = CTkFrame(root)
green_tile_frame = CTkFrame(root, width=100)
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
	elif(curr_frame=="green_tile_frame"):
		back.grid_forget( )
		nextt.grid(row=1,column=1, ipadx=83)
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

	def check(ch):
		
		ch = ch.get( )
		if((ch=="") or (ch.isalpha( ))) and (len(ch)<2):
			nextt.configure(state="normal", justify=CENTER)
		else:
			nextt.configure(state="disabled")
			comment.configure(text="[ONLY 1 CHAR/BLANKSPACE PER ENTRY]")			

	hide_show("green_tile_frame")
	frm.grid_forget( )
	root.geometry(f"{289}x{140}")

	# Different lables on the screen
	enter1 = CTkLabel(master=green_tile_frame, text="Type in the letters with green tiles in their positions")
	enter2 = CTkLabel(master=green_tile_frame, text="Leave the rest blank")
	comment = CTkLabel(master=green_tile_frame, text="[1 Block = 1 Char]")

	ch1 = StringVar( )
	ch2 = StringVar( )
	ch3 = StringVar( )
	ch4 = StringVar( )
	ch5 = StringVar( )
	ch1.trace_add("write", lambda: check(ch1))
	ch2.trace_add("write", lambda: check(ch2))
	ch2.trace_add("write", lambda: check(ch3))
	ch3.trace_add("write", lambda: check(ch4))
	ch4.trace_add("write", lambda: check(ch5))

	# The 5 entry boxes 
	c1 = CTkEntry(master=green_tile_frame, width=25, justify=CENTER, textvariable=ch1)
	c2 = CTkEntry(master=green_tile_frame, width=25, justify=CENTER, textvariable=ch2)
	c3 = CTkEntry(master=green_tile_frame, width=25, justify=CENTER, textvariable=ch3)
	c4 = CTkEntry(master=green_tile_frame, width=25, justify=CENTER, textvariable=ch4)
	c5 = CTkEntry(master=green_tile_frame, width=25, justify=CENTER, textvariable=ch5)

	# Placing everything using grid( )
	enter1.grid(row=0, column=0, columnspan=5)
	enter2.grid(row=1, column=0, columnspan=5)
	comment.grid(row=2, column=0, columnspan=5)
	c1.grid(row=3,column=0,columnspan=4)
	c2.grid(row=3,column=1,columnspan=3)
	c3.grid(row=3,column=2,columnspan=2)
	c4.grid(row=3,column=3,columnspan=1)
	c5.grid(row=3,column=4,columnspan=1)
	green_tile_frame.grid(row=0, column=0, columnspan=3)
	return

start(hide_frame)

root.mainloop( )
