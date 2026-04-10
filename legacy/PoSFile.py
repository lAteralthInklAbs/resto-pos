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
        self.master.geometry('450x450')
        self.master.title("Main Interface Menu")
        self.bookingButton = Button(master, text="Add \nCustomer", width=20, height=5,command=self.booking_menu)
        self.bookingButton.grid(row=0, column=2, padx=120, pady=20)

        self.MenuButton = Button(master, text="Menu", width=20, height=5,command=self.menu)
        self.MenuButton.grid(row=1, column=2, padx=120, pady=20)

        # self.statusButton = Button(master, text="Order Process Status", width=40, height=5,command=self.order_status_menu)
        # self.statusButton.grid(row=2, column=2, padx=120, pady=20)

        self.paymentButton = Button(master, text="Payment", width=20, height=5,command=self.payment_menu)
        self.paymentButton.grid(row=3, column=2, padx=120, pady=20)

    def widget_clearer(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def cashier_booking_display(self):
        self.app = cash_booking_display(self.master)

    def booking_menu(self):
        self.widget_clearer()
        self.cashier_booking_display()

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

    def payments_menu_display(self):
        self.app = payment_menu_display(self.master)

    def payment_menu(self):
        self.widget_clearer()
        self.payments_menu_display()
#Customer details entry and checking
class cash_booking_display():
    def __init__(self, master):
        self.master = master
        self.booking_display_frame = tk.Frame(self.master)
        self.master.geometry('500x300')
        self.master.title("Customer Registry")

        self.titleLabel = Label(master, text="Customer Details Table", font="Arial 30", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(80, 0), pady=(10, 0))

        # # self.tableLabel = LabelFrame(master, text="Active Customer Registry", font="Arial 20")
        # # self.tableLabel.grid(row=1, column=0, padx=(30, 0), columnspan=2, pady=10)
        self.backButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1,
                                                                                                              x=-2, y=2,
                                                                                                              anchor=NE)
        ##checking database

        #        conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
        #        curs=conn.cursor()
        #        curs.execute("select* from active_reigistry")


        self.trv = ttk.Treeview(self.master, columns=(0,), height="4")
        self.style = ttk.Style(self.trv)
        self.style.configure('Treeview', rowheight=20)
        self.trv.heading('#0', text="Customer Reference Number")
        self.trv.heading('#1', text="Customer Name")
        # self.trv.heading('#2', text="Registered Mobile Number(RMN)")
        # self.trv.heading('#3', text="Assigined Table Number(RTN)")
        self.trv.grid(row=3,column=0,columnspan=10,padx=(16,0))
        # self.clockLabel = Label(master, text="Clock", font="Arial 20", fg="red").grid(row=3, column=0,padx=(0, 0), pady=(20, 0))

        self.entrylabel = Label(master, text="Enter Customer Name", font="Arial 20", fg="green")
        self.entrylabel.grid(row=1, column=0, columnspan=1, padx=(0, 0), pady=(0, 0))
        self.customer_name_entry= Entry(master,font=('calibre',10, 'bold'),bg='red',width=20)
        self.customer_name_entry.grid(row=2,column=0,padx=20)
        self.open_cust_menu_Button = Button(master, text="Open Customer Menu", width=20, height=2).grid(row=4,column=0,padx=0,pady=0)
        self.gen_custref_num_Button = Button(master, text="Generate Customer\n Reference Number", width=20,height=2).grid(row=5, column=0, padx=0, pady=0)
        #self.gen_token_num_Button = Button(master, text="Assign\n Token Number", width=20, height=2).grid(row=5,column=0,padx=0,pady=0)
        self.add_customer_Button = Button(master, text="Add\n Customer ", width=20, height=2).grid(row=4, column=1, padx=0, pady=0)
        self.del_customer_Button = Button(master, text="Remove\n Customer ", width=20, height=2).grid(row=5, column=1, padx=0, pady=0)

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



