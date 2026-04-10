from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql

window = Tk()
window.geometry("600x600")
window.title("Login")



#========Field Listener=========#
def quantityFieldListener(a,b,c):
    global quantityVar
    global costVar
    global itemRate
    quantity = quantityVar.get()
    if quantity != "":
        try:
            quantity = float(quantity)
            cost = quantity*itemRate
            quantityVar.set("%.2f"%quantity)
            costVar.set("%.2f"%cost)
        except ValueError:
            quantity = quantity[:-1]
            quantityVar.set("%.2f"%quantity)

def costFieldListener(a,b,c):
    global quantityVar
    global costVar
    global itemRate
    cost = costVar.get()
    if cost != "":
        try:
            cost=float(cost)
            quantity = cost/itemRate
            quantityVar.set("%.2f"%quantity)
            costVar.set("%.2f"%cost)
        except ValueError:
            cost = cost[:-1]
            costVar.set(cost)
    else:
        cost=0
        costVar.set(cost)

#========Global variable for entries========#
#=========Login Variables========#

usernameVar = StringVar()
passwordVar = StringVar()
#=========main window variables=======#
options = []
rateDict= {}
itemVariable=StringVar()
quantityVar = StringVar()
quantityVar.trace('w',quantityFieldListener)
itemRate=1
rateVar=StringVar()
rateVar.set("%.2f"%itemRate)
costVar=StringVar()
costVar.trace('w',costFieldListener)
#===========Main Tree View=============#
billsTV=ttk.Treeview(height=15,columns=("Item Name","Quantity","Cost"))

#==========add item variables==========#
storeOptions=['Frozen','Fresh']
addItemNameVar=StringVar()
addItemRateVar=StringVar()
addItemTypeVar=StringVar()
addstoreVar=StringVar()
addstoreVar.set(storeOptions[0])

#============function to generate bill===========#
def generate_bill():
    global itemVariable
    global quantityVar
    global itemRate
    global costVar
    itemName = itemVariable.get()
    quantity = quantityVar.get()
    cost = costVar.get()
    conn = pymysql.connect(host="localhost",user="root",passwd="anuroop1602",db="billService")
    cursor = conn.cursor()

    query ="insert into bill (name,quantity,rate,cost) values('{}','{}','{}','{}')".format(itemName,quantity,itemRate,cost)
    cursor.execute(query)
    conn.commit()
    conn.close()
    quantityVar.set("0")

#===========function to  read data from list of items======#
def readsAllData():
    global options
    global rateDict
    global itemVariable
    global itemRate
    global Rate
    options=[]
    rateDict={}
    conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    query = "select* from itemlist"
    cursor.execute(query)
    data = cursor.fetchall()
    count = 0
    for row in data:
        count+=1
        options.append(row['nameid'])
        rateDict[row['nameid']]=row['rate']
        itemVariable.set(options)
        itemRate=int(rateDict[options[0]])
    conn.close()
    rateVar.set("%.2f"%itemRate)
    if count==0:
        remove_all_widgets()
        itemAddWindow()
    else:
        remove_all_widgets()
        mainwindow()


def optionMenuListener():
    global itemVariable
    global rateDict
    global itemRate
    item = itemVariable.get()
    itemRate = int(rateDict(item))
    rateVar.set("%.2f"%itemRate)
# ===============function to logOut===================
def LogOut():
    remove_all_widgets()
    loginWindow()
#=============function to remove all widgets==========#

def remove_all_widgets():
    global window
    for widget in window.winfo_children():
        widget.grid_remove()

#=====admin login function===========#
def adminLogin():
    global usernameVar
    global passwordVar

    username=usernameVar.get()
    password=passwordVar.get()

    conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
    cursor = conn.cursor()

    query = "select* from users where username='{}' and password='{}'".format(username,password)
    cursor.execute(query)
    data = cursor.fetchall()
    admin = False
    for row in data:
        admin = True
    conn.close()
    if admin:
        remove_all_widgets()
        readsAllData()
    else:
        messagebox.showerror("Invalid User","Credentials entered are invalid")

def addItemListener():
    remove_all_widgets()
    itemAddWindow()

def goBack():
    remove_all_widgets()
    mainwindow()

def addItem():
    global addItemNameVar
    global addItemRateVar
    global addItemTypeVar
    global addstoreVar
    name = addItemNameVar.get()
    rate = addItemRateVar.get()
    Type = addItemTypeVar.get()
    storeType = addstoreVar.get()
    nameId = name.replace(" ","_")

    conn = pymysql.connect(host="localhost", user="root", passwd="anuroop1602", db="billService")
    cursor = conn.cursor()

    query = "insert into itemlist (name,nameid,rate,type,storetype) values ('{}','{}','{}','{}','{}')".format(name,nameId,rate,Type,storeType)
    cursor.execute(query)
    conn.commit()
    conn.close()
    addItemNameVar.set("")
    addItemRateVar.set("")
    addItemTypeVar.set("")


