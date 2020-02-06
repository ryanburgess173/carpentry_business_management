from tkinter import *


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Carpentry Business Management")
        self.mainMenuBar = Menu(self.master)
        self.fileMenu = Menu(self.mainMenuBar, tearoff=0)
        self.fileMenu.add_command(label="About", command=None)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=None)
        self.mainMenuBar.add_cascade(label="File", menu=self.fileMenu)
        self.master.config(menu=self.mainMenuBar)

        self.frameLeft = Frame(self.master, bg='cyan')
        self.placeOrderBtn = Button(self.frameLeft, text="Place Order")

        self.frameMiddle = Frame(
            self.master, bg='yellow', relief=RAISED, borderwidth=1)
        self.employee_id_lbl = Label(self.frameMiddle, text="Employee ID #:")

        self.completeTransactionBtn = Button(
            self.frameMiddle, text="Complete Transaction")

        self.frameRight = Frame(self.master, bg='salmon',
                                relief=RAISED, borderwidth=1)
        self.paystubBtn = Button(self.frameRight, text="Complete Paystub")

        self.placeOrderBtn.grid(
            row=1, column=1, padx=(100, 100), pady=(10, 10))
        self.frameLeft.pack(fill=Y, side=LEFT)
        self.employee_id_lbl.grid(
            row=1, column=1, padx=(100, 100), pady=(10, 10))
        self.completeTransactionBtn.grid(
            row=2, column=1, padx=(100, 100), pady=(10, 10))
        self.frameMiddle.pack(fill=Y, side=LEFT)
        self.paystubBtn.grid(row=1, column=1, padx=(100, 100), pady=(10, 10))
        self.frameRight.pack(fill=Y, side=LEFT)

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
