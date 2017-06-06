import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox
import os
import subprocess


current_file = open("input.sz", "r")
root = Tkinter.Tk(className=" Stochmize GUI")
textPad = ScrolledText(root, width=100, height=20)
outputPad = ScrolledText(root, width=100, height=10, background='lightblue')



# create a menu & define functions for each menu item
def open_command():
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
    if file != None:
    	current_file = file
        contents = file.read()
        textPad.insert('1.0',contents)
        file.close()

def save_command():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
    # slice off the last character from get, as an extra return is added
        data = textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()
        
def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def about_command():
    label = tkMessageBox.showinfo("About", "Stochmize is a parser for a language to describe stochastic optimization problems")

def new_file():
    print "Falta implementar"

def compile():
	p = subprocess.Popen([sys.executable, 'test_2.py', current_file.name, '--debug'], stdout=subprocess.PIPE)
	output = p.stdout.read()
	#result = subprocess.run(['python', 'compiler.py', current_file.name, '--debug'], stdout=subprocess.PIPE)
	#output = os.system('python compiler.py '+current_file.name+ " --debug")
	outputPad.insert('1.0', output)

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
helpmenu = Menu(menu)
menu.add_command(label="Compile", command=compile)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)
textPad.pack()
textPad.insert('1.0',current_file.read())
outputPad.pack()
root.mainloop()