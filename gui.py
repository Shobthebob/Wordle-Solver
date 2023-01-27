from tkinter import *
from tkinter import ttk
from customtkinter import *
import warnings

warnings.filterwarnings("ignore")

root = CTk( )
root.title("Wordle Solver")
set_appearance_mode("System")
set_default_color_theme("green")

fobj = open("five-letter-words.txt", "r")
all_words = fobj.readlines()
all_words = [(i.replace("\n","")).upper() for i in all_words]
possible_words = []

global_str = ""
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Initializing the frames
hide_frame = CTkFrame(root)
start_frame = CTkFrame(root)
eliminate_frame = CTkFrame(root)
loading_frame = CTkFrame(root)
green_tile_frame = CTkFrame(root, width=100)
yellow_tile_frame = CTkFrame(root)
loading_frame = CTkFrame(root)
output_frame = CTkFrame(root)

# Declaring and postitioning the back and next buttons
back = CTkButton(master=root, text="Back", width=80)
nextt = CTkButton(master=root, text="Next", width=80)

# Subtracts two given lists
def subtract(main_list: list, small_list:list) -> list:
	return [i for i in main_list if i not in small_list]

# Removes all duplicate characters in a string
def duplicateRemover(str: str) -> str:
	li = []
	st = ""
	for i in str:
		if(i not in li):
			li.append( )
			st+=i
	return st		

# To hide/show the next & back buttons
def hide_show(curr_frame: CTkFrame) -> None:

	if(curr_frame=="start_frame") or (curr_frame=="loading_frame"):
		back.grid_forget( )
		nextt.grid_forget( )
	elif(curr_frame=="green_tile_frame"):
		back.grid_forget( )
		nextt.grid(row=1,column=1, ipadx=83, padx=4)
	elif(curr_frame=="yellow_tile_frame"):
		back.grid_forget( )
		nextt.grid(row=1,column=1, ipadx=70)
	else:
		back.grid(row=1, column=0, ipadx=10)
		nextt.grid(row=1, column=1, ipadx=10)
	return

# Everything in the start frame (main frame)
def start(frm: CTkFrame) -> None:

	hide_show("start_frame")
	frm.grid_forget( )
	root.geometry(f"{220}x{133}")

	start = CTkButton(master=start_frame, text="Start", width=60, command=lambda: eliminateGUI(start_frame)) 
	leave = CTkButton(master=start_frame, text="Exit", width=60, command=root.destroy)
	
	start.grid(row=1, column=0, padx=35, pady = 50)
	leave.grid(row=1, column=1)

	start_frame.grid(row=0, column=0, ipadx=32, ipady=43)
	return

# Everything in the frame that asks for grey tiled letters
def eliminateGUI(frm: CTkFrame) -> None:

	hide_show("eliminate_frame")
	frm.grid_forget( )
	root.geometry(f"{220}x{134}")

	enter = CTkLabel(master=eliminate_frame, text="Enter the letters that are NOT there")
	comment = CTkLabel(master=eliminate_frame, text="[GREY TILED LETTERS]")
	letters_not_there = CTkEntry(master=eliminate_frame, placeholder_text="No Commas Required")

	back.configure(command=lambda: start(eliminate_frame))
	nextt.configure(command=lambda: [greenTile(eliminate_frame), eliminate(letters_not_there.get( ).upper( ))])
	
	enter.grid(row=0, column=0, ipadx=10)
	comment.grid(row=1, column=0)
	letters_not_there.grid(row=2, column=0, ipadx=25, pady=10)

	eliminate_frame.grid(row=0, column=0, columnspan=2) # columnspan for the next & back buttons
	return

# Eliminates all characters that are not there
def eliminate(letters_not_there: str) -> str:

	print(f"{letters_not_there=}")
	global alphabets, all_words, possible_words
	deleted_words = []
	letters_not_there = duplicateRemover(letters_not_there)
	alphabets_not_there = list(letters_not_there)
	alphabets = subtract(main_list=alphabets, small_list=alphabets_not_there)
	print(f"{alphabets=}")
	print(f"{alphabets_not_there=}")

	for i in all_words:
		for j in i:
			if(j in alphabets_not_there):
				deleted_words.append(i)
				break
	possible_words = subtract(main_list=all_words, small_list=deleted_words)
	print(f"{possible_words=}")

