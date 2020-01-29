from tkinter import END, Tk, StringVar, Label, E, Entry, Label, Listbox, Scrollbar, Button, messagebox
from db import Database

db = Database('reports.db')

def populate_list():
        details_list.delete(0, END)
        for row in db.fetch():
            details_list.insert(END, row)

def add_item():
    if class_text.get() == '' or classno_text.get() == '' or date_text.get() == '' or time_text.get() == '' or details_text.get() == '':  
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(class_text.get(), classno_text.get(), date_text.get(), time_text.get(), details_text.get())
    details_list.delete(0, END)
    details_list.insert(END, (class_text.get(), classno_text.get(), date_text.get(), time_text.get(), details_text.get()))
    populate_list()

def select_item(event):
    global selected_item
    index = details_list.curselection()[0]
    selected_item = details_list.get(index)
    
    entry_class.delete(0, END)
    entry_class.insert(END, selected_item[1])
    entry_classno.delete(0, END)
    entry_classno.insert(END, selected_item[2])
    entry_date.delete(0, END)
    entry_date.insert(END, selected_item[3])
    entry_time.delete(0, END)
    entry_time.insert(END, selected_item[4])
    entry_details.delete(0, END)
    entry_details.insert(END, selected_item[5])

def remove_item():
    db.remove(selected_item[0])
    populate_list()
    
def update_item():
    print("update") 

def clear_text():
    print("Clear")

app = Tk()


#titles
class_text = StringVar()
label_1 = Label(app, text = '班级:', font=(20), pady = 20)
label_1.grid(row=0, column=0, sticky=E)
entry_class = Entry(app, textvariable = class_text)
entry_class.grid(row=0, column=1)

classno_text = StringVar()
label_2 = Label(app, text = '课室编号:', font=(20), pady=20)
label_2.grid(row=1, column=0, sticky=E)
entry_classno = Entry(app, textvariable = classno_text)
entry_classno.grid(row=1, column=1)

date_text = StringVar()
label_3 = Label(app, text = '日期:', font=(20), pady=20)
label_3.grid(row=0, column=2, sticky=E)
entry_date = Entry(app, textvariable = date_text)
entry_date.grid(row=0, column=3)

time_text = StringVar()
label_4 = Label(app, text = '时间:', font=(20), pady=20)
label_4.grid(row=1, column=2, sticky=E)
entry_time = Entry(app, textvariable = time_text)
entry_time.grid(row=1, column=3)

details_text = StringVar()
label_5 = Label(app, text = '报备事项:', font=(20), pady=20)
label_5.grid(row=2, column=0, sticky=E)
entry_details = Entry(app, textvariable = details_text)
entry_details.grid(row=2, column=1)

#listbox
details_list = Listbox(app, height=8, width=100)
details_list.grid(row=4, column=0, columnspan=4, rowspan=6, pady=20, padx=20)

#scroll
scrollbar= Scrollbar(app)
scrollbar.grid(row=4, column=5)

#set scroll to listbox
details_list.configure(yscrollcommand= scrollbar.set)
scrollbar.configure(command=details_list.yview)

#bind select
details_list.bind('<<ListboxSelect>>', select_item)

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
