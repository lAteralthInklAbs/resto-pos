###goes into customer_pos
from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pymysql


class cust_main_menu:
    def __init__(self, master):
        self.master = master
        self.admin_menu_frame = tk.Frame(self.master)

        self.bookingButton = Button(master, text="Menu", width=40, height=5,command=self.cust_order_menu)
        self.bookingButton.grid(row=0, column=2, padx=120, pady=20)

        self.ordersButton = Button(master, text="Order", width=40, height=5)
        self.ordersButton.grid(row=1, column=2, padx=120, pady=20)

        self.statusButton = Button(master, text="Status", width=40, height=5)
        self.statusButton.grid(row=2, column=2, padx=120, pady=20)

        self.paymentButton = Button(master, text="Payment", width=40, height=5)
        self.paymentButton.grid(row=3, column=2, padx=120, pady=20)

    def widget_clearer(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def customer_menu_display(self):
       self.app = customer_menu_display(self.master)

    def cust_order_menu(self):
        self.widget_clearer()
        self.customer_menu_display()



class customer_menu_display():
    def __init__(self, master):
        self.master = master
        self.booking_display_frame = tk.Frame(self.master)
        self.master.geometry('1000x600')

        self.titleLabel = Label(master, text="Menu of Cuisines", font="Arial 40", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(80, 0), pady=(10, 0))

        self.tableLabel = LabelFrame(master, text="Menu", font="Arial 20")
        self.tableLabel.grid(row=1, column=0, padx=(30, 0), columnspan=2, pady=10)

        ##checking database
#        conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
#        curs=conn.cursor()
#        curs.execute("select* from active_reigistry")

        self.trv =ttk.Treeview(self.tableLabel)
        self.style = ttk.Style(self.trv)
        #billsTV = ttk.Treeview(height=15, columns=('Rate', 'Quantity', 'Cost'))
        # scrollBar = Scrollbar(master, orient="vertical", command=self.trv.yview)
        # scrollBar.grid(row=5, column=0, sticky="NSE")
        # self.trv.configure(yscrollcommand=scrollBar.set)
        self.style.configure('Treeview',rowheight=20)
        self.trv.heading('#0', text="Index")
        self.trv.heading('#1', text="Item/Dish")
        self.trv.heading('#2', text="Type of Dish")
        self.trv.heading('#3', text="Price")
        self.trv.pack()
        #self.clockLabel = Label(master, text="Clock", font="Arial 20", fg="red").grid(row=3, column=0,padx=(0, 0), pady=(20, 0))
        self.startcustguiButton = Button(master, text="Refresh Menu", width=20, height=5).grid(row=3, column=0, padx=0, pady=20)
        self.startcustguiButton = Button(master, text="Open Particular Cuisine", width=20, height=5).grid(row=4, column=0, padx=0, pady=20)
        self.startcustguiButton = Button(master, text="Check Availability of Item\n(for Initial Order)", width=20, height=5).grid(row=3, column=1, padx=0, pady=20)
        self.startcustguiButton = Button(master, text="Create Initial Order", width=20, height=5).grid(row=4, column=1, padx=0, pady=20)
        self.bookingButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1,
                                                                                                             x=-2, y=2,
                                                                                                             anchor=NE)


    # back button
    def widget_clearer(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def cust_order_menu(self):
        self.app = cust_main_menu(self.master)

    def back_button(self):
        self.widget_clearer()
        self.cust_order_menu()
        #define number of columns
       # self.trv["columns"] = ()

#        import customer_pos
#  def customer_main_menu(self):

#        self.newWindow = tk.Toplevel(self.master)
#        self.app = cash_booking_display(self.newWindow)


admin = tk.Tk()
app = cust_main_menu(admin)
admin.mainloop()