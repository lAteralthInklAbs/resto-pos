# main file for project last edit March25th 6:30am
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import random
import pymysql

# from customerinfo
selected_cust = StringVar
bill_ReferenceID = StringVar
receipt_ID = StringVar


# admin page to start application
class cashier_authen:
    def __init__(self, master):
        self.master = master
        self.admin_frame = tk.Frame(self.master)
        self.master.geometry('400x300')
        self.titleLabel = Label(master, text="Cashier Interface", font="Arial 40", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(40, 0), pady=(10, 0))

        self.loginLabel = Label(master, text="Admin Login", font="Arial 30")
        self.loginLabel.grid(row=1, column=2, padx=(50, 0), columnspan=2, pady=10)

        self.usernameLabel = Label(master, text="Username")
        self.usernameLabel.grid(row=2, column=2, padx=20, pady=5)

        self.passwordLabel = Label(master, text="Password")
        self.passwordLabel.grid(row=3, column=2, padx=20, pady=5)

        self.usernameEntry = Entry(master)
        self.usernameEntry.grid(row=2, column=3, padx=20, pady=5)

        self.passwordEntry = Entry(master, show="*")
        self.passwordEntry.grid(row=3, column=3, padx=20, pady=5)

        self.loginButton = Button(master, text="Login", width=20, height=2, command=self.adminLogin)
        self.loginButton.grid(row=4, column=2, columnspan=2)

        # self.logout_button = Button(master, text="Logout", width=20, height=2, command=self.logout_button)
        # self.logout_button.grid(row=4, column=2, columnspan=2)

    def adminLogin(self):
        global usernameEntry
        global passwordEntry
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
        cursor = conn.cursor()

        query = "select* from users where username='{}' and password='{}'".format(username, password)
        cursor.execute(query)
        data = cursor.fetchall()
        admin = False
        for row in data:
            admin = True
        conn.close()
        if admin:
            self.widget_clearer()
            self.cashier_main_menu()
        else:
            messagebox.showerror("Invalid User", "Credentials entered are invalid")

    def cashier_main_menu(self):
        self.app = cash_menu(self.master)

    def widget_clearer(self):
        for widget in self.master.winfo_children():
            widget.destroy()


# class cash_menu:
#     def __init__(self, master):
# #        self.master = master  code used when called after cashier login
# #        self.admin_menu_frame = tk.Frame(self.master)
#         self.master = master
#         self.booking_display_frame = tk.Frame(self.master)
#         self.master.geometry('1000x600')
#         self.bookingButton = Button(master, text="Customer\nRegistration", width=40, height=5,command=self.booking_menu)
#         self.bookingButton.grid(row=0, column=2, padx=120, pady=20)
#
#         self.ordersButton = Button(master, text="Orders", width=40, height=5,command=self.orders_menu)
#         self.ordersButton.grid(row=1, column=2, padx=120, pady=20)
#
#         self.statusButton = Button(master, text="Order Process Status", width=40, height=5,command=self.order_status_menu)
#         self.statusButton.grid(row=2, column=2, padx=120, pady=20)
#
#         self.paymentButton = Button(master, text="Payment", width=40, height=5,command=self.payment_menu)
#         self.paymentButton.grid(row=3, column=2, padx=120, pady=20)
#
#     def widget_clearer(self):
#         for widget in self.master.winfo_children():
#             widget.destroy()
#
#     def cashier_booking_display(self):
#         self.app = cash_booking_display(self.master)
#
#     def booking_menu(self):
#         self.widget_clearer()
#         self.cashier_booking_display()
#
#     def orders_menu_display(self):
#         self.app = order_menu_display(self.master)
#
#     def orders_menu(self):
#         self.widget_clearer()
#         self.orders_menu_display()
#
#     def orders_status_display(self):
#         self.app = order_status_display(self.master)
#
#     def order_status_menu(self):
#         self.widget_clearer()
#         self.orders_status_display()
#
#     def payments_menu_display(self):
#         self.app = payment_menu_display(self.master)
#
#     def payment_menu(self):
#         self.widget_clearer()
#         self.payments_menu_display()
#
#
# """
#         self.custname = StringVar()
#         self.mobileno = StringVar()
#         self.tableno = StringVar()
#
#     def table_content_status(self):
#         conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
#         cursor = conn.cursor()
#         query = "select* from active_reigistry where cust_name='{}' and mobileno='{}' and assi_no={}".format(self.custname, self.mobileno, self.tableno)
#         cursor.execute(query)
#         data = cursor.fetchall()
#         customer = False
#         for row in data:
#             customer = True
#         conn.close()
#         if not customer:
#
#         else:
#             messagebox.showerror("Invalid User", "Credentials entered are invalid")
#
#
# """

