# Standard library

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import os
from contextlib import redirect_stdout


# Import main exe from `run.py`

from run import start_detection
from run import TPS_RANGE, MIN_IrIo, STRICT_IrIo


# Set up GUI & global vars

api_name = 'OsBp Detect v.1.1'
in_fast5 = ''
out_fast5 = ''
geom_x, geom_y = 300, 420
root = Tk()
root.title(api_name)
root.geometry('{}x{}'.format(geom_x, geom_y))


# Helper functions

def open_file():
	global in_fast5
	in_fast5 = filedialog.askopenfilename(initialdir='./', title='Load file', filetypes=[('Bulk FAST5 files', '.fast5')])
	
def save_file():
	global out_fast5
	out_fast5 = filedialog.asksaveasfilename(initialdir='./', title='Select file', defaultextension='.tsv')
	
def execute():
	start_idx, end_idx = e1.get(), e2.get()
	tmin, tmax, allI, minI = p1.get(), p2.get(), p3.get(), p4.get()

	# File error handling
	if in_fast5 == '':
		messagebox.showerror('Error', 'Please specify the input file')
	elif out_fast5 == '':
		messagebox.showerror('Error', 'Please specify the output file')
		
	# Channel error handling
	elif not start_idx.strip().isnumeric():
		messagebox.showerror('Error', 'Please specify a valid start channel index')
	elif not end_idx.strip().isnumeric():
		messagebox.showerror('Error', 'Please specify a valid end channel index')
		
	# Threshold error handling
	elif not tmin.strip().isnumeric():
		messagebox.showerror('Error', 'Please specify a valid min(time) threshold')
	elif not tmax.strip().isnumeric():
		messagebox.showerror('Error', 'Please specify a valid max(time) threshold')
	elif not allI.strip().replace('.', '').isnumeric():
		messagebox.showerror('Error', 'Please specify a valid all(Ir/Io) threshold')
	elif not minI.strip().replace('.', '').isnumeric():
		messagebox.showerror('Error', 'Please specify a valid min(Ir/Io) threshold')

	else:
		in_file = os.path.abspath(in_fast5)
		out_file = os.path.abspath(out_fast5)
		start_int, end_int = int(start_idx), int(end_idx)
		t_min, t_max = int(tmin), int(tmax)
		all_irio, min_irio = float(allI), float(minI)
		with open(out_file, 'w') as f:
			with redirect_stdout(f):
				print('  _   _   _   _   _   _   _   _   _   _  ')
				print(' / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ ')
				print('( O | s | B | p | D | e | t | e | c | t )')
				print(' \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \n')
				print('=============  Thresholds  =============')
				print('Event duration (in tps): {} - {}'.format(t_min, t_max))
				print('Lowest Ir/Io < {}'.format(min_irio))
				print('All Ir/Io < {}'.format(all_irio))
				print('========================================\n')
				start_detection(in_file, [i for i in range(start_int, end_int + 1)], duration=(t_min, t_max), min_thresh_i=min_irio, strict_thresh_i=all_irio)
				messagebox.showinfo(api_name, 'Analysis complete!')
				root.destroy()
		
		
# Main
	
Frame(root, height=10).grid(row=0)
Label(root, text='1. File I/O:', font=('Helvetica', 10, 'bold')).grid(row=1)
Button(root, text='Open Input File', command=open_file).grid(row=2, column=1, pady=4, sticky='nsew')
Frame(root, height=1).grid(row=3)
Button(root, text='Save Output File', command=save_file).grid(row=4, column=1, pady=4, sticky='nsew')

Frame(root, height=15).grid(row=5)
Frame(root, height=2, width=geom_x-150, bg='black').grid(row=6, column=1)
Frame(root, height=10).grid(row=7)

Label(root, text='2. Channels:', font=('Helvetica', 10, 'bold')).grid(row=8)
Label(root, text='Start').grid(row=9)
Label(root, text='End').grid(row=10)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=9, column=1)
e2.grid(row=10, column=1)

Frame(root, height=15).grid(row=11)
Frame(root, height=2, width=geom_x-150, bg='black').grid(row=12, column=1)
Frame(root, height=10).grid(row=13)

Label(root, text='3. Thresholds:', font=('Helvetica', 10, 'bold')).grid(row=14)
Label(root, text='min(time)').grid(row=15)
Label(root, text='max(time)').grid(row=16)
Label(root, text='all(Ir/Io)').grid(row=17)
Label(root, text='min(Ir/Io)').grid(row=18)
p1 = Entry(root, textvariable=StringVar(root, value='{}'.format(TPS_RANGE[0])))
p2 = Entry(root, textvariable=StringVar(root, value='{}'.format(TPS_RANGE[1])))
p3 = Entry(root, textvariable=StringVar(root, value='{}'.format(STRICT_IrIo)))
p4 = Entry(root, textvariable=StringVar(root, value='{}'.format(MIN_IrIo)))
p1.grid(row=15, column=1)
p2.grid(row=16, column=1)
p3.grid(row=17, column=1)
p4.grid(row=18, column=1)

Frame(root, height=15).grid(row=19)
Frame(root, height=2, width=geom_x-150, bg='black').grid(row=20, column=1)
Frame(root, height=10).grid(row=21)

Button(root, text='Run', command=execute, bg='green').grid(row=22, column=1, pady=4, sticky='nsew')

root.mainloop()
