from tkinter import *
from db import Database 
from tkinter import messagebox

db = Database('store.db')

app = Tk()


def populate_list():
    bill_list.delete(0, END)
    for row in db.fetch():
        bill_list.insert(END, row)

    

def add_bill():
    if bill_title.get() == '' or bill_ammount.get() == '' or bill_notes.get()== '' or bill_date.get() == '':
        messagebox.showerror('Required Fields', 'Please fill out all the entry boxes')
        return

    db.insert(bill_title.get(),bill_ammount.get(),bill_notes.get(), bill_date.get())
    bill_list.delete(0, END)
    bill_list.insert(END, (bill_title.get(),bill_ammount.get(),bill_notes.get(), bill_date.get()))
    clear_text()
    populate_list()


def select_bill(event):
    try:   
        global selected_bill
        index = bill_list.curselection()[0]
        selected_bill = bill_list .get(index)

        bill_entry.delete (0, END)
        bill_entry.insert(END, selected_bill[1])

        bill_ammount_entry.delete (0, END)
        bill_ammount_entry.insert(END, selected_bill[2])

        bill_notes_entry.delete (0, END)
        bill_notes_entry.insert(END, selected_bill[3])

        bill_date_entry.delete (0, END)
        bill_date_entry.insert(END, selected_bill[4])
    except IndexError:
        pass

def remove_bill():
    db.remove(selected_bill[0])
    clear_text()
    populate_list()

def update_bill():

    db.update(selected_bill[0], bill_title.get(),bill_ammount.get(),bill_notes.get(), bill_date.get())

    populate_list()


def clear_text():
    bill_entry.delete (0, END)
    bill_ammount_entry.delete (0, END)
    bill_notes_entry.delete (0, END)
    bill_date_entry.delete (0, END)



def show_help():
    help_text = """
    This app helps you track your bills.

    - To add a bill, fill in the required fields (Bill title, Amount, Notes, Date) and click 'Add bill'.
    - To remove a bill, select it from the list and click 'Remove bill'.
    - To update a bill, select it from the list, make changes, and click 'Update bill'.
    - To clear input fields, click 'Clear input'.
    """
    help_popup = Toplevel()
    help_popup.title("Help")
    help_popup.geometry("500x300")

    help_label = Label(help_popup, text=help_text, justify=LEFT)
    help_label.pack(padx=10, pady=10)

    ok_button = Button(help_popup, text="OK", command=help_popup.destroy) 
    ok_button.pack(pady=10)

    

# Create labels and entry boxes for Title and price
bill_title = StringVar()
bill_label = Label(app, text='Bill title', font = ('bold', 16), pady = 20)
bill_label.grid(row = 0, column =0)

bill_entry = Entry(app, textvariable = bill_title)
bill_entry.grid(row = 0 , column= 1)

bill_ammount = StringVar()
bill_ammount_label = Label(app,text= 'ammount', font= ('bold', 16))
bill_ammount_label.grid(row = 1, column= 0)

bill_ammount_entry =Entry(app, textvariable = bill_ammount)
bill_ammount_entry.grid (row = 1, column = 1)


# Create StringVars for additional fields
bill_notes = StringVar()
bill_date = StringVar()

# Create labels and entry boxes for notes and dates
bill_notes_label = Label(app, text='Notes', font=('bold', 16) )
bill_notes_label.grid(row=0, column=3)
bill_notes_entry = Entry(app, textvariable=bill_notes)
bill_notes_entry.grid(row=0, column=4)

bill_date_label = Label(app, text='Date', font=('bold', 16))
bill_date_label.grid(row=1, column=3)
bill_date_entry = Entry(app, textvariable=bill_date)
bill_date_entry.grid(row=1, column=4)


bill_list = Listbox(app,height = 8, width = 50, border = 1)
bill_list.grid(row=3,column = 0, columnspan = 3, rowspan= 6, pady= 2, padx = 20 )

#create scrollbar 
scrollbar = Scrollbar(app)
scrollbar.grid(row = 3, column = 3)

#set scroll to listbox
bill_list.configure(yscrollcommand= scrollbar.set)
scrollbar.configure(command = bill_list.yview)

# bind select 

bill_list.bind('<<ListboxSelect>>', select_bill)


#Buttons 
add_btn = Button(app, text= "Add bill", width = 12, command = add_bill )
add_btn.grid(row = 2, column = 0 , pady = 20)

remove_btn = Button(app, text= "Remove bill", width = 12, command = remove_bill )
remove_btn.grid(row = 2, column = 1 )

update_btn = Button(app, text= "Update bill", width = 12, command = update_bill )
update_btn.grid(row = 2, column = 2 )

clear_btn = Button(app, text= "Clear input", width = 12, command = clear_text )
clear_btn.grid(row = 2, column = 3 )

# Help button
help_btn = Button(app, text="Help", bg="#1af041", fg="black", width=8, border = 2, command=show_help)
help_btn.grid(row=0, column=5, padx=10, pady=10, sticky="ne")





app.title('BillTrack Pro')
app.geometry('700x350')

#populate data
populate_list()



app.mainloop()