# Everything in the frame that asks for green tiled chars
def greenTile(frm: CTkFrame) -> None:

	global global_str

	# creating different functions to make sure no one gives a wrong input in each entry
	def check1(cha1, index, mode) -> None:

		cha1 = ch1.get( )
		# for 1st entry
		if((not cha1.isalpha( ) and cha1!="") or (len(cha1)>1)):
			nextt.configure(state="disabled")
			c2.configure(state="disabled")
			c3.configure(state="disabled")
			c4.configure(state="disabled")
			c5.configure(state="disabled")
			comment.configure(text="[ONLY 1 ALPHABET/BLANKSPACE PER ENTRY]", padx=4)
			root.geometry(f"{276}x{140}")
		else:
			nextt.configure(state="normal")
			c2.configure(state="normal")
			c3.configure(state="normal")
			c4.configure(state="normal")
			c5.configure(state="normal")
			comment.configure(text="Valid")		
			root.geometry(f"{255}x{140}")		
		return
	def check2(cha2, index, mode) -> None:

		cha2 = ch2.get( )
		# for 2nd entry
		if((not cha2.isalpha( ) and cha2!="") or (len(cha2)>1)):
			nextt.configure(state="disabled")
			c1.configure(state="disabled")
			c3.configure(state="disabled")
			c4.configure(state="disabled")
			c5.configure(state="disabled")
			comment.configure(text="[ONLY 1 ALPHABET/BLANKSPACE PER ENTRY]", padx=4)
			root.geometry(f"{276}x{140}")
		else:
			nextt.configure(state="normal")
			c1.configure(state="normal")
			c3.configure(state="normal")
			c4.configure(state="normal")
			c5.configure(state="normal")
			comment.configure(text="Valid")	
			root.geometry(f"{255}x{140}")
		return
	def check3(cha3, index, mode) -> None:

		cha3 = ch3.get( )
		# for 3rd entry
		if((not cha3.isalpha( ) and cha3!="") or (len(cha3)>1)):
			nextt.configure(state="disabled")
			c1.configure(state="disabled")
			c2.configure(state="disabled")
			c4.configure(state="disabled")
			c5.configure(state="disabled")
			comment.configure(text="[ONLY 1 ALPHABET/BLANKSPACE PER ENTRY]", padx=4)
			root.geometry(f"{276}x{140}")
		else:
			nextt.configure(state="normal")
			c1.configure(state="normal")
			c3.configure(state="normal")
			c4.configure(state="normal")
			c5.configure(state="normal")
			comment.configure(text="Valid")
			root.geometry(f"{255}x{140}")
		return
	def check4(cha4, index, mode) -> None:

		cha4 = ch4.get( )
		# for 4th entry 
		if((not cha4.isalpha( ) and cha4!="") or (len(cha4)>1)):
			nextt.configure(state="disabled")
			c1.configure(state="disabled")
			c2.configure(state="disabled")
			c3.configure(state="disabled")
			c5.configure(state="disabled")
			comment.configure(text="[ONLY 1 ALPHABET/BLANKSPACE PER ENTRY]", padx=4)
			root.geometry(f"{276}x{140}")
		else:
			nextt.configure(state="normal")
			c1.configure(state="normal")
			c2.configure(state="normal")
			c3.configure(state="normal")
			c5.configure(state="normal")
			comment.configure(text="Valid")	
			root.geometry(f"{255}x{140}")
		return
	def check5(cha5, index, mode) -> None:

		cha5 = ch5.get( )
		#for 5th entry
		if((not cha5.isalpha( ) and cha5!="") or (len(cha5)>1)):
			nextt.configure(state="disabled")
			c1.configure(state="disabled")
			c2.configure(state="disabled")
			c3.configure(state="disabled")
			c4.configure(state="disabled")
			comment.configure(text="[ONLY 1 ALPHABET/BLANKSPACE PER ENTRY]", padx=4)
			root.geometry(f"{276}x{140}")
		else:
			nextt.configure(state="normal")
			c1.configure(state="normal")
			c2.configure(state="normal")
			c3.configure(state="normal")
			c4.configure(state="normal")
			comment.configure(text="Valid")	
			root.geometry(f"{255}x{140}")
		return
	
	def string( ) -> None:
		if(c1.get()==""):
			cha1 = "."
		else:
			cha1 = c1.get( )
		
		if(c2.get()==""):
			cha2 = "."
		else:
			cha2 = c2.get( )
		
		if(c3.get()==""):
			cha3 = "."
		else:
			cha3 = c3.get( )
		
		if(c4.get()==""):
			cha4 = "."
		else:
			cha4 = c4.get( )
		
		if(c5.get()==""):
			cha5 = "."
		else:
			cha5 = c5.get( )
		
		global global_str
		global_str = cha1+cha2+cha3+cha4+cha5
		global_str = global_str.upper( )
		yellowTile(green_tile_frame)

	hide_show("green_tile_frame")
	frm.grid_forget( )
	root.geometry(f"{255}x{140}")
	nextt.configure(command=lambda: [string( ),check( )])
	# nextt.configure(command=lambda: yellowTile(green_tile_frame))

	# Different lables on the screen
	enter1 = CTkLabel(master=green_tile_frame, text="Type in the green tile letters in their positions")
	enter2 = CTkLabel(master=green_tile_frame, text="Leave the remaining blank")
	comment = CTkLabel(master=green_tile_frame, text="[1 Block = 1 Char]")

	# The values that we input in the 5 entry boxes
	ch1 = StringVar( )
	ch2 = StringVar( )
	ch3 = StringVar( )
	ch4 = StringVar( )
	ch5 = StringVar( )
	ch1.trace_variable("w", check1)
	ch2.trace_variable("w", check2)
	ch3.trace_variable("w", check3)
	ch4.trace_variable("w", check4)
	ch5.trace_variable("w", check5)
	
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
	c1.grid(row=3,column=0,ipadx=3,sticky="ew")
	c2.grid(row=3,column=1,ipadx=3,sticky="ew")
	c3.grid(row=3,column=2,ipadx=3,sticky="ew")
	c4.grid(row=3,column=3,ipadx=3,sticky="ew")
	c5.grid(row=3,column=4,ipadx=3,sticky="ew")
	green_tile_frame.grid(row=0, column=0, columnspan=3) # columnspan for the next button
	return

# Checks for words that are similar to the globat str
def check( ) -> None:

	global possible_words, global_str
	temp = []
	print(f"{global_str=}")
	for i in possible_words:
		for j in range(5):
			if(global_str[j]!='.') and (global_str[j]!=i[j]):
				temp.append(i)

	possible_words = subtract(main_list=possible_words, small_list=temp)
	print(f"{possible_words=}")				

# Everything in the yellow tile frame
def yellowTile(frm: CTkFrame) -> None:

	def check1(cha1, index, mode) -> None:
		
		cha1 = ch1.get()
		
		if(not cha1.isalpha( )) and (cha1!=""):
			nextt.configure(state="disabled")
			c2.configure(state="disabled")
			c3.configure(state="disabled")
			c4.configure(state="disabled")
			c5.configure(state="disabled")
			enter3.configure(text="[ONLY ENGLISH ALPHABETS]")
		else:
			nextt.configure(state="normal")
			c2.configure(state="normal")
			c3.configure(state="normal")
			c4.configure(state="normal")
			c5.configure(state="normal")
			enter3.configure(text="Valid")
	def check2(cha2, index, mode) -> None:
		
		cha2 = ch2.get()
		
		if(not cha2.isalpha( )) and (cha2!=""):
			nextt.configure(state="disabled")
			c1.configure(state="disabled")
			c3.configure(state="disabled")
			c4.configure(state="disabled")
			c5.configure(state="disabled")
			enter3.configure(text="[ONLY ENGLISH ALPHABETS]")
		else:
			nextt.configure(state="normal")
			c1.configure(state="normal")
			c3.configure(state="normal")
			c4.configure(state="normal")
			c5.configure(state="normal")
			enter3.configure(text="Valid")
	def check3(cha3, index, mode) -> None:
		
		cha3 = ch3.get()
		
		if(not cha3.isalpha( )) and (cha3!=""):
			nextt.configure(state="disabled")
			c1.configure(state="disabled")
			c2.configure(state="disabled")
			c4.configure(state="disabled")
			c5.configure(state="disabled")
			enter3.configure(text="[ONLY ENGLISH ALPHABETS]")
		else:
			nextt.configure(state="normal")
			c1.configure(state="normal")
			c2.configure(state="normal")
			c4.configure(state="normal")
			c5.configure(state="normal")
			enter3.configure(text="Valid")
	def check4(cha4, index, mode) -> None:
		
		cha4 = ch4.get()
		
		if(not cha4.isalpha( )) and (cha4!=""):
			nextt.configure(state="disabled")
			c1.configure(state="disabled")
			c2.configure(state="disabled")
			c3.configure(state="disabled")
			c5.configure(state="disabled")
			enter3.configure(text="[ONLY ENGLISH ALPHABETS]")
		else:
			nextt.configure(state="normal")
			c1.configure(state="normal")
			c2.configure(state="normal")
			c3.configure(state="normal")
			c5.configure(state="normal")
			enter3.configure(text="Valid")
	def check5(cha5, index, mode) -> None:
		
		cha5 = ch5.get()
		
		if(not cha5.isalpha( )) and (cha5!=""):
			nextt.configure(state="disabled")
			c1.configure(state="disabled")
			c2.configure(state="disabled")
			c3.configure(state="disabled")
			c4.configure(state="disabled")
			enter3.configure(text="[ONLY ENGLISH ALPHABETS]")
		else:
			nextt.configure(state="normal")
			c1.configure(state="normal")
			c2.configure(state="normal")
			c3.configure(state="normal")
			c4.configure(state="normal")
			enter3.configure(text="Valid")
	
	def array( ) -> None:
		if(c1.get()==""):
			cha1 = "."
		else:
			cha1 = c1.get( ).upper( )
		
		if(c2.get()==""):
			cha2 = "."
		else:
			cha2 = c2.get( ).upper( )
		
		if(c3.get()==""):
			cha3 = "."
		else:
			cha3 = c3.get( ).upper( )
		
		if(c4.get()==""):
			cha4 = "."
		else:
			cha4 = c4.get( ).upper( )
		
		if(c5.get()==""):
			cha5 = "."
		else:
			cha5 = c5.get( ).upper( )
		
		list_of_chr = [cha1,cha2,cha3,cha4,cha5]
		loadingScreen(yellow_tile_frame,list_of_chr)

	hide_show("yellow_tile_frame")
	frm.grid_forget( )
	root.geometry(f"{230}x{144}")
	nextt.configure(command=array)

	enter1 = CTkLabel(master=yellow_tile_frame, text="Enter the yellow tile letter(s) respectively")
	enter2 = CTkLabel(master=yellow_tile_frame, text="Eg: if 'M','E' are yellow at the 3rd position\nthen you put those in the 3rd entry")
	enter3 = CTkLabel(master=yellow_tile_frame, text="")

	# The values that we input in the 5 entry boxes
	ch1 = StringVar( )
	ch2 = StringVar( )
	ch3 = StringVar( )
	ch4 = StringVar( )
	ch5 = StringVar( )
	ch1.trace_variable("w", check1)
	ch2.trace_variable("w", check2)
	ch3.trace_variable("w", check3)
	ch4.trace_variable("w", check4)
	ch5.trace_variable("w", check5)
	
	# The 5 entry boxes 
	c1 = CTkEntry(master=yellow_tile_frame, width=25, justify=CENTER, textvariable=ch1)
	c2 = CTkEntry(master=yellow_tile_frame, width=25, justify=CENTER, textvariable=ch2)
	c3 = CTkEntry(master=yellow_tile_frame, width=25, justify=CENTER, textvariable=ch3)
	c4 = CTkEntry(master=yellow_tile_frame, width=25, justify=CENTER, textvariable=ch4)
	c5 = CTkEntry(master=yellow_tile_frame, width=25, justify=CENTER, textvariable=ch5)

	# Placing everything using grid( )
	enter1.grid(row=0, column=0, columnspan=5)
	enter2.grid(row=1, column=0, columnspan=5)
	enter3.grid(row=2, column=0, columnspan=5)
	c1.grid(row=3,column=0,ipadx=3,sticky="ew")
	c2.grid(row=3,column=1,ipadx=3,sticky="ew")
	c3.grid(row=3,column=2,ipadx=3,sticky="ew")
	c4.grid(row=3,column=3,ipadx=3,sticky="ew")
	c5.grid(row=3,column=4,ipadx=3,sticky="ew")
	yellow_tile_frame.grid(row=0, column=0, columnspan=3)
	return

# Frame containing the progress bar
def loadingScreen(frm: CTkFrame, list_of_chr: list):

	global possible_words
	hide_show("loading_frame")
	frm.grid_forget( )

	temp = []
	progress = CTkProgressBar(master=loading_frame, mode="determinate", height=20, corner_radius=0, progress_color="green")
	progress.grid(row=0, column=0, columnspan=2, padx=10, pady=20)
	# step = 100/len(possible_words)
	
	for i in possible_words:
		if(i[0] in list_of_chr[0]) or (i[1] in list_of_chr[1]) or (i[2] in list_of_chr[2]) or (i[3] in list_of_chr[3]) or (i[4] in list_of_chr[4]):
			temp.append(i)
	possible_words = subtract(main_list=possible_words, small_list=temp)
	
	loading_frame.grid(row=0, column=0, sticky="eswn")

start(hide_frame)

root.mainloop( )
