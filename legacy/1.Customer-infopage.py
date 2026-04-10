#completed database entry test for customer
#customer details page customer select button added and interfacing to be done
from tkinter import *
import tkinter as tk
import random
#import string as stri
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import pymysql

class cash_booking_display():
    def __init__(self, master):
        #initalisiations to frame
        self.master = master
        self.booking_display_frame = tk.Frame(self.master)
        self.master.geometry('600x500')
        self.master.title("Customer Registry")

        self.titleLabel = Label(master, text="Customer Details Table", font="Arial 30", fg="green")
        self.titleLabel.grid(row=0, column=0, columnspan=3, padx=(0, 0), pady=(0, 0))
        conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
        cursor = conn.cursor()
        query1 = "TRUNCATE TABLE CustomerInfo"
        cursor.execute(query1)
        # query2 = "insert into CustomerInfo (customerName, customerRefID) values('{}','{}')".format(custName,custRefID)
        # cursor.execute(query2)

        # # self.tableLabel = LabelFrame(master, text="Active Customer Registry", font="Arial 20")
        # # self.tableLabel.grid(row=1, column=0, padx=(30, 0), columnspan=2, pady=10)
        # self.backButton = Button(master, text="Back", width=10, height=2, command=self.back_button).place(relx=1,
        #                                                                                                       x=-2, y=2,
        #                                                                                                       anchor=NE)

        #customer name details(left)
        self.trv = ttk.Treeview(height=9, selectmode='extended')
        self.trv['columns'] = ("Index", "Customer Name","Customer Reference ID")
        self.trv.column("#0", width=0, stretch=NO)
        self.trv.column("Index", anchor=W, width=40)
        self.trv.column("Customer Name", anchor=W, width=180)
        self.trv.column("Customer Reference ID", anchor=W, width=180)
        self.trv.grid(row=1,column=0,padx=(60,0),pady=10)

        # self.scrollBar = Scrollbar(self.master, orient="vertical")
        # self.scrollBar.grid(row=1, column=1, sticky="NSE")
        # self.scrollBar.config(command=self.trv.yview)
        # self.trv.configure(yscrollcommand=self.scrollBar.set)
        self.trv.heading('#0')
        self.trv.heading('#1', text="Index")
        self.trv.heading('#2', text="Customer Name")
        self.trv.heading('#3', text="Customer Reference ID")
         #CUSTOMER ENTRY WIDGET
        self.cust_entrylabel = Label(master, text="Enter Customer Name:", font="Arial 20", fg="green")
        self.cust_entrylabel.grid(row=2, column=0, padx=(0, 0), pady=(0, 0))
        self.customer_name_entry= Entry(master,font=('calibre',15, 'bold'),bg='red',width=20)
        self.customer_name_entry.grid(row=3,column=0,padx=0,pady=0)
        # self.time_entrylabel = Label(master, text="Enter Customer Entry Time:", font="Arial 20", fg="green")
        # self.time_entrylabel.grid(row=4, column=1, padx=(0, 0), pady=(0, 0))
        # self.customer_time_entry = Entry(master, font=('calibre', 15, 'bold'), bg='red', width=20)
        # self.customer_time_entry.grid(row=5, column=1, padx=30, pady=0)

        #Customer Review Buttons For next page
        self.open_cust_menu_Button = Button(master, text="Open Customer Menu", width=15, height=2).grid(row=5,column=0,padx=0,pady=0)
        self.confirm_selection_Button = Button(master, text="Confirm\nSelection",command=lambda:selected_customer(), width=15, height=2).grid(row=4,column=0,padx=0,pady=0)
        #Customer Table Buttons
        self.add_customer_Button = Button(master, text="Add\n Customer ", width=12, height=2,command=lambda:insert_data()).grid(row=4, column=1, padx=0, pady=10)
        self.del_customer_Button = Button(master, text="Remove\n Customer ", width=12, height=2,command=lambda:remove_selected_data()).grid(row=5, column=1, padx=0, pady=0)
        # self.gen_custref_num_Button = Button(master, text="Generate Customer\n Reference Number", width=15,height=2,command=lambda:gen_cust_ref_id()).grid(row=6, column=0, padx=0, pady=0)
        self.name =StringVar()
        self.time= StringVar()
        self.i = 0

        #Functions bound to the buttons
        def changeframe_customer_menu():
            pass

        def remove_selected_data():
            y = self.trv.selection()[0]
            self.trv.delete(y)
        def selected_customer():
            """has to take the value of customer name and customer reference id, storing it in variable and give to frame changing function"""
            selected = self.trv.focus()
            values = self.trv.item(selected,'values')
            print(values)
            table_cust_name = values[1]
            table_cust_refid = values[2]
            a = " Customer Name Entered is:\n"+ table_cust_name +"\n"
            b = " \nCustomer referenceID:\n"+ table_cust_refid+ "\n"
            c = "You Have Selected:\n"+a+b
            messagebox.showinfo("Customer Info:", c)
            return values


        def insert_data():
            """
            Insertion method.
            """
            import string as stri
            self.i = self.i + 1
            self.name = self.customer_name_entry.get()
            self.customer_name_entry.delete(0,END)
            print(self.name)
            q = str(self.name)
            n_child = len(q)
            print(n_child)
            cust_name = q.upper()
            letters = stri.ascii_uppercase
            n = len(cust_name)
            #randomised customer reference generator
            f = cust_name
            a = ''.join(random.choice(f) for j in range(2))
            self.cust_ref_ID = ''.join(random.choice(letters) for h in range(6))+f+a
            print("Customer Reference Number:",self.cust_ref_ID)

            # self.time = self.customer_time_entry.get()

            self.trv.insert('', 'end',iid=self.i, values=(self.i,self.name,self.cust_ref_ID))
            ##meassagebox code
            t = []
            for child in self.trv.get_children():
                t.append(self.trv.item(child))

            for elem in t:
                if elem != ['']:
                    a = "Customer Name Entered is:"+cust_name
                    b = "\nCustomer referenceID:"+self.cust_ref_ID
                    c = a+b
                    messagebox.showinfo("Customer Info:",c)
            #database entry code
            custName = cust_name
            custRefID = self.cust_ref_ID
            conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
            cursor = conn.cursor()
            # query1 = "TRUNCATE TABLE CustomerInfo"
            query2 = "insert into CustomerInfo (customerName, customerRefID) values('{}','{}')".format(custName,custRefID)
            cursor.execute(query2)
            # cursor.execute(query1)
            conn.commit()
            conn.close()
            #proof of selected customer returning values
            #print(selected_customer())
    #        import customer_pos
    #  def customer_main_menu(self):

    #        self.newWindow = tk.Toplevel(self.master)
    #        self.app = cash_booking_display(self.newWindow)

#back button
    def widget_clearer(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    #def cashier_main_menu_display(self,values):
    #    values = selected_customer()
    #    self.app = cash_menu(self.master)

    def back_button(self):
        self.widget_clearer()
        # self.cashier_main_menu_display()


def main():
    admin = tk.Tk()
    app = cash_booking_display(admin)
    admin.mainloop()


if __name__ == '__main__':
    main()
