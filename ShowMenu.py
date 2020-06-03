from tkinter import *
import mysql.connector as connector
import pandas


def ShowMenu():

    window = Tk()
    window.title('MENU')
    mydb = connector.connect(host = 'localhost', user = 'root', password = 'root', database = 'food_chain')
    mycursor = mydb.cursor()
    mycursor.execute('select itemname, rate from itemsmaster')
    itemname = mycursor.fetchall()
    DF = pandas.DataFrame(itemname, columns=['Itemname', 'Rate'])

    text = Text(window)
    text.place(x = 1, y = 1)
    text.insert(INSERT,'\t\tMENU\t\t\n')
    text.insert(INSERT, 'Item\t\t\t\tRate\n\n')
    for ri,rd in DF.iterrows():
        a = DF.loc[ri,'Itemname']
        b = DF.loc[ri, 'Rate']
        text.insert(INSERT, a)
        text.insert(INSERT, '\t\t\t\t')
        text.insert(INSERT, b)
        text.insert(INSERT, '\n\n')



    window.geometry('300x300')
    window.mainloop()