def loginWindow():

    titleLabel = Label(window,text="P&E Billing System",font="Ariel 40",fg="green")
    titleLabel.grid(row=0,column=0,columnspan=4,padx=(40,0),pady=(10,0))

    loginLabel = Label(window,text="Admin Login",font="Ariel 30")
    loginLabel.grid(row=1,column=2,columnspan=2,padx=(50,0),pady=(10,0))

    usernameLabel = Label(window,text="Username")
    usernameLabel.grid(row=2,column=2,padx=(20,0),pady=(5,0))

    passwordLabel = Label(window,text="Password")
    passwordLabel.grid(row=3,column=2,padx=(20,0),pady=(5,0))

    usernameEntry = Entry(window,textvariable=usernameVar)
    usernameEntry.grid(row=2,column=3,padx=(20,0),pady=(5,0))

    passwordEntry = Entry(window,textvariable=passwordVar,show="*")
    passwordEntry.grid(row=3,column=3,padx=(20,0),pady=(5,0))

    loginButton = Button(window,text="Login",width=20,height=2,command=lambda:adminLogin())
    loginButton.grid(row=4,column=2,columnspan=2)

def mainwindow():
    titleLabel = Label(window,text="P&E Billing System",font="Ariel 30",fg="green")
    titleLabel.grid(row=0,column=1,columnspan=3,pady=(10,0))

    addNewItem = Button(window,text="Add Item",width = 15,height=2,command=lambda:addItemListener())
    addNewItem.grid(row=1,column=0,padx=(10,0),pady=(10,0))

    logoutBtn = Button(window,text="Logout",width = 15,height=2,command=lambda:LogOut())
    logoutBtn.grid(row=1,column=5,pady=(10,0))

    itemLabel = Label(window,text="Select Item")
    itemLabel.grid(row=2,column=0,padx=(5,0),pady=(10,0))

    itemDropDown = OptionMenu(window, itemVariable,options, command=optionMenuListener)
    itemDropDown.grid(row=2,column=1,padx=(10,0),pady=(10,0))

    rateLabel=Label(window,text="Rate")
    rateLabel.grid(row=2,column=2,padx=(10,0),pady=(10,0))
    rateEntry=Entry(window,textvariable=rateVar)
    rateEntry.grid(row=2,column=3,padx=(10,0),pady=(10,0))

    quantityLabel = Label(window,text="Quantity")
    quantityLabel.grid(row=3,column=0,padx=(5,0),pady=(10,0))
    quantityEntry = Entry(window,textvariable=quantityVar)
    quantityEntry.grid(row=3,column=1,padx=(5,0),pady=(10,0))

    costLabel=Label(window,text="Cost")
    costLabel.grid(row=3,column=2,padx=(10,0),pady=(10,0))
    costEntry=Entry(window,textvariable=costVar)
    costEntry.grid(row=3,column=3,padx=(10,0),pady=(10,0))

    buttonBill = Button(window,text="Generate Bill",width=15,command=lambda:generate_bill())
    buttonBill.grid(row=2,column=4,padx=(5,0),pady=(10,0))

    billLabel = Label(window,text="Bills",font="AriaL 25")
    billLabel.grid(row=4,column=2)

    billsTV.grid(row=5,column=0,columnspan=5)

    scrollBar = Scrollbar(window,orient="vertical",command=billsTV.yview())
    scrollBar.grid(row=5,column=4,sticky="NSE")

    billsTV.configure(yscrollcommand=scrollBar.set)

    billsTV.heading('#0',text="Item Name")
    billsTV.heading('#1',text="Rate")
    billsTV.heading('#2',text="Quantity")
    billsTV.heading('#3',text="Cost")

def itemAddWindow():
    backButton = Button(window,text="Back",command=lambda:readsAllData())
    backButton.grid(row=0,column=1)
    titleLabel = Label(window, text="P&E Billing System",width=40,font="Ariel 30", fg="green")
    titleLabel.grid(row=0, column=2, columnspan=4 , pady=(10, 0))

    itemNameLabel= Label(window, text="Name")
    itemNameLabel.grid(row=1, column=1, pady=(10,0))
    itemNameEntry = Entry(window,textvariable=addItemNameVar)
    itemNameEntry.grid(row=1, column=2, pady=(10,0))

    itemRateLabel = Label(window,text="Rate")
    itemRateLabel.grid(row=1, column=3, pady=(10,0))
    itemRateEntry = Entry(window,textvariable=addItemRateVar)
    itemRateEntry.grid(row=1, column=4, pady=(10,0))

    itemTypeLabel = Label(window,text="Type")
    itemTypeLabel.grid(row=2, column=1, pady=(10,0))
    itemTypeEntry = Entry(window,textvariable=addItemTypeVar)
    itemTypeEntry.grid(row=2, column=2, pady=(10,0))

    storetypeLabel = Label(window,text="StoredType")
    storetypeLabel.grid(row=2, column=3, pady=(10,0))
    storetypeEntry = OptionMenu(window,addstoreVar,*storeOptions)
    storetypeEntry.grid(row=2, column=4, pady=(10,0))

    AddItemButton = Button(window,text="Add Item",width=20,height=2,command=lambda:addItem())

    AddItemButton.grid(row=3,column=3,pady=(10,0))

loginWindow()
window.mainloop()