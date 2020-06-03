from tkinter import *
import tkinter.messagebox
import mysql.connector as connector
from tkinter.simpledialog import askstring

def check_password():
    pswd = askstring('Password', 'Enter password', show='*')
    if pswd == '1234':
        def insertnewitem():
            mydb = connector.connect(host='localhost', user='root', password='root', database='food_chain')

            mycursor = mydb.cursor()

            itemno = txtitemno.get()
            itemname = txtitemname.get()
            itemrate = txtitemrate.get()
            qry = "insert into itemsmaster values({},'{}',{})".format(itemno, itemname, itemrate)
            mycursor.execute(qry)
            mydb.commit()
            mainwindow.destroy()
            tkinter.messagebox.showinfo('Information', 'Item Created Successfully!')
        mainwindow = Tk()
        mainwindow.geometry('800x500')

        headinglabel = Label(mainwindow, text="Item Creation form", font='times 24 bold underline')
        headinglabel.place(x=280, y=20)

        lblitemno = Label(mainwindow, text='Enter Item Number', font='times 15')
        lblitemname = Label(mainwindow, text='Enter Item Name', font='times 15')
        lblitemrate = Label(mainwindow, text='Enter Charges', font='times 15')

        txtitemno = Entry(mainwindow)
        txtitemname = Entry(mainwindow)
        txtitemrate = Entry(mainwindow)

        lblitemno.place(x=50, y=150)
        lblitemname.place(x=50, y=200)
        lblitemrate.place(x=50, y=250)

        txtitemno.place(x=250, y=155)
        txtitemname.place(x=250, y=205)
        txtitemrate.place(x=250, y=255)

        savebutton = Button(mainwindow, text='Save Item', width=30, command=insertnewitem)
        savebutton.place(x=50, y=305)
        mainwindow.title('Insert New Item')

        txtitemno.focus()
        mainwindow.mainloop()

    else:
        tkinter.messagebox.showinfo("Access Denied","Wrong Password!")





