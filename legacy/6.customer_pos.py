from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pymysql

"""
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

        self.authenButton = Button(master, text="Authenticate", width=20, height=2, command=self.customer_Login())
        self.authenButton.grid(row=4, column=2, columnspan=2)
STILL TO MAKE CUSTOMER LOGIN CLASS/Func IF ALREADY registered; if registered customer enter token number and custref no.

if cust_ref no. == login__input_cust_ref and mob_no.==login__input_cust_ref
    then open customer menu
"""

class cust_registration():
    def __init__(self, master):
        self.master = master
        self.booking_entry_frame = tk.Frame(self.master)
        self.master.geometry('1100x600')
        self.titleLabel = Label(master, text="Customer Registration Page", font="Arial 40", fg="green")
        self.titleLabel.grid(row=0, column=4, columnspan=2, padx=(120, 0), pady=(10, 0))

        self.custnameLabel = Label(master, text="Customer Name",font="Arial 20")
        self.custnameLabel.grid(row=4, column=3, padx=0, pady=10)

        self.mobnumLabel = Label(master, text="Mobile Number",font="Arial 20")
        self.mobnumLabel.grid(row=5, column=3, padx=0, pady=00)

        self.custnameEntry = Entry(master)
        self.custnameEntry.grid(row=4, column=4, padx=0, pady=0)
        self.custname = self.custnameEntry

        self.mobnumEntry = Entry(master)
        self.mobnumEntry.grid(row=5, column=4, padx=0, pady=0)
        self.mobileno = self.mobnumEntry

        self.registerButton = Button(master,text="Register",font='Arial 20',width=30, height=3,command=self.customer_registration)
        self.registerButton.grid(row=6, column=4, padx=0, pady=0)

    def customer_registration(self):

        conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
        cursor = conn.cursor()
        cursor.execute("insert into active_cust_reg (cust_reg_nam,reg_mob_num) values(%s,%s)", (self.custname.get(), self.mobileno.get()))
        conn.commit()
        conn.close()
#        query = "select* from active_reigistry "
#        cursor.execute(query)
#        data = cursor.fetchall()
#        customer = False
#        for row in data:
#             customer = True
#        conn.close()
#        if customer:
#            print("Parameteres authenticated")
#        else:
#            print(data)
#       conn.commit()



    def customer_main_menu(self):

        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.titleLabel = Label(master, text="Customer Interface", font="Arial 40", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(40, 0), pady=(10, 0))
        self.frame.pack()

def cust_main():
    admin = tk.Tk()
    app = cust_registration(admin)
    admin.mainloop()

cust_main()