from tkinter import *
from tkinter import Button

#******importing required modules********
import Register
import Manager
import order
import ShowMenu

MainWindow = Tk()
MainWindow.title('Main Menu')
#**********adding background image***************
picture = PhotoImage(file = "C:\\Users\\Utsav Singh\\Desktop\\IP Project\\Pic.gif")
heading = Label(MainWindow, text = 'Welcome to XYZ', font = 'times 26 bold underline', image = picture)
heading.pack()

#**************creating buttons******************
btnOrderFood = Button(MainWindow, text = 'Order Food' ,width = 25, font = 'times 20 bold', activebackground = 'red', activeforeground = 'white',command = order.showbillform)
btnShowMenu = Button(MainWindow, text = 'Show Menu',width = 25, font = 'times 20 bold',activebackground = 'red', activeforeground = 'white', command = ShowMenu.ShowMenu)
btnRegisterMember = Button(MainWindow, text = 'Register Yourself as a member',width = 25, font = 'times 20 bold', activebackground = 'red', activeforeground ='white',command = Register.registerform,)
btnExit = Button(MainWindow, text = 'Exit',width = 25, font = 'times 20 bold', activebackground = 'red', activeforeground = 'white', command = MainWindow.destroy)
btnManager = Button(MainWindow, text = 'Admin', width = 10, font = 'times 15 bold', activebackground = 'red', activeforeground ='white', command = Manager.check_password)


#****************placing buttons on screen***************
btnOrderFood.place(x = 200, y = 100)
btnShowMenu.place(x = 200, y = 170)
btnRegisterMember.place (x = 200, y = 240)
btnExit.place(x = 200, y= 310)
btnManager.place (x = 650,y = 450)

#****************MainWindow Geometry****************
w = 800
h = 500
screenwidth = MainWindow.winfo_screenmmwidth()
screenheight = MainWindow.winfo_screenheight()
x = str(int(screenwidth/2 - w / 2))
y = str(int(screenheight/2 - h/2))
s = '800x500' + x + '+' + y
MainWindow.geometry(s)
MainWindow.resizable(width = False, height = True)

MainWindow.mainloop()