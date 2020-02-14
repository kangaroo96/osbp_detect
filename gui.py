# Standard library

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import os
from contextlib import redirect_stdout


# Import main exe from `run.py`

from run import start_detection


# Set up GUI & global vars

api_name = 'OsBp Detect'
in_fast5 = ''
out_fast5 = ''
root = Tk()
root.title(api_name)
root.geometry('300x300')


# Helper functions

def open_file():
	global in_fast5
	in_fast5 = filedialog.askopenfilename(initialdir='./', title='Load file', filetypes=[('Bulk FAST5 files', '.fast5')])
	
def save_file():
	global out_fast5
	out_fast5 = filedialog.asksaveasfilename(initialdir='./', title='Select file', defaultextension='.tsv')
	
def execute():
	start_idx, end_idx = e1.get(), e2.get()
	if in_fast5 == '':
		messagebox.showerror('Error', 'Please specify the input file')
	elif out_fast5 == '':
		messagebox.showerror('Error', 'Please specify the output file')
	elif start_idx == '' or not start_idx.isnumeric():
		messagebox.showerror('Error', 'Please specify a valid start channel index')
	elif end_idx == '' or not end_idx.isnumeric():
		messagebox.showerror('Error', 'Please specify a valid end channel index')
	else:
		in_file = os.path.abspath(in_fast5)
		out_file = os.path.abspath(out_fast5)
		start_int = int(start_idx)
		end_int = int(end_idx)
		with open(out_file, 'w') as f:
			with redirect_stdout(f):
				print('  _   _   _   _   _   _   _   _   _   _  ')
				print(' / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ ')
				print('( O | s | B | p | D | e | t | e | c | t )')
				print(' \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \n')
				start_detection(in_file, [i for i in range(start_int, end_int + 1)])
				messagebox.showinfo(api_name, 'Analysis complete!')
				root.destroy()
		
		
# Main
	
Label(root, text='').grid(row=0)
Button(root, text='Open Input File', command=open_file).grid(row=1, column=1, pady=4, sticky='nsew')
Label(root, text='').grid(row=2)
Button(root, text='Save Output File', command=save_file).grid(row=3, column=1, pady=4, sticky='nsew')

Label(root, text='').grid(row=4)
Label(root, text='Channels:').grid(row=5)
Label(root, text='Start').grid(row=6)
Label(root, text='End').grid(row=7)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=6, column=1)
e2.grid(row=7, column=1)

Label(root, text='').grid(row=8)
Button(root, text='Run', command=execute, bg='green').grid(row=9, column=1, pady=4, sticky='nsew')

root.mainloop()
