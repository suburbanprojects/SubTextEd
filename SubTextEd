import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox 

filename = '' #set variable

app = tk.Tk()
app.title("SubTextEd")
app.geometry("500x495")

def openFile():
    global filename #ensure the variable is accessed
    filename = filedialog.askopenfilename(initialdir="/",title="Dialog Box",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files","*.*")))     # take file location and file type
    if filename:
        open_file = open(filename)
        showText.delete("1.0","end") #clear the text field if there is an open file
        showText.insert(tk.END, open_file.read())
        open_file.close()
    elif filename == '':
        messagebox.showinfo("Error","No File Opened")

def onSave():
    global filename
    filename = filedialog.asksaveasfile(mode='w', defaultextension = '.txt',
                                        initialdir="/",
                                        title="Save As",
                                        filetypes=(("text files", "*.txt"),
                                                          ("all files","*.*"))) 
    if filename:
        text_get = showText.get('1.0', 'end-1c')
        filename.write(text_get)
        filename.close()
    else:
        messagebox.showinfo("Error", "Cancelled")
        
def newFile():
    showText.delete("1.0","end") #clear the text field if there is an open file

#put menu here
menubar = tk.Menu(app)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open File", command=openFile)
filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Save File", command=onSave)
filemenu.add_command(label="Exit", command=app.quit)

menubar.add_cascade(label="File", menu=filemenu)
app.config(menu=menubar)

#put text box here
showText = tk.Text(app, height=28, width=60)
showText.pack()

app.mainloop()
