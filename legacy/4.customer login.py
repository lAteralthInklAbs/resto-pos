##goes into customer_pos
from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pymysql

class customer_login(object):
    def __init__(self, master):
        self.master = master
        self.admin_frame = tk.Frame(self.master)
        self.master.geometry('1100x600')

        titleLabel = Label(master, text="Customer Interface", font="Arial 40", fg="green")
        titleLabel.grid(row=0, column=0, columnspan=4, padx=(40, 0), pady=(10, 0))

        authLabel = Label(master, text="Authentication", font="Arial 30")
        authLabel.grid(row=1, column=2, padx=(50, 0), columnspan=2, pady=10)

        tablenumLabel = Label(master, text="Booked Table Number")
        tablenumLabel.grid(row=2, column=2, padx=20, pady=5)

        mobilenumLabel = Label(master, text="Mobile Number")
        mobilenumLabel.grid(row=3, column=2, padx=20, pady=5)

        self.tablenumEntry = Entry(master)
        self.tablenumEntry.grid(row=2, column=3, padx=20, pady=5)
        self.tableno = self.tablenumEntry.get()
        self.mobilenumEntry = Entry(master, show="*")
        self.mobilenumEntry.grid(row=3, column=3, padx=20, pady=5)
        self.mobileno = self.tablenumEntry.get()

        self.authenButton = Button(master, text="Authenticate", width=20, height=2)
        self.authenButton.grid(row=4, column=2, columnspan=2)

admin = tk.Tk()
app = customer_login(admin)
admin.mainloop()