class cash_menu:
    def __init__(self, master):
        #        self.master = master  code used when called after cashier login
        #        self.admin_menu_frame = tk.Frame(self.master)
        self.master = master
        self.booking_display_frame = tk.Frame(self.master)
        self.master.geometry('450x450')
        self.master.title("Main Interface Menu")
        self.bookingButton = Button(master, text="Add \nCustomer", width=20, height=5, command=self.booking_menu)
        self.bookingButton.grid(row=0, column=2, padx=120, pady=20)

        self.MenuButton = Button(master, text="Menu", width=20, height=5, command=self.menu)
        self.MenuButton.grid(row=1, column=2, padx=120, pady=20)

        # self.statusButton = Button(master, text="Order Process Status", width=40, height=5,command=self.order_status_menu)
        # self.statusButton.grid(row=2, column=2, padx=120, pady=20)

        self.paymentButton = Button(master, text="Payment", width=20, height=5, command=self.payment_menu)
        self.paymentButton.grid(row=3, column=2, padx=120, pady=20)

        self.logout_button = Button(master, text="Logout", width=5, height=2, command=self.logout_cashier)
        self.logout_button.place(relx=1, x=-2, y=2, anchor=NE)

    # admin page
    def logout_cashier(self):
        self.widget_clearer()
        self.app = cashier_authen(self.master)

    def widget_clearer(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    # interface for customer info entry
    def cashier_booking_display(self):
        self.app = cash_booking_display(self.master)

    def booking_menu(self):
        self.widget_clearer()
        self.cashier_booking_display()

    # menu interface for customer
    def menu_display(self):
        self.app = menu_display(self.master)

    def menu(self):
        self.widget_clearer()
        self.menu_display()

    # def orders_status_display(self):
    #     self.app = order_status_display(self.master)

    # def order_status_menu(self):
    #     self.widget_clearer()
    #     self.orders_status_display()
    # payments display page
    def payments_menu_display(self):
        self.app = payment_menu_display(self.master)

    def payment_menu(self):
        self.widget_clearer()
        self.payments_menu_display()


# Customer details entry and checking
class cash_booking_display():
    def __init__(self, master):
        # initalisiations to frame
        self.master = master
        self.booking_display_frame = tk.Frame(self.master)
        self.master.geometry('600x500')
        self.master.title("Customer Registry")

        self.titleLabel = Label(master, text="Customer Details Table", font="Arial 30", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=3, padx=(0, 0), pady=(0, 0))
        # conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
        # cursor = conn.cursor()
        # query1 = "TRUNCATE TABLE CustomerInfo"
        # cursor.execute(query1)
        # query2 = "insert into CustomerInfo (customerName, customerRefID) values('{}','{}')".format(custName,custRefID)
        # cursor.execute(query2)

        # # self.tableLabel = LabelFrame(master, text="Active Customer Registry", font="Arial 20")
        # # self.tableLabel.grid(row=1, column=0, padx=(30, 0), columnspan=2, pady=10)
        self.backButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1, x=-2,
                                                                                                          y=2,
                                                                                                          anchor=NE)
        # self.backButton = Button(master, text="Refresh \nDatabase Table", width=10, height=2, command=lambda:refresh_customer_table()).place(x=600,y=100,anchor=NE)

        # customer name details(left)
        self.trv = ttk.Treeview(height=9, selectmode='extended')
        self.trv['columns'] = ("Index", "Customer Name", "Customer Reference ID")
        self.trv.column("#0", width=0, stretch=NO)
        self.trv.column("Index", anchor=W, width=40)
        self.trv.column("Customer Name", anchor=W, width=180)
        self.trv.column("Customer Reference ID", anchor=W, width=180)
        self.trv.grid(row=1, column=0, padx=(60, 0), pady=10)

        # self.scrollBar = Scrollbar(self.master, orient="vertical")
        # self.scrollBar.grid(row=1, column=1, sticky="NSE")
        # self.scrollBar.config(command=self.trv.yview)
        # self.trv.configure(yscrollcommand=self.scrollBar.set)
        self.trv.heading('#0')
        self.trv.heading('#1', text="Index")
        self.trv.heading('#2', text="Customer Name")
        self.trv.heading('#3', text="Customer Reference ID")
        # CUSTOMER ENTRY WIDGET
        self.cust_entrylabel = Label(master, text="Enter Customer Name:", font="Arial 20", fg="green")
        self.cust_entrylabel.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.customer_name_entry = Entry(master, font=('calibre', 15, 'bold'), bg='red', width=20)
        self.customer_name_entry.grid(row=3, column=0, padx=0, pady=0)
        # self.time_entrylabel = Label(master, text="Enter Customer Entry Time:", font="Arial 20", fg="green")
        # self.time_entrylabel.grid(row=4, column=1, padx=(0, 0), pady=(0, 0))
        # self.customer_time_entry = Entry(master, font=('calibre', 15, 'bold'), bg='red', width=20)
        # self.customer_time_entry.grid(row=5, column=1, padx=30, pady=0)

        # Customer Review Buttons For next page
        self.open_cust_menu_Button = Button(master, text="Open Customer Menu", width=15, height=2,
                                            command=lambda: self.menu()).grid(row=5, column=0,
                                                                              padx=0, pady=0)
        self.confirm_selection_Button = Button(master, text="Confirm\nSelection", command=lambda: selected_customer(),
                                               width=15, height=2).grid(row=4, column=0, padx=0, pady=0)
        # Customer Table Buttons
        self.add_customer_Button = Button(master, text="Add\n Customer ", width=12, height=2,
                                          command=lambda: insert_data()).grid(row=4, column=1, padx=0, pady=10)
        self.del_customer_Button = Button(master, text="Remove\n Customer ", width=12, height=2,
                                          command=lambda: remove_selected_data()).grid(row=5, column=1, padx=0, pady=0)
        # self.gen_custref_num_Button = Button(master, text="Generate Customer\n Reference Number", width=15,height=2,command=lambda:gen_cust_ref_id()).grid(row=6, column=0, padx=0, pady=0)
        self.name = StringVar()
        self.time = StringVar()
        self.i = 0

        x = []
        for x in self.trv.get_children():
            x.append(self.trv.get_children(['values']))
        if x == []:
            messagebox.showinfo("Cashier Prompt", "Please Enter a Customers Name")

        # Functions bound to the buttons
        # def refresh_customer_table():
        #     conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
        #     cursor = conn.cursor()
        #     query1 = "TRUNCATE TABLE CustomerInfo"
        #     cursor.execute(query1)
        #     query2 = "insert into CustomerInfo (customerName, customerRefID) values('{}','{}')".format(custName,custRefID)
        #     cursor.execute(query2)
        # global selected_cust
        # selected_cust = lambda:selected_customer
        # print(selected_cust)

        def remove_selected_data():
            y = self.trv.selection()[0]
            self.trv.delete(y)

        def insert_data():
            """
            Insertion method.
            """
            import string as stri
            self.i = self.i + 1
            self.name = self.customer_name_entry.get()
            self.customer_name_entry.delete(0, END)
            print(self.name)
            q = str(self.name)
            n_child = len(q)
            print(n_child)
            cust_name = q.upper()
            letters = stri.ascii_uppercase
            n = len(cust_name)
            # randomised customer reference generator
            f = cust_name
            a = ''.join(random.choice(f) for j in range(2))
            self.cust_ref_ID = ''.join(random.choice(letters) for h in range(6)) + f + a
            print("Customer Reference Number:", self.cust_ref_ID)

            # self.time = self.customer_time_entry.get()

            self.trv.insert('', 'end', iid=self.i, values=(self.i, self.name, self.cust_ref_ID))
            ##meassagebox code
            t = []
            for child in self.trv.get_children():
                t.append(self.trv.item(child))

            for elem in t:
                if elem != ['']:
                    a = "Customer Name Entered is:" + cust_name
                    b = "\nCustomer referenceID:" + self.cust_ref_ID
                    c = a + b
                    messagebox.showinfo("Customer Info:", c)
            # database entry code
            custName = cust_name
            custRefID = self.cust_ref_ID
            conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
            cursor = conn.cursor()
            # query1 = "TRUNCATE TABLE CustomerInfo"
            query2 = "insert into CustomerInfo (customerName, customerRefID) values('{}','{}')".format(custName,
                                                                                                       custRefID)

            cursor.execute(query2)
            # cursor.execute(query1)
            conn.commit()
            conn.close()
            instruction_label = Label(master,
                                      text="Please Select a Customer and Cust RefID \nto go ahead with order selection",
                                      font="Arial 25", fg="green")
            instruction_label.place(x=100, y=400)
            # proof of selected customer returning values
            # print(selected_customer())
            # x = []
            # for x in self.trv.get_children():
            #     x.append(self.trv.get_children(['values']))
            # if x == []:

        def selected_customer():
            """has to take the value of customer name and customer reference id, storing it in variable and give to frame changing function"""
            selected = self.trv.focus()
            global values
            values = self.trv.item(selected, 'values')
            # print(values)

            table_cust_name = values[1]
            table_cust_refid = values[2]
            a = " Customer Name Entered is:\n" + table_cust_name + "\n"
            b = " \nCustomer referenceID:\n" + table_cust_refid + "\n"
            c = "You Have Selected:\n" + a + b
            messagebox.showinfo("Customer Info:", c)
            global selected_cust
            selected_cust = values
            return selected_cust

    def menu_display(self):
        self.app = menu_display(self.master)

    def menu(self):
        self.widget_clearer()
        self.menu_display()

    # back button
    def widget_clearer(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def cashier_main_menu_display(self):
        self.app = cash_menu(self.master)

    def back_button(self):
        self.widget_clearer()
        self.cashier_main_menu_display()


class menu_display():
    def __init__(self, master):
        # initialisation commands
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.geometry('1000x600')
        self.master.title("Menu for Customer")
        self.titleLabel = Label(master, text="Menu Interface", font="Arial 40", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(80, 0), pady=(10, 0))
        self.bookingButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1,
                                                                                                             x=-2, y=2,
                                                                                                             anchor=NE)

        self.custinterfacevalues = selected_cust
        print(self.custinterfacevalues)
        cust_name = self.custinterfacevalues[1]
        cust_refid = self.custinterfacevalues[2]
        self.cust_details_label = Label(master,
                                        text=f"Selected Customer Name:{cust_name}\n Customer RefID:{cust_refid}",
                                        font="Arial 20", fg="green")
        self.cust_details_label.place(x=450, y=10)

        # initilize databases
        conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
        cursor = conn.cursor()
        # query1 = "TRUNCATE TABLE CustomerInfo"
        # query2 = "TRUNCATE TABLE Bills"
        query3 = "TRUNCATE TABLE CartOrders"
        # cursor.execute(query1)
        # cursor.execute(query2)
        cursor.execute(query3)
        # menu treeview
        self.billsTV = ttk.Treeview(height=15, selectmode='browse')
        self.billsTV['columns'] = ("Item Index", "Item/Dish", "Type of Dish", "Price")
        self.billsTV.column("#0", width=0, stretch=NO)
        self.billsTV.column("Item Index", anchor=W, width=40)
        self.billsTV.column("Item/Dish", anchor=W, width=160)
        self.billsTV.column("Type of Dish", anchor=W, width=100)
        self.billsTV.column("Price", anchor=W, width=60)
        self.billsTV.grid(row=1, column=1, columnspan=2, padx=20)

        self.scrollBar = Scrollbar(self.master, orient="vertical")
        self.scrollBar.grid(row=1, column=2, columnspan=1, sticky="NSE")
        self.scrollBar.config(command=self.billsTV.yview)
        self.billsTV.configure(yscrollcommand=self.scrollBar.set)
        self.billsTV.heading('#0')
        self.billsTV.heading('#1', text="Index")
        self.billsTV.heading('#2', text="Item/Dish")
        self.billsTV.heading('#3', text="Type of Dish")
        self.billsTV.heading('#4', text="Price")
        # lefttable
        self.temp_billsTV1 = ttk.Treeview(height=15, selectmode='browse')
        self.temp_billsTV1['columns'] = ("Item Index", "Item/Dish", "Quantity", "Price", "Total for Qty Sel")
        self.temp_billsTV1.column("#0", width=0, stretch=NO)
        self.temp_billsTV1.column("Item Index", anchor=W, width=40)
        self.temp_billsTV1.column("Item/Dish", anchor=W, width=120)
        self.temp_billsTV1.column("Quantity", anchor=CENTER, width=80)
        self.temp_billsTV1.column("Price", anchor=CENTER, width=50)
        self.temp_billsTV1.column("Total for Qty Sel", anchor=CENTER, width=120)
        # righttable
        # self.temp_billsTV2 = ttk.Treeview(height=15, selectmode='browse')
        # self.temp_billsTV2['columns'] = ("Price", "Total for Qty Sel",)
        # self.temp_billsTV2.column("#0", width=0, stretch=NO)
        # self.temp_billsTV2.column("Price", anchor=CENTER, width=50)
        # self.temp_billsTV2.column("Total for Qty Sel", anchor=CENTER, width=90)
        # self.temp_billsTV.column("Price of Selected Ele", anchor=W, width=60)
        # self.temp_billsTV.column("Price of Selected Qty", anchor=W, width=60)
        # lefttable
        self.temp_billsTV1.grid(row=1, column=3, columnspan=10, padx=130)
        self.temp_billsTV1.heading('#0')
        self.temp_billsTV1.heading('#1', text="Index")
        self.temp_billsTV1.heading('#2', text="Item/Dish")
        self.temp_billsTV1.heading('#3', text="Quantity")
        self.temp_billsTV1.heading('#4', text="Price")
        self.temp_billsTV1.heading('#5', text="Total for Qty Sel")
        ##fake data
        # data = {
        #     [1: ["Rava Dosa", "South Indian", 150],
        #     [2: ["Masala Dosa", "South Indian", 120],
        #     [3: ["Sada Dosa", "South Indian", 70],
        #     [4: ["Idli Plate", "South Indian", 40],
        #     [5: ["Vada Plate", "South Indian", 50],
        #     [6: ["Chinese Bhel", "Chinese", 30],
        #     [7: ["Manhurian Soup", "Chinese", 30],
        #     [8: ["Singapore Soup", "Chinese", 30],
        #     [9: ["Chicken 65", "Chinese", 30],
        #     [10: ["Chicken Crispy", "Cinese", 150],
        #     [11: ["Chicken Manchurian", "Chinese", 120],
        #     12: ["Egg Fried Rice", "Chinese", 70],
        #     13: ["Egg Fried Noodles", "Chinese", 40],
        #     14: ["Chicken Fried Rice", "Chinese", 50],
        #     15: ["Chicken Fried Noodles", "Chinese", 30],
        #     16: ["Chicken Triple Rice", "Chinese", 30],
        #     17: ["Chicken Triple Noodles", "Chinese", 30],
        #     18: ["Veg Triple Rice", "Chinese", 30],
        #     19: ["Veg Triple Noodles", "Chinese", 30]
        # }
        # ["Rava Dosa", 70],
        # ["Masala Dosa", 75],
        # ["Sada Dosa", 60],
        # ["Idli Plate", 40],
        # ["Vada Plate", 50],
        # ["Chinese Bhel", 25],
        # ["Manhurian Soup", 50],
        # ["Singapore Soup", 75],
        # ["Chicken 65", 120],
        # ["Chicken Crispy", 135],
        # ["Chicken Manchurian", 130],
        # ["Egg Fried Rice", 85],
        # ["Egg Fried Noodles", 90],
        # ["Chicken Fried Rice", 100],
        # ["Chicken Fried Noodles", 110],
        # ["Chicken Triple Rice", 130],
        # ["Chicken Triple Noodles", 150],
        # ["Veg Triple Rice", 110],
        # ["Veg Triple Noodles", 124],

        data = [
            [1, "Rava Dosa", "South Indian", 70],
            [2, "Masala Dosa", "South Indian", 75],
            [3, "Sada Dosa", "South Indian", 60],
            [4, "Idli Plate", "South Indian", 40],
            [5, "Vada Plate", "South Indian", 50],
            [6, "Chinese Bhel", "Chinese", 25],
            [7, "Manchurian Soup", "Chinese", 50],
            [8, "Singapore Soup", "Chinese", 75],
            [9, "Chicken 65", "Chinese", 120],
            [10, "Chicken Crispy", "Chinese", 135],
            [11, "Chicken Manchurian", "Chinese", 130],
            [12, "Egg Fried Rice", "Chinese", 85],
            [13, "Egg Fried Noodles", "Chinese", 90],
            [14, "Chicken Fried Rice", "Chinese", 100],
            [15, "Chicken Fried Noodles", "Chinese", 110],
            [16, "Chicken Triple Rice", "Chinese", 130],
            [17, "Chicken Triple Noodles", "Chinese", 150],
            [18, "Veg Triple Rice", "Chinese", 110],
            [19, "Veg Triple Noodles", "Chinese", 124],
        ]
        quantity_values = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20
        ]
        index_items = [
            "Rava Dosa",
            "Masala Dosa",
            "Sada Dosa",
            "Idli Plate",
            "Vada Plate",
            "Chinese Bhel",
            "Manhurian Soup",
            "Singapore Soup",
            "Chicken 65",
            "Chicken Crispy",
            "Chicken Manchurian",
            "Egg Fried Rice",
            "Egg Fried Noodles",
            "Chicken Fried Rice",
            "Chicken Fried Noodles",
            "Chicken Triple Rice",
            "Chicken Triple Noodles",
            "Veg Triple Rice",
            "Veg Triple Noodles",

        ]
        # striped rows
        self.billsTV.tag_configure('oddrow', background='white')
        self.billsTV.tag_configure('evenrow', background='lightblue')

        # add our data
        global count
        count = 0

        for record in data:
            if count % 2 == 0:
                self.billsTV.insert(parent='', index='end', iid=count, text='',
                                    values=(record[0], record[1], record[2], record[3]), tags=('evenrow',))
            else:
                self.billsTV.insert(parent='', index='end', iid=count, text='',
                                    values=(record[0], record[1], record[2], record[3]), tags=('oddrow',))
            # increment counter
            count += 1
        # self.entry_item_dish_entrybox = Label(master, text="Enter Item INDEX", font="Arial 20", fg="green")
        # self.entry_item_dish_entrybox.grid(row=11, column=2, columnspan=1, padx=(0, 0), pady=(0, 0))
        # self.item_name_entry = Entry(master, font=('calibre', 10, 'bold'), bg='grey', width=20)
        # self.item_name_entry.grid(row=12, column=2, padx=20)
        #
        # self.entry_item_qty_entrybox = Label(master, text="Enter Item Quantity", font="Arial 20", fg="green")
        # self.entry_item_qty_entrybox.grid(row=11, column=3, columnspan=1, padx=(0, 0), pady=(0, 0))
        # self.item_qty_entry = Entry(master, font=('calibre', 10, 'bold'), bg='grey', width=20)
        # self.item_qty_entry.grid(row=12, column=3, padx=20)
        # buttons
        # self.cart_add = Button(master, text='Add to\nCart', width=10, height=2)
        # self.cart_add.grid(row=13, column=2, padx=(20, 0), pady=(10, 0))
        # self.cart_del = Button(master, text='Remove from\nCart', width=10, height=2)
        # self.cart_del.grid(row=13, column=3, padx=(20, 0), pady=(10, 0))

        # self.cart_del = Button(master, text='Proceed to\n Payment', width=10, height=2)
        # self.cart_del.grid(row=14, column=3, padx=(20, 0), pady=(10, 0))
        global i
        i = 1
        # trv.insert("", 'end', iid=1,
        #           values=(i, 'Alex', 'Four', 78, 'Male'))

        # l0 = tk.Label(master, text='Add Item',
        #               font=('Helvetica', 16), width=30, anchor="c")
        # l0.grid(row=2, column=1, columnspan=4)

        l1 = tk.Label(master, text='Item Selected: ', width=10, anchor="c")
        l1.grid(row=5, column=1)

        # add one text box

        l2 = tk.Label(master, text='Quantity: ', width=10)
        l2.grid(row=5, column=2)

        # add list box for selection of class
        options = StringVar(master)  # options of item
        options.set("")  # default value
        options1 = IntVar(master)  # options for quantity
        options1.set("")
        options2 = IntVar()
        optionlist_items_list = [
            ["Rava Dosa", 70],
            ["Masala Dosa", 75],
            ["Sada Dosa", 60],
            ["Idli Plate", 40],
            ["Vada Plate", 50],
            ["Chinese Bhel", 25],
            ["Manhurian Soup", 50],
            ["Singapore Soup", 75],
            ["Chicken 65", 120],
            ["Chicken Crispy", 135],
            ["Chicken Manchurian", 130],
            ["Egg Fried Rice", 85],
            ["Egg Fried Noodles", 90],
            ["Chicken Fried Rice", 100],
            ["Chicken Fried Noodles", 110],
            ["Chicken Triple Rice", 130],
            ["Chicken Triple Noodles", 150],
            ["Veg Triple Rice", 110],
            ["Veg Triple Noodles", 124],
        ]

        optionlist_qty = [1,
                          2,
                          3,
                          4,
                          5,
                          6,
                          7,
                          8,
                          9,
                          10,
                          11,
                          12,
                          13,
                          14,
                          15,
                          16,
                          17,
                          18,
                          19

                          ]
        option_list_price = [
            70,
            75,
            60,
            40,
            50,
            25,
            50,
            75,
            120,
            135,
            130,
            85,
            90,
            100,
            110,
            130,
            150,
            110,
            124,
        ]
        k = 0
        j = 0
        n = len(optionlist_items_list)
        items = []
        prices = []
        for price in optionlist_items_list:
            if k in range(n):
                prices.append(optionlist_items_list[k][1])
            k = k + 1

        for item in optionlist_items_list:
            if j in range(n):
                items.append(optionlist_items_list[j][0])
            j = j + 1

        t1 = OptionMenu(master, options, *items)
        t1.grid(row=10, column=1)

        opt1 = OptionMenu(master, options1, *optionlist_qty)
        opt1.grid(row=10, column=2)

        def remove_selected_data():
            y = self.temp_billsTV1.focus()
            self.temp_billsTV1.delete(y)

        def readandWritebillEntries():  # read entries and calculate total for particular quantity selected
            ites = options.get()  # read items
            qty = options1.get()  # read qty
            # prices = options.get()  # read gender

            # loop for selecting prices automatically
            for selectioni in items:
                if ites == selectioni:
                    item_index = items.index(selectioni)
                    price = prices[item_index]
            # code segment for finding total
            total_for_sel_qty = qty * price
            Total = "Rs" + str(total_for_sel_qty)
            global i
            i = i + 1

            self.temp_billsTV1.insert("", 'end',
                                      values=(i - 1, ites, qty, price, total_for_sel_qty))
            print("Selected Itemis:", ites, "and quantity is:", qty)

        def Gtotal():
            t_nested_l = []
            for child in self.temp_billsTV1.get_children():
                t_nested_l.append(self.temp_billsTV1.item(child)["values"])
            no_of_totals = len(t_nested_l)
            list_of_totals = []
            for t in t_nested_l:
                p = t[4]
                list_of_totals.append(p)
            Total = 0
            for tot in list_of_totals:
                Total = Total + tot

            print(Total)
            grand_Total = Label(master, text=f"Grand Total:{Total}", font="Arial 20", fg="green")
            grand_Total.grid(row=4, column=9, padx=30)
            return t_nested_l, Total

        def gen_bill():
            nested_l, grand_Total = Gtotal()

            num_items_ordered = len(nested_l)
            custom_ref_ID = cust_refid  ###must be taken from customer info interface
            import random
            import string as stri
            letters = stri.ascii_uppercase
            f = custom_ref_ID.upper()
            a = ''.join(random.choice(f) for j in range(2))
            self.result_str = ''.join(random.choice(letters) for h in range(2)) + f + a + str(num_items_ordered)
            print(self.result_str)
            print(nested_l)
            cart_order = []
            cart_qty = []
            cart_price = []
            cart_price_for_qty = []
            for elem in nested_l:
                cart_order.append(elem[1])
            for elem in nested_l:
                cart_qty.append(elem[2])
            for elem in nested_l:
                cart_price.append(elem[3])
            for elem in nested_l:
                cart_price_for_qty.append(elem[4])
            print("Items Ordered are:", cart_order)
            print("Item Quantity is:", cart_qty)
            print("Item Price of single item:", cart_price)
            print("Item Price of Selected Quatity:", cart_price_for_qty)
            bill_ref_ID = f"The Bill RefID :{self.result_str} for \nCustomer Ref ID:{custom_ref_ID} "
            messagebox.showinfo("Bill Reference Number", bill_ref_ID)
            billreflabel = Label(master,
                                 text=f"The Bill ReferenceID:{self.result_str} \nCustomer Reference ID:{cust_refid}",
                                 font="Arial 20", fg="green")
            billreflabel.place(x=500, y=500)

            #
            # #cust_ref_id, bill_re_id , grandTotal must be inputted into database
            custrefID = custom_ref_ID
            billrefID = self.result_str
            grandtotal = grand_Total  # returned from function
            conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
            cursor = conn.cursor()
            # query1 = "TRUNCATE TABLE CustomerInfo"
            query2 = "insert into BILLS (customerRefID,billRefID,grandTotal) values('{}','{}',{})".format(custrefID,
                                                                                                          billrefID,
                                                                                                          grandtotal)
            cursor.execute(query2)
            for n in range(num_items_ordered):
                selectedItem = cart_order[n]
                priceOfDish = cart_price[n]
                qtySelected = cart_qty[n]
                priceofqtySelected = cart_price_for_qty[n]
                print(selectedItem)
                print(priceOfDish)
                print(qtySelected)
                cursor.execute(
                    "insert into CartOrders(billRefID,selectedItem,priceOfDish,qtySelected,priceofqtySel) values('{}','{}','{}',{},{})".format(
                        self.result_str, selectedItem, priceOfDish, qtySelected, priceofqtySelected))
                # query3 = "insert into CartOrders(selectedItem,priceOfDish,qtySelected) values('{}','{}',{})".format(selectedItem,priceOfDish, qtySelected)
                # cursor.execute(query3)

            # cursor.execute(query1)
            conn.commit()
            conn.close()
            bill_ReferenceID = billrefID
            return bill_ReferenceID
            #
            # flattened_t_list = [ item for elem in t_nested_l for item in elem]

        add_menu_item_button = tk.Button(master, text='Add Menu Item', width=10,
                                         command=lambda: readandWritebillEntries())
        add_menu_item_button.grid(row=7, column=5)
        rem_menu_item_button = tk.Button(master, text='Remove Menu Item', width=12,
                                         command=lambda: remove_selected_data())
        rem_menu_item_button.grid(row=8, column=5)
        grand_tot_button = tk.Button(master, text='Grand Total', width=10, command=lambda: Gtotal())
        grand_tot_button.grid(row=7, column=6)

        # used to generate bill reference number and initiate databases
        gen_bill_button = tk.Button(master, text='Generate Bill', width=10, command=lambda: gen_bill())
        gen_bill_button.grid(row=8, column=6)

        open_payments_interface_button = tk.Button(master, text='Open Payments', width=10,
                                                   command=lambda: self.payment_menu())
        open_payments_interface_button.grid(row=9, column=6)

        my_str = tk.StringVar()
        l5 = tk.Label(master, textvariable=my_str, width=10)
        l5.grid(row=8, column=1)

    def payments_menu_display(self):
        self.app = payment_menu_display(self.master)

    def payment_menu(self):
        self.widget_clearer()
        self.payments_menu_display()
        return

    # back button
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
        self.master.title("Payment Module")
        self.master.geometry('600x800')
        self.titleLabel = Label(master, text="Payment Interface", anchor=CENTER, font="Arial 40", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(10, 0))
        self.bookingButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1,
                                                                                                             x=-2, y=2,
                                                                                                             anchor=NE)

        self.grand_Total = 0
        self.customer_ref_ID = selected_cust[2]
        self.bill_ref_ID = bill_ReferenceID
        self.billsTV = ttk.Treeview(height=15, selectmode='browse')
        self.billsTV['columns'] = ("Index", "Item/Dish", "Quantity", "Price of Selected Qty")
        self.billsTV.column("#0", width=0, stretch=NO)
        self.billsTV.column("Index", anchor=W, width=40)
        self.billsTV.column("Item/Dish", anchor=N, width=160)
        self.billsTV.column("Quantity", anchor=N, width=120)
        self.billsTV.column("Price of Selected Qty", anchor=N, width=220)
        # labels
        self.billsTV.grid(row=1, column=0, columnspan=1, padx=50)
        self.scrollBar = Scrollbar(self.master, orient="vertical")
        self.scrollBar.grid(row=1, column=0, sticky="NSE", padx=50)
        self.scrollBar.config(command=self.billsTV.yview)
        self.billsTV.configure(yscrollcommand=self.scrollBar.set)
        self.billsTV.heading('#0')
        self.billsTV.heading('#1', text="Index")
        self.billsTV.heading('#2', text="Item/Dish")
        self.billsTV.heading('#3', text="Quantity")
        self.billsTV.heading('#4', text="Price of Selected Quantity")

        # labels
        self.grand_total = Label(master, text="Grand Total:", font="Arial 40", fg="green")
        self.grand_total.place(x=180, y=356)
        cust_ref_ID_label = Label(master, text=f"Customer RefID: {self.customer_ref_ID}", anchor=E, font="Arial 20",
                                  fg="green")
        cust_ref_ID_label.place(x=5, y=400)
        # # self.mode_payment = Label(master, text="Select Mode of Payment:", font="Arial 20", fg="green")
        # self.mode_payment.grid(row=12, column=1, padx=(0, 0), pady=(0, 0))
        self.cash_recieved = Label(master, text="Cash Recieved:", anchor=W, font="Arial 30", fg="green")
        self.cash_recieved.place(x=5, y=450)
        # self.cash_recieved.grid(row=15, column=0,columnspan=1 ,padx=(0, 0), pady=(0, 0))
        self.cash_recieved_entry = Entry(master, font=('calibre', 20, 'bold'), justify=LEFT, bg='red', width=20)
        self.cash_recieved_entry.place(x=250, y=450)
        # self.cash_recieved_entry.grid(row=16, column=0,columnspan=1, padx=0, pady=5)
        # self.credit_card_info = Entry(master, font=('calibre', 20, 'bold'), bg='red', width=20)
        # self.credit_card_info = Label(master, text="Credit Card Info:", font="Arial 20", fg="green")
        # self.credit_card_info.grid(row=14, column=1, columnspan=1, padx=(0, 0), pady=(15, 0))
        # entry widgets
        # self.credit_card_info.grid(row=14, column=2, columnspan=1, padx=20, pady=25)

        # OptionMenu
        # def selected():
        #     pass
        #
        # self.options = ['Cash', 'Credit']
        # self.clicked = StringVar()
        # self.drop = OptionMenu(master, self.clicked, *self.options, command=selected)
        # self.drop.grid(row=12, column=2, pady=10)

        # buttons
        self.make_payment_button = Button(master, text='Make\nPayment', width=10, height=2,
                                          command=lambda: make_payment())
        self.make_payment_button.place(x=100, y=500)
        # self.make_payment_button.grid(row=17, column=0, pady=(10, 0))
        self.grand_total = Button(master, text='Grand\nTotal', width=10, height=2, command=lambda: gen_total())
        self.grand_total.place(x=400, y=500)
        # self.grand_total.grid(row=17, column=1,  pady=(10, 0))
        self.cust_ref_page = Button(master, text='Next Customer', width=10, height=2,
                                    command=lambda: self.booking_menu())
        self.cust_ref_page.place(x=100, y=550)

        # def insert_data():
        conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
        cursor = conn.cursor()
        cursor.execute("select * from  CartOrders")
        self.i = 0
        for ro in cursor:
            self.billsTV.insert('', 'end', text="", values=(self.i + 1, ro[1], ro[3], ro[4]))
            self.i = self.i + 1

        def gen_total():
            c = []
            for child in self.billsTV.get_children():
                c.append(self.billsTV.item(child)["values"])
            print(c)
            l_of_totalprices_qty_sel = []
            for elem in c:
                l_of_totalprices_qty_sel.append(elem[3])
            print(l_of_totalprices_qty_sel)
            total = 0
            for t in l_of_totalprices_qty_sel:
                total = total + float(t)
            print(total)
            self.grand_Total = total + total * (0.18)

            print(self.grand_Total)
            grand_total_label = Label(master, text=f"Rs {self.grand_Total}", font="Arial 40", fg="green")
            grand_total_label.place(x=420, y=356)

        # creates randomised receipt Id and add details to reciept table and

        def make_payment():
            def receiptId_generator():
                import random
                import string as stri
                letters = stri.ascii_uppercase
                customer_refID = str(self.customer_ref_ID)
                bill_refID = str(self.bill_ref_ID)
                c = customer_refID.upper()
                b = bill_refID.upper()
                a = ''.join(random.choice(b) for j in range(2))
                d = ''.join(random.choice(c) for j in range(2))
                self.result_str = ''.join(random.choice(letters) for h in range(2)) + d + a
                print(self.result_str)
                return self.result_str

            r_id = receiptId_generator()
            try:
                G_total = float(self.grand_Total)
                print(self.grand_Total)
                cash_recvd = int(self.cash_recieved_entry.get())
                if cash_recvd == self.grand_Total:
                    messagebox.showinfo("Order Created", f"Hi Your Food is being prepared and Your Reciept ID is")
                    payment_label_complete = Label(master,
                                                   text=f"Payment Completed.ReceiptID is:{r_id}\nPlease select next customer button ",
                                                   anchor=CENTER, font="Arial 20", fg="green")
                    payment_label_complete.place(x=100, y=600)
                elif cash_recvd > self.grand_Total:
                    change = cash_recvd - self.grand_Total
                    print("Change to be returned", change)
                    messagebox.showinfo("Order Completed",
                                        f"Your Reciept ID is{r_id}\n please collect your change:Rs{change}")
                    payment_label_with_change = Label(master,
                                                      text=f"Payment Completed.ReceiptID is:{r_id}\nPlease select next customer after collecting change button ",
                                                      anchor=CENTER, font="Arial 20", fg="green")
                    payment_label_with_change.place(x=100, y=600)
                elif cash_recvd < self.grand_Total:
                    remainder = self.grand_Total - cash_recvd
                    print("Insufficient amount Recieved.Please provide the remaining:", remainder)
                    messagebox.showinfo("Order Incomplete",
                                        f"Insufficient amount Recieved.Please provide the remaining:{remainder}")
            except ValueError:
                self.cash_recieved_entry.delete(0, END)
                messagebox.showinfo("Warning", "PLEASE ENTER AN INTEGER")

            global receipt_ID
            receipt_ID = r_id
            return receipt_ID

    def cashier_booking_display(self):
        self.app = cash_booking_display(self.master)

    def booking_menu(self):
        self.widget_clearer()
        self.cashier_booking_display()

    # back button
    def widget_clearer(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def cashier_main_menu_display(self):
        self.app = cash_menu(self.master)

    def back_button(self):
        self.widget_clearer()
        self.cashier_main_menu_display()


def main():
    admin = tk.Tk()
    app = cashier_authen(admin)
    admin.mainloop()


if __name__ == '__main__':
    main()
