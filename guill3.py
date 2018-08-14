from Tkinter import *
import os
import tkinter.messagebox
from tkFileDialog import *

def newfile():
    textbox.delete('1.0', END)

def save_as():
     f = asksaveasfile(mode='w', defaultextension=".txt")
     if f is None:
          return
     text=textbox.get(1.0, END)
     f.write(text)
     f.close()
     tkinter.messagebox.showinfo('Saved','Your File has been saved...')

def exitsc():
    root.destroy()

def openfile():
    f = askopenfilename(filetypes=(("Text Files","*.txt"),("All files","*.*")))
    if f is None:
        return
    filenm = open(f,'r')
    i=1.0
    for line in filenm:
        textbox.insert(i, line)
        i=i+1
    filenm.close()

root = Tk()

topframe = Frame(root)
bottomframe = Frame(root)

textbox = Text(bottomframe, height=38, width=80)
topframe.pack()
bottomframe.pack(side=BOTTOM)
textbox.grid(row=0)

savebutton = Button(topframe, text="Save File", command=save_as)
savebutton.grid(row=0,column=3,padx=2)

newbutton = Button(topframe, text="New File", command=newfile)
newbutton.grid(row=0,column=1,padx=2)

openbutton = Button(topframe, text="Open File", command=openfile)
openbutton.grid(row=0,padx=2)

exitbutton = Button(topframe, text="Exit", command=exitsc)
exitbutton.grid(row=0,column=4,padx=2)

root.mainloop()
