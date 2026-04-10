# payments processing file last edit 24th March 4:12pm
#completed payments module
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pymysql


class payment_menu_display():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("Payment Module")
        self.master.geometry('600x600')
        self.titleLabel = Label(master, text="Payment Interface", anchor=CENTER,font="Arial 40", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=1, padx=(0, 0), pady=(10, 0))
        # self.bookingButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1, x=-2,y=2,anchor=NE)
        self.grand_Total=0
        self.customer_ref_ID = "ANUROOPSFJO"
        self.bill_ref_ID = "FHJGGANUROOPSFJO4"
        self.billsTV = ttk.Treeview(height=15, selectmode='browse')
        self.billsTV['columns'] = ("Index", "Item/Dish", "Quantity", "Price of Selected Qty")
        self.billsTV.column("#0", width=0, stretch=NO)
        self.billsTV.column("Index", anchor=W, width=40)
        self.billsTV.column("Item/Dish", anchor=N, width=160)
        self.billsTV.column("Quantity", anchor=N, width=120)
        self.billsTV.column("Price of Selected Qty", anchor=N, width=220)
        #labels
        self.billsTV.grid(row=1, column=0,columnspan=1,padx = 50)
        self.scrollBar = Scrollbar(self.master, orient="vertical")
        self.scrollBar.grid(row=1, column=0,sticky="NSE",padx=50)
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
        cust_ref_ID_label = Label(master, text=f"Customer RefID: {self.customer_ref_ID}",anchor=E, font="Arial 20", fg="green")
        cust_ref_ID_label.place(x=5, y=400)
        # # self.mode_payment = Label(master, text="Select Mode of Payment:", font="Arial 20", fg="green")
        # self.mode_payment.grid(row=12, column=1, padx=(0, 0), pady=(0, 0))
        self.cash_recieved = Label(master, text="Cash Recieved:",anchor=W ,font="Arial 30", fg="green")
        self.cash_recieved.place(x=5, y=450)
        # self.cash_recieved.grid(row=15, column=0,columnspan=1 ,padx=(0, 0), pady=(0, 0))
        self.cash_recieved_entry = Entry(master, font=('calibre', 20, 'bold'),justify=LEFT, bg='red', width=20)
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
        self.make_payment_button = Button(master, text='Make\nPayment', width=10, height=2,command=lambda:make_payment())
        self.make_payment_button.place(x=100,y=500)
        # self.make_payment_button.grid(row=17, column=0, pady=(10, 0))
        self.grand_total = Button(master, text='Grand\nTotal',width=10, height=2,command=lambda:gen_total())
        self.grand_total.place(x=450, y=500)
        # self.grand_total.grid(row=17, column=1,  pady=(10, 0))

        # def insert_data into treeview:
        conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
        cursor = conn.cursor()
        cursor.execute("select * from  CartOrders")
        self.i = 0
        for ro in cursor:
            self.billsTV.insert('','end',text="",values =(self.i+1,ro[1],ro[3],ro[4]))
            self.i=self.i+1
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
            self.grand_Total = total+total*(0.18)

            print(self.grand_Total)
            grand_total_label = Label(master, text=f"Rs {self.grand_Total}", font="Arial 40", fg="green")
            grand_total_label.place(x=420, y=356)

        #must create randomised receipt Id and add details to reciept table and

        def make_payment():
            def db_table_insert():
                final_order_nested_l = []
                for child in self.billsTV.get_children():
                    final_order_nested_l.append(self.billsTV.item(child)["values"])
                no_of_totals = len(final_order_nested_l)
                print(final_order_nested_l)
                cart_order = []
                cart_qty = []

                cart_price_for_qty = []
                for elem in final_order_nested_l:
                    cart_order.append(elem[1])
                for elem in final_order_nested_l:
                    cart_qty.append(elem[2])
                for elem in final_order_nested_l:
                    cart_price_for_qty.append(elem[4])
                print("Items Ordered are:", cart_order)
                print("Item Quantity is:", cart_qty)
                print("Item Price of Selected Quatity:", cart_price_for_qty)
                for n in range(no_of_totals):
                    selectedItem = cart_order[n]

                    qtySelected = cart_qty[n]
                    priceofqtySelected = cart_price_for_qty[n]
                    print(selectedItem)
                    print(qtySelected)
                    print(priceofqtySelected)
                    cursor.execute(
                        "insert into FinalOrders(billRefID,selectedItem,priceOfDish,qtySelected,priceofqtySel) values('{}','{}','{}',{},{})".format(
                            self.result_str, selectedItem, qtySelected, priceofqtySelected,G_total))

            def receiptId_generator():
                import random
                import string as stri
                letters = stri.ascii_uppercase
                customer_refID = self.customer_ref_ID
                bill_refID = self.bill_ref_ID
                c = customer_refID.upper()
                b = bill_refID.upper()
                a = ''.join(random.choice(b) for j in range(2))
                self.result_str = ''.join(random.choice(letters) for h in range(2)) + c + a
                print(self.result_str)
                return self.result_str
            r_id = receiptId_generator()
            try:
                G_total = float(self.grand_Total)
                print(self.grand_Total)
                cash_recvd= int(self.cash_recieved_entry.get())
                if cash_recvd == self.grand_Total:
                    db_table_insert()
                    messagebox.showinfo("Order Created",f"Hi Your Food is being prepared and Your Reciept ID is")
                    pass
                elif cash_recvd > self.grand_Total:
                    change = cash_recvd - self.grand_Total
                    print("Change to be returned",change)
                    print("Reference ID",r_id)
                    db_table_insert()
                    messagebox.showinfo("Order Completed",f"Your Reciept ID is{r_id}\n please collect your change:Rs{change}")
                elif cash_recvd < self.grand_Total:
                    remainder = self.grand_Total-cash_recvd
                    print("Insufficient amount Recieved.Please provide the remaining:",remainder)
                    messagebox.showinfo("Order Incomplete", f"Insufficient amount Recieved.Please provide the remaining:{remainder}")
            except ValueError:
                self.cash_recieved_entry.delete(0, END)
                messagebox.showinfo("Warning","PLEASE ENTER AN INTEGER")
    #back button
    # def widget_clearer(self):
    #     for widget in self.master.winfo_children():
    #         widget.destroy()
    #
    # def cashier_main_menu_display(self):
    #     self.app = cash_menu(self.master)
    #
    # def back_button(self):
    #     self.widget_clearer()
    #     self.cashier_main_menu_display()


def main():
    admin = tk.Tk()
    app = payment_menu_display(admin)
    admin.mainloop()


if __name__ == '__main__':
    main()

