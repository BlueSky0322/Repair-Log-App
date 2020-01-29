from tkinter import END, Tk, StringVar, Label, E, Entry, Label
from tkinter import Listbox, Scrollbar, Button
from db import Database

db = Database('reports.db')

def populate_list():
    for row in db.fetch():
        details_list.insert(END, row)

def add_item():
    print("add")

def remove_item():
    print("remove")

def update_item():
    print("update") 

def clear_text():
    print("Clear")

app = Tk()


#titles
class_text = StringVar()
label_1 = Label(app, text = '班级:', font=(20), pady = 20)
label_1.grid(row=0, column=0, sticky=E)
entry_1 = Entry(app, textvariable = class_text)
entry_1.grid(row=0, column=1)

classno_text = StringVar()
label_2 = Label(app, text = '课室编号:', font=(20), pady=20)
label_2.grid(row=1, column=0, sticky=E)
entry_2 = Entry(app, textvariable = classno_text)
entry_2.grid(row=1, column=1)

date_text = StringVar()
label_1 = Label(app, text = '日期:', font=(20), pady=20)
label_1.grid(row=0, column=2, sticky=E)
entry_1 = Entry(app, textvariable = date_text)
entry_1.grid(row=0, column=3)

time_text = StringVar()
label_1 = Label(app, text = '时间:', font=(20), pady=20)
label_1.grid(row=1, column=2, sticky=E)
entry_1 = Entry(app, textvariable = time_text)
entry_1.grid(row=1, column=3)

details_text = StringVar()
label_1 = Label(app, text = '报备事项:', font=(20), pady=20)
label_1.grid(row=2, column=0, sticky=E)
entry_1 = Entry(app, textvariable = details_text)
entry_1.grid(row=2, column=1)

#listbox
details_list = Listbox(app, height=8, width=100)
details_list.grid(row=4, column=0, columnspan=4, rowspan=6, pady=20, padx=20)

#scroll
scrollbar= Scrollbar(app)
scrollbar.grid(row=4, column=5)

#set scroll to listbox
details_list.configure(yscrollcommand= scrollbar.set)
scrollbar.configure(command=details_list.yview)

#buttons
add_btn = Button(app, text = "Add Part", width=12, command=add_item)
add_btn.grid(row=3, column=0, pady=20)

remove_btn = Button(app, text = "Remove", width=12, command=remove_item)
remove_btn.grid(row=3, column=1)

update_btn = Button(app, text = "Update", width=12, command=update_item)
update_btn.grid(row=3, column=2)

clear_btn = Button(app, text = "Clear", width=12, command=clear_text)
clear_btn.grid(row=3, column=3)


app.title("Manager")
app.geometry('700x350')

#Populate list
populate_list()

app.mainloop()
