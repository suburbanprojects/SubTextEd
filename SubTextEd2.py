import tkinter as tk
from tkinter import font, colorchooser, filedialog, messagebox, ttk

#put program frame here
app = tk.Tk()
app.title("SubTextEd")
app.geometry("650x650")

#Menu Functions Go here
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

#####Put menus here####
menubar = tk.Menu(app)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open File", command=openFile)
filemenu.add_command(label="New File", command=newFile)
filemenu.add_command(label="Save File", command=onSave)
filemenu.add_command(label="Exit", command=app.quit)

menubar.add_cascade(label="File", menu=filemenu)
app.config(menu=menubar)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=lambda:showText.event_generate("<Control x>"))
editmenu.add_command(label="Copy", command=lambda:showText.event_generate("<Control c>"))
editmenu.add_command(label="Paste", command=lambda:showText.event_generate("<Control v>"))
editmenu.add_command(label="Clear All", command=lambda:showText.delete(1.0,tk.END))

menubar.add_cascade(label="Edit", menu=editmenu)
app.config(menu=menubar)

###### toolbar starts here ######
tool_bar = ttk.Label(app)
tool_bar.pack(side=tk.TOP, fill=tk.X)

### select font here ###
font_listing = tk.font.families()
font_names = tk.StringVar()
font_box=ttk.Combobox(tool_bar, width=30, textvariable=font_names,state='readonly')
font_box['values']=font_listing
font_box.current(font_listing.index('Arial'))
font_box.grid(row=0,column=0, padx=5)

#text size here
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, width=15, textvariable = size_var, state='readonly')
font_size['values']=tuple(range(8,80,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

#bold button
bold_button = ttk.Button(tool_bar, text="Bold")
bold_button.grid(row=0, column=2, padx=5)

#italic button
italic_button = ttk.Button(tool_bar, text="Italic")
italic_button.grid(row=0, column=3, padx=5)

#underline button
underline_button = ttk.Button(tool_bar, text="Underline")
underline_button.grid(row=0, column=4, padx=5)

#put font functions here
current_font_family = 'Calibri'
current_font_size = 12

def change_font(event=None):
    global current_font_family
    current_font_family = font_names.get()
    showText.config(font=(current_font_family, current_font_size))

def change_size(event=None):
    global current_font_size
    current_font_size = size_var.get()
    showText.config(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_size)

### button functions go here ###
#bold function
def change_bold():
    text_property=tk.font.Font(font=showText['font'])
    if text_property.actual()['weight']=='normal':
        showText.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        showText.configure(font=(current_font_family,current_font_size,'normal'))

bold_button.configure(command=change_bold)

#italic function
def change_italic():
    text_property=tk.font.Font(font=showText['font'])
    if text_property.actual()['slant'] == 'roman':
        showText.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant'] == 'italic':
        showText.configure(font=(current_font_family,current_font_size,'normal'))

italic_button.configure(command=change_italic)

#underline function
def change_underline():
    text_property=tk.font.Font(font=showText['font'])
    if text_property.actual()['underline'] == 0:
        showText.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline'] == 1:
        showText.configure(font=(current_font_family,current_font_size,'normal'))

underline_button.configure(command=change_underline)
    
#put text box here
showText = tk.Text(app, height=37, width=75)
showText.pack()

app.mainloop()
