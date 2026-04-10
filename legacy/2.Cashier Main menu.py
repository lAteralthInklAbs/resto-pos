###goes in cashier_pos
from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pymysql


class cash_menu:
    def __init__(self, master):
#        self.master = master  code used when called after cashier login
#        self.admin_menu_frame = tk.Frame(self.master)
        self.master = master
        self.booking_display_frame = tk.Frame(self.master)
        self.master.geometry('600x600')
        self.bookingButton = Button(master, text="Customer \nRegistry Page", width=40, height=5,command=self.booking_menu)
        self.bookingButton.grid(row=0, column=2, padx=120, pady=20)

        self.ordersButton = Button(master, text="Orders", width=40, height=5,command=self.orders_menu)
        self.ordersButton.grid(row=1, column=2, padx=120, pady=20)

        self.statusButton = Button(master, text="Order Process Status", width=40, height=5,command=self.order_status_menu)
        self.statusButton.grid(row=2, column=2, padx=120, pady=20)

        self.paymentButton = Button(master, text="Payment", width=40, height=5,command=self.payment_menu)
        self.paymentButton.grid(row=3, column=2, padx=120, pady=20)

    def widget_clearer(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def cashier_booking_display(self):
        self.app = cash_booking_display(self.master)

    def booking_menu(self):
        self.widget_clearer()
        self.cashier_booking_display()

    def orders_menu_display(self):
        self.app = order_menu_display(self.master)

    def orders_menu(self):
        self.widget_clearer()
        self.orders_menu_display()

    def orders_status_display(self):
        self.app = order_status_display(self.master)

    def order_status_menu(self):
        self.widget_clearer()
        self.orders_status_display()

    def payments_menu_display(self):
        self.app = payment_menu_display(self.master)

    def payment_menu(self):
        self.widget_clearer()
        self.payments_menu_display()

class cash_booking_display():
    def __init__(self, master):
        self.master = master
        self.booking_display_frame = tk.Frame(self.master)
        self.master.geometry('1000x600')

        self.titleLabel = Label(master, text="Customer Registry Page", font="Arial 40", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(80, 0), pady=(10, 0))

        self.tableLabel = LabelFrame(master, text="Active Token Registry", font="Arial 20")
        self.tableLabel.grid(row=1, column=0, padx=(30, 0), columnspan=2, pady=10)
        self.bookingButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1,
                                                                                                             x=-2, y=2,
                                                                                                             anchor=NE)
        ##checking database

        #        conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
        #        curs=conn.cursor()
        #        curs.execute("select* from active_reigistry")

        self.trv = ttk.Treeview(self.tableLabel, columns=(0, 1, 2,3), height="8")
        self.style = ttk.Style(self.trv)
        self.style.configure('Treeview', rowheight=20)
        self.trv.heading('#0', text="Customer Reference Number")
        self.trv.heading('#1', text="Customer Registered Name(RCN)")
        self.trv.heading('#2', text="Registered Mobile Number(RMN)")
        self.trv.heading('#3', text="Assigined Table Number(RTN)")
        # self.clockLabel = Label(master, text="Clock", font="Arial 20", fg="red").grid(row=3, column=0,padx=(0, 0), pady=(20, 0))
        self.startcustguiButton = Button(master, text="Start Customer GUI", width=20, height=5).grid(row=3,
                                                                                                     column=0,
                                                                                                     padx=0,
                                                                                                     pady=20)
        self.startcustguiButton = Button(master, text="Generate Customer\n Reference Number", width=20,
                                         height=5).grid(row=4, column=0, padx=0, pady=20)
        self.startcustguiButton = Button(master, text="Assign\n Table Number", width=20, height=5).grid(row=3,
                                                                                                        column=1,
                                                                                                        padx=0,
                                                                                                        pady=20)
        self.startcustguiButton = Button(master, text="Update\n Table ", width=20, height=5).grid(row=4, column=1, padx=0, pady=20)
        self.trv.pack()

            # define number of columns
        # self.trv["columns"] = ()

    #        import customer_pos
    #  def customer_main_menu(self):

    #        self.newWindow = tk.Toplevel(self.master)
    #        self.app = cash_booking_display(self.newWindow)

#back button
    def widget_clearer(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def cashier_main_menu_display(self):
        self.app = cash_menu(self.master)

    def back_button(self):
        self.widget_clearer()
        self.cashier_main_menu_display()



class order_menu_display():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.titleLabel = Label(master, text="Orders Interface", font="Arial 40", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(40, 0), pady=(10, 0))
        self.bookingButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1, x=-2,y=2,anchor=NE)

#back button
    def widget_clearer(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def cashier_main_menu_display(self):
        self.app = cash_menu(self.master)

    def back_button(self):
        self.widget_clearer()
        self.cashier_main_menu_display()


class order_status_display():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.titleLabel = Label(master, text="Order Process Interface", font="Arial 40", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(40, 0), pady=(10, 0))
        self.bookingButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1, x=-2,y=2,anchor=NE)

#back button
    def widget_clearer(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def cashier_main_menu_display(self):
        self.app = cash_menu(self.master)

    def back_button(self):
        self.widget_clearer()
        self.cashier_main_menu_display()

class payment_menu_display():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.titleLabel = Label(master, text="Customer Interface", font="Arial 40", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(40, 0), pady=(10, 0))
        self.bookingButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1, x=-2,y=2,anchor=NE)
#back button
    def widget_clearer(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def cashier_main_menu_display(self):
        self.app = cash_menu(self.master)

    def back_button(self):
        self.widget_clearer()
        self.cashier_main_menu_display()

admin = tk.Tk()
app = cash_menu(admin)
admin.mainloop()