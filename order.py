#****************importing required modules****************
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector as connector
import pandas

#****************user-defined functions****************
def showbillform():
    def loaditemsinitemscombo():
        mydb = connector.connect(host="localhost", user="root", passwd="root", database="food_chain")
        mycursor = mydb.cursor()
        mycursor.execute('Select itemname from itemsmaster')
        result = mycursor.fetchall()
        DF = pandas.DataFrame(result, columns=['itemname'])
        return list(DF['itemname'])

    def setselecteditem(event):
        txtselecteditem.delete(0, END)
        txtselecteditem.insert(0, itemscombo.get())

        mydb = connector.connect(host="localhost", user="root", passwd="root", database="food_chain")
        mycursor = mydb.cursor()
        mycursor.execute("Select rate from itemsmaster where itemname = '{}'".format(txtselecteditem.get()))
        result = mycursor.fetchall()
        DF = pandas.DataFrame(result, columns=['rate'])
        txtrate.delete(0, END)
        txtrate.insert(0, list(DF['rate']))

    def calculateitemamount():
        rate = int(txtrate.get())
        qty = int(qtyspin.get())
        amount = rate * qty
        txtamt.delete(0, END)
        txtamt.insert(0, amount)

    def additemdatatobill():
        txtdata.config(state='normal')
        item = txtselecteditem.get()
        rate = txtrate.get()
        qty = qtyspin.get()
        amount = txtamt.get()
        txtdata.insert(INSERT, item + '\t\t' + rate + '\t\t' + qty + '\t\t' + amount + '\n\n')
        txtdata.config(state='disabled')
        grandtotal = int(txtgrandtotal.get()) + int(txtamt.get())
        txtgrandtotal.delete(0, END)
        txtgrandtotal.insert(0, grandtotal)


    def savebill():
        billdate = txtbilldate.get()
        name = txtname.get()
        billdescription = txtdata.get(1.0, END)
        grandtotal = txtgrandtotal.get()
        mydb = connector.connect(host="localhost", user="root", passwd="root", database="food_chain")
        mycursor = mydb.cursor()
        q = "insert into bill values({},'{}','{}','{}',{})"
        q = q.format(c, billdate, name, billdescription, grandtotal)
        mycursor.execute(q)
        mydb.commit()
        tkinter.messagebox.showinfo('Information', 'Order Received!')
        mainwindow.destroy()

    # ****************************************** Window Layout ****************************************
    mainwindow = Tk()
    mainwindow.title('Order Food')
    mainwindow.geometry('800x640')

    headinglabel = Label(mainwindow, text="Generate Bill", font='times 24 bold underline')
    selectlabel = Label(mainwindow, text="Select Item", font='times 12 bold')
    txtdata = Text(mainwindow, width=70, height=12)
    txtdata.insert(INSERT, 'Item Name' + '\t\t' + 'Rate' + '\t\t' + 'Qty' + '\t\t' + 'Amount' + '\n\n')
    txtselecteditem = Entry(mainwindow, width=25)
    ratelabel = Label(mainwindow, text="Rate", font='times 12 bold')
    qtylabel = Label(mainwindow, text = 'Quantity', font = 'times 12 bold')
    qtyspin = Spinbox(mainwindow, from_=0,to = 50)
    amountlabel = Label(mainwindow, text="Amount", font='times 12 bold')
    txtrate = Entry(mainwindow)
    txtamt = Entry(mainwindow)
    btncalculate = Button(mainwindow, text='Calculate', command=calculateitemamount)
    btnaddtobill = Button(mainwindow, text='Add Selected Item To Bill', width=40, font='times 14 bold',
                          command=additemdatatobill)
    btnsavebill = Button(mainwindow, text='Order Food', font='times 14 bold', width=20, command=savebill)
    grandtotallabel = Label(mainwindow, text="Grand Total", font='times 12 bold')
    txtgrandtotal = Entry(mainwindow)

    mydb = connector.connect(host="localhost", user="root", passwd="root", database="food_chain")
    mycursor = mydb.cursor()
    a = "select * from bill"
    mycursor.execute(a)
    b = mycursor.fetchall()
    DF = pandas.DataFrame(b, columns=['billno', 'billdate', 'name', 'billdescription', 'grandtotal'])
    c = max(DF['billno'])
    c = c + 1
    billnolabel = Label(mainwindow, text=('Bill No:',c), font='times 12 bold')
    itemscombo = ttk.Combobox(mainwindow, values=loaditemsinitemscombo(), width=25, state='readonly')
    itemscombo.current(0)
    itemscombo.bind("<<ComboboxSelected>>", setselecteditem)
    billdatelabel = Label(mainwindow, text="Bill Date", font='times 12 bold')
    txtbilldate = Entry(mainwindow)
    namelabel = Label(mainwindow, text="Name Of Person", font='times 12 bold')
    txtname = Entry(mainwindow, width=50)

    headinglabel.place(x=300, y=15)
    selectlabel.place(x=50, y=80)
    txtdata.place(x=50, y=250)
    itemscombo.place(x=150, y=85)
    txtselecteditem.place(x=350, y=85)
    ratelabel.place(x=50, y=120)
    txtrate.place(x=100, y=125)
    qtylabel.place(x=250, y=120)
    qtyspin.place(x=320, y=125)
    amountlabel.place(x=450, y=120)
    txtamt.place(x=520, y=125)
    btncalculate.place(x=650, y=120)
    btnaddtobill.place(x=50, y=180)
    grandtotallabel.place(x=50, y=480)
    txtgrandtotal.place(x=150, y=485)
    txtgrandtotal.insert(0, 0)
    billnolabel.place(x=50, y=40)
    billdatelabel.place(x=400, y=485)
    txtbilldate.place(x=480, y=485)
    namelabel.place(x=50, y=520)
    txtname.place(x=200, y=525)
    btnsavebill.place(x=50, y=560)

    # **** Show Current Date in Bill Date Text Field *****

    mydb = connector.connect(host="localhost", user="root", passwd="root", database="food_chain")
    mycursor = mydb.cursor()
    mycursor.execute('Select curdate()')
    result = mycursor.fetchall()
    DF = pandas.DataFrame(result, columns=['Date'])
    txtbilldate.insert(0, list(DF['Date']))
    mydb.close()
    # ****************************************************

    mainwindow.mainloop()
