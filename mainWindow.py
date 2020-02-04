from tkinter import *


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Carpentry Business Management")
        self.master.geometry("1200x800")
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

        self.placeOrderBtn.pack()
        self.frameLeft.pack(fill=Y, side=LEFT)
        self.employee_id_lbl.grid(row=1, column=1, padx=(100, 100))
        self.completeTransactionBtn.grid(row=2, column=1, padx=(100, 100))
        self.frameMiddle.pack(fill=Y, side=LEFT)
        self.paystubBtn.grid(row=1, column=1, padx=(100, 100))
        self.frameRight.pack(fill=Y, side=LEFT)

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
