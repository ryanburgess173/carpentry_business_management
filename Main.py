from tkinter import *
from createDBConnection import MySQLConnection
from mainWindow import MainWindow

root = Tk()
my_gui = MainWindow(root)
root.mainloop()