class menu_display():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.geometry('500x500')
        self.master.title("Menu for Customer")
        self.titleLabel = Label(master, text="Menu Interface", font="Arial 40", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(40, 0), pady=(10, 0))
        self.bookingButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1, x=-2,y=2,anchor=NE)
        self.billsTV = ttk.Treeview(height=15, selectmode='browse')
        self.billsTV['columns'] = ("Item Index", "Item/Dish", "Type of Dish", "Price")
        self.billsTV.column("#0", width=0, stretch=NO)
        self.billsTV.column("Item Index", anchor=W, width=40)
        self.billsTV.column("Item/Dish", anchor=W, width=160)
        self.billsTV.column("Type of Dish", anchor=W, width=100)
        self.billsTV.column("Price", anchor=W, width=60)
        self.billsTV.grid(row=1, column=1, columnspan=5)

        self.scrollBar = Scrollbar(self.master, orient="vertical")
        self.scrollBar.grid(row=1, column=2, columnspan=4, sticky="NSE")
        self.scrollBar.config(command=self.billsTV.yview)
        self.billsTV.configure(yscrollcommand=self.scrollBar.set)
        self.billsTV.heading('#0')
        self.billsTV.heading('#1', text="Index")
        self.billsTV.heading('#2', text="Item/Dish")
        self.billsTV.heading('#3', text="Type of Dish")
        self.billsTV.heading('#4', text="Price")

        ###fake data
        data = [
            [1, "Rava Dosa", "South Indian", 150],
            [2, "Masala Dosa", "South Indian", 120],
            [3, "Sada Dosa", "South Indian", 70],
            [4, "Idli Plate", "South Indian", 40],
            [5, "Vada Plate", "South Indian", 50],
            [6, "Chinese Bhel", "Chinese", 30],
            [7, "Manhurian Soup", "Chinese", 30],
            [8, "Singapore Soup", "Chinese", 30],
            [9, "Chicken 65", "Chinese", 30],
            [10, "Chicken Crispy", "Cinese", 150],
            [11, "Chicken Manchurian", "Chinese", 120],
            [12, "Egg Fried Rice", "Chinese", 70],
            [13, "Egg Fried Noodles", "Chinese", 40],
            [14, "Chicken Fried Rice", "Chinese", 50],
            [15, "Chicken Fried Noodles", "Chinese", 30],
            [16, "Chicken Triple Rice", "Chinese", 30],
            [17, "Chicken Triple Noodles", "Chinese", 30],
            [18, "Veg Triple Rice", "Chinese", 30],
            [19, "Veg Triple Noodles", "Chinese", 30]
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
        self.entry_item_dish_entrybox = Label(master, text="Enter Item INDEX", font="Arial 20", fg="green")
        self.entry_item_dish_entrybox.grid(row=11, column=1, columnspan=1, padx=(0, 0), pady=(0, 0))
        self.item_name_entry = Entry(master, font=('calibre', 10, 'bold'), bg='grey', width=20)
        self.item_name_entry.grid(row=12, column=1, padx=20)

        self.entry_item_qty_entrybox = Label(master, text="Enter Item Quantity", font="Arial 20", fg="green")
        self.entry_item_qty_entrybox.grid(row=11, column=2, columnspan=1, padx=(0, 0), pady=(0, 0))
        self.item_qty_entry = Entry(master, font=('calibre', 10, 'bold'), bg='grey', width=20)
        self.item_qty_entry.grid(row=12, column=2, padx=20)
        #buttons
        self.cart_add= Button(master,text='Add to\nCart',width=10, height=2)
        self.cart_add.grid(row=13,column=1,padx=(20,0),pady=(10,0))
        self.cart_del = Button(master, text='Remove from\nCart', width=10, height=2)
        self.cart_del.grid(row=13, column=2, padx=(20, 0), pady=(10, 0))

        # item_dish_entrybox = Entry(self.master, value=index_items)
        # item_dish_entrybox.grid(row=10, column=1)
        #
        # item_qty_entrybox = Entry(self.master, value=q)
        #
        # item_qty_entrybox.grid(row=10, column=1)

        # def pick_index(e):
        #     if index_combobox.get() == "Rava Dosa":
        #         item_dish_combobox.config(value=index_items)
        #         item_dish_combobox.current(0)
        #
        # # create a dropbox
        # index_combobox = ttk.Combobox(self.master, value=index_values)
        # index_combobox.current(0)
        # index_combobox.grid(row=10, column=2)
        #
        # # bind the comboboxes
        # index_combobox.bind("<<ComboboxSelected>>", pick_index)
        # # item_dish combobox
        # item_dish_entrybox = ttk.Combobox(self.master, value=index_items)
        # item_dish_entrybox.current(0)
        # item_dish_entrybox.grid(row=10, column=1)

#         #self.treescroll.grid()
#         self.titleWindow = root.title("Customer Menu")
#
#         self.titleLabel = Label(root, text="Menu of Cuisines ", font="Arial 40", fg="green")
#         self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(80, 0), pady=(10, 0))
#
#         # self.tableLabel = LabelFrame(root, text="Menu", font="Arial 40")
#         # self.tableLabel.grid(row=1, column=0, padx=(30, 0), columnspan=2, pady=10)
#
#         ##checking database
# #        conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
# #        curs=conn.cursor()
# #        curs.execute("select* from active_reigistry")
#
#         self.trv = ttk.Treeview(self.master,yscrollcommand=self.treescroll.set,columns=(0,1,2),height="6",selectmode='extended')
#
#         # scrollBar = Scrollbar(window, orient="vertical", command=billsTV.yview)
#         # scrollBar.grid(row=5, column=4, sticky="NSE")
#         #
#
#         self.treescroll = Scrollbar(self.booking_display_tree_frame, orient="vertical", command=self.trv.yview)
#         self.treescroll.config(command=self.trv.yview)
#         self.style = ttk.Style(self.trv)
#         self.style.configure('Treeview',rowheight=20)
#         self.trv.heading('#0', text="Index")
#         self.trv.heading('#1', text="Item/Dish")
#         self.trv.heading('#2', text="Type of Dish")
#         self.trv.heading('#3', text="Price")
#
#
#         #define number of columns
#       #  self.trv["columns"] = ()
#
#      #   import customer_pos
#         self.trv.pack()
#
#

#back button
    def widget_clearer(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def cashier_main_menu_display(self):
        self.app = cash_menu(self.master)

    def back_button(self):
        self.widget_clearer()
        self.cashier_main_menu_display()


# class order_status_display():
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.titleLabel = Label(master, text="Order Process Interface", font="Arial 40", fg="green")
#         self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(40, 0), pady=(10, 0))
#         self.bookingButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1, x=-2,y=2,anchor=NE)
#
# #back button
#     def widget_clearer(self):
#         for widget in self.master.winfo_children():
#             widget.destroy()
#
#     def cashier_main_menu_display(self):
#         self.app = cash_menu(self.master)
#
#     def back_button(self):
#         self.widget_clearer()
#         self.cashier_main_menu_display()

class payment_menu_display():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("Payment Module")
        self.master.geometry('500x700')
        self.titleLabel = Label(master, text="Payment Interface", font="Arial 40", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=4, padx=(40, 0), pady=(10, 0))
        self.bookingButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1, x=-2,y=2,anchor=NE)


        self.billsTV = ttk.Treeview(height=15,selectmode='browse')
        self.billsTV['columns']= ("Item Index","Item/Dish","Quantity","Price")
        self.billsTV.column("#0",width=0,stretch=NO)
        self.billsTV.column("Item Index",anchor=W,width=40)
        self.billsTV.column("Item/Dish",anchor=W,width=160)
        self.billsTV.column("Quantity",anchor=W,width=100)
        self.billsTV.column("Price",anchor=W,width=60)

        self.scrollBar = Scrollbar(self.master, orient="vertical")
        self.scrollBar.grid(row=9, column=2,columnspan=11, sticky="NSE")
        self.scrollBar.config(command=self.billsTV.yview)
        self.billsTV.configure(yscrollcommand=self.scrollBar.set)
        self.billsTV.heading('#0')
        self.billsTV.heading('#1', text="Index")
        self.billsTV.heading('#2', text="Item/Dish")
        self.billsTV.heading('#3', text="Quantity")
        self.billsTV.heading('#4', text="Price")
        self.billsTV.grid(row=9, column=1,columnspan=10,padx=20)

        #labels
        self.grand_total= Label(master, text="Grand Total:", font="Arial 40", fg="green")
        self.grand_total.grid(row=11, column=1, columnspan=1, padx=(0, 0), pady=(0, 0))
        self.mode_payment= Label(master, text="Select Mode of Payment:", font="Arial 20", fg="green")
        self.mode_payment.grid(row=12, column=1, columnspan=1, padx=(0, 0), pady=(0, 0))
        self.cash_recieved= Label(master, text="Cash Recieved:", font="Arial 20", fg="green")
        self.cash_recieved.grid(row=13, column=1, columnspan=1, padx=(0, 0), pady=(15, 0))
        self.credit_card_info = Label(master, text="Credit Card Info:", font="Arial 20", fg="green")
        self.credit_card_info.grid(row=14, column=1, columnspan=1, padx=(0, 0), pady=(15, 0))
        #entry widgets
        self.cash_recieved_entry = Entry(master, font=('calibre', 10, 'bold'), bg='red', width=20)
        self.cash_recieved_entry.grid(row=13, column=2,columnspan=1, padx=20,pady=15)
        self.credit_card_info= Entry(master, font=('calibre', 10, 'bold'), bg='red', width=20)
        self.credit_card_info.grid(row=14, column=2,columnspan=1 ,padx=20,pady=15)
        #OptionMenu
        def selected():
            pass
        self.options=['Cash','Credit']
        self.clicked = StringVar()
        self.drop = OptionMenu(master, self.clicked, *self.options, command=selected)
        self.drop.grid(row=12, column=2)

        #buttons
        self.make_payment_button= Button(master,text='Make\nPayment',width=10, height=2)
        self.make_payment_button.grid(row=15,column=2,padx=(20,0),pady=(10,0))
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