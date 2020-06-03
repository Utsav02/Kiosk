from tkinter import *
import tkinter.messagebox
import mysql.connector as connector




def registerform():
    def newmember():
        mydb = connector.connect(host = 'localhost', user = 'root', password = 'root', database = 'Food_Chain')
        mycursor = mydb.cursor()

        firstname = txtfirstname.get()
        lastname = txtlastname.get()
        address = txtaddress.get()
        mobile = txtmobile.get()


        qry = "insert into memberdetails values('{}','{}','{}',{})".format(firstname, lastname,address, mobile)
        mycursor.execute(qry)
        mydb.commit()
        mainwindow.destroy()
        tkinter.messagebox.showinfo('Information', 'Registered Successfully')

    mainwindow = Tk()
    mainwindow.geometry('900x700')
    mainwindow.title("REGISTER")



    lblfirstname = Label(mainwindow, text='Enter your First Name', font='time 15')
    lbllastname = Label(mainwindow, text='Enter your Last Name', font='times 15')
    lbladdress = Label(mainwindow, text='Enter your Address', font='times 15')
    lblmobile = Label(mainwindow, text='Enter your phone number', font='times 15')

    txtfirstname =Entry(mainwindow)
    txtlastname = Entry(mainwindow)
    txtaddress = Entry(mainwindow)
    txtmobile =Entry(mainwindow)

    lblfirstname.place(x=50, y=150)
    lbllastname.place(x=50, y=200)
    lbladdress.place(x = 50, y = 250)
    lblmobile.place(x=50, y=300)

    txtfirstname.place(x=250, y=155)
    txtlastname.place(x=250, y=205)
    txtaddress.place(x = 250, y = 255)
    txtmobile.place(x=255, y=305)

    savebutton = Button(mainwindow, text='Save', font='times 15 bold', width=30, command = newmember)
    savebutton.place(x=50, y=400)

    txtfirstname.focus()
    mainwindow.mainloop()






