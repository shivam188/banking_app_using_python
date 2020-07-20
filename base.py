from tkinter import *
import mysql.connector
from tkinter import messagebox
import sys
import os

#Register Function SQL
def register_user():
    try:
        a=(txt1.get())
        b=(txt2.get())
        c=(txt3.get())
        d=(txt4.get())
        e=(txt5.get())
        f=(txt6.get())
        g=(txt9.get())
        if (e == f and a!='' and b!='' and c!='' and d!='' and e!='' and g!=None):
            con=mysql.connector.connect(user='root',password='root',host='localhost',port='8889',database='pro')
            cursor=con.cursor()
            sql="insert into base(name,dob,mob,email,pass,bal) values('%s','%s','%s','%s','%s','%d')"%\
                (a,b,c,d,e,int(g))
            cursor.execute(sql)
            con.commit()
            display_sql="select acno from base where email='%s' "%\
                         (d)
            cursor.execute(display_sql)
            l=cursor.fetchone()
            con.commit()
            messagebox.showinfo("Congratulations","Account Opened...Thank You\nAccount Number : "+str(l[0]))
            root1.destroy()
        else:
            messagebox.showerror("Error","Enter Correct Details Please")

    except mysql.connector.Error as err:

        messagebox.showerror("Error","\tServer Error!\n\tTry after some Time.")

#Register Page Function
def register():
    global root1
    root1 = Toplevel(root)
    root1.title("Registeration Form")
    root1.geometry("500x550+500+200")
    Label(root1,text = "Bank Application", bg = "grey", width = "500", height = "4", font = ("Calibri", 16)).pack()
    global txt1,txt2,txt3,txt3,txt4,txt5,txt6,txt9
    lbl1=Label(root1,text='Enter Name: ')
    txt1=Entry(root1)
    lbl2=Label(root1,text='Enter DOB(dd/mm/yyyy): ')
    txt2=Entry(root1)
    lbl3=Label(root1,text='Enter Mobile No.: ')
    txt3=Entry(root1)
    lbl4=Label(root1,text='Enter Email ID: ')
    txt4=Entry(root1)

    lbl9=Label(root1,text='Enter Opening Balance: ')
    txt9=Entry(root1)

    lbl5=Label(root1,text='Enter Password: ')
    txt5=Entry(root1,show='*')
    lbl6=Label(root1,text='Enter Password Again: ')
    txt6=Entry(root1,show='*')

    btn1 = Button(root1, text = "Register", width = 10, height = 1, command = register_user)
    btn2 = Button(root1, text = "Home", width = 10, height = 1, command = exitFunc1)

    lbl1.place(x=50,y=125)
    txt1.place(x=250,y=125)
    lbl2.place(x=50,y=175)
    txt2.place(x=250,y=175)
    lbl3.place(x=50,y=225)
    txt3.place(x=250,y=225)
    lbl4.place(x=50,y=275)
    txt4.place(x=250,y=275)

    lbl9.place(x=50,y=325)
    txt9.place(x=250,y=325)

    lbl5.place(x=50,y=375)
    txt5.place(x=250,y=375)
    lbl6.place(x=50,y=425)
    txt6.place(x=250,y=425)
    btn1.place(x=110,y=475)
    btn2.place(x=260,y=475)

#Exit Register Page
def exitFunc1():
    root1.destroy()

#Login Page Function
def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Login Window")
    root2.geometry("500x550+500+200")
    Label(root2,text = "Bank Application", bg = "grey", width = "500", height = "5", font = ("Calibri", 16)).pack()
    global txt11,txt12,txt14,t
    lbl11=Label(root2,text='Enter Email ID: ')
    txt11=Entry(root2)
    lbl14=Label(root2,text='Enter Account No.: ')
    txt14=Entry(root2)
    lbl12=Label(root2,text='Enter Password: ')
    txt12=Entry(root2,show='*')
    t=StringVar()
    lbl13=Label(root2,textvariable=t,fg = "red")
    lbl13.place(x=180,y=380)

    btn11 = Button(root2, text = "Login", width = 10, height = 1, command = login_user)
    btn12 = Button(root2, text = "Home", width = 10, height = 1, command = exitFunc2)

    lbl11.place(x=50,y=200)
    txt11.place(x=250,y=200)
    lbl14.place(x=50,y=250)
    txt14.place(x=250,y=250)
    lbl12.place(x=50,y=300)
    txt12.place(x=250,y=300)
    btn11.place(x=140,y=350)
    btn12.place(x=270,y=350)

#Login Function SQL
def login_user():
    global username,password,account
    username=(txt11.get())
    password=(txt12.get())
    account=int(txt14.get())
    try:
        con=mysql.connector.connect(user='root',password='root',host='localhost',port='8889',database='pro')
        cursor=con.cursor()
        display_sql="select * from base where email='%s' and acno='%d' and pass='%s' "%\
                     (username,account,password)
        cursor.execute(display_sql)
        l=cursor.fetchone()
        con.commit()
        if l == None:
            t.set("Wrong credentials!")
        else:
            if( username == l[4] and account == l[0] and  password == l[5]):
                dispaccount(l)
            else:
                t.set("Wrong credentials!")

    except mysql.connector.Error as err:
        messagebox.showerror("Error",'Server Error...')

#Exit Login Function
def exitFunc2():
    root2.destroy()

#Display Accont Page Function
def dispaccount(l):
    global root3
    root3 = Toplevel(root2)
    root3.title("Account Information")
    root3.geometry("500x550+500+200")
    data = l
    sacno = str(data[0])
    Label(root3,text = "Bank Application", bg = "grey", width = "500", height = "5", font = ("Calibri", 16)).pack()
    Label(root3,text="Account Number : "+sacno).pack()
    Label(root3,text="Accountholder Name : "+data[1]).pack()
    Button(root3,text = "Balance", height = "3", width = "20", command = getbal).pack()
    Button(root3,text = "Debit",height = "3", width = "20", command = debit).pack()
    Button(root3,text = "Credit",height = "3", width = "20", command = credit).pack()
    Button(root3,text = "Transfer",height = "3", width = "20", command = transfer).pack()
    Button(root3,text = "Enquiry",height = "3", width = "20", command = enquiry).pack()
    Button(root3,text = "Logout",height = "3", width = "20", command = logout).pack()

#Exit Display Accont Page
def logout():
    root3.destroy()
    root2.destroy()

#Fetch Balance
def getbal():
    try:
        con=mysql.connector.connect(user='root',password='root',host='localhost',port='8889',database='pro')
        #print("Database Connected Succesfully...")
        cursor=con.cursor()
        display_sql="select * from base where email='%s' and acno='%d' and pass='%s' "%\
                     (username,account,password)
        cursor.execute(display_sql)
        d=cursor.fetchone()
        con.commit()
        sbal = str(d[6])
        messagebox.showinfo("Balance","Balance : Rs. "+sbal)

    except mysql.connector.Error as err:
        messagebox.showerror("Error",'Server Error...')

#Account Enquiry
def enquiry():
    global enquiry
    enquiry = Toplevel(root3)
    enquiry.title("Enquiry Window")
    enquiry.geometry("500x550+500+200")
    Label(enquiry,text = "Bank Application", bg = "grey", width = "500", height = "5", font = ("Calibri", 16)).pack()

    try:
        con=mysql.connector.connect(user='root',password='root',host='localhost',port='8889',database='pro')
        cursor=con.cursor()
        display_sql="select * from base where email='%s'"%\
                     (username)
        cursor.execute(display_sql)
        l=cursor.fetchone()
        con.commit()
        data(l)

    except mysql.connector.Error as err:
        messagebox.showerror("Error",'Server Error...')

#Accont Enquiry Data
def data(l):
    dlbl0=Label(enquiry,text='User Accont Number: '+str(l[0]))
    dlbl1=Label(enquiry,text='User Name: '+l[1])
    dlbl2=Label(enquiry,text='User DOB(dd/mm/yyyy): '+l[2])
    dlbl3=Label(enquiry,text='User Mobile No.: '+l[3])
    dlbl4=Label(enquiry,text='User Email ID: '+l[4])
    dlbl9=Label(enquiry,text='User Balance: '+str(l[6]))
    dbtn2 = Button(enquiry, text = "Home", width = 10, height = 1, command = dexit)
    dbtn1 = Button(enquiry, text = "Reset Password", width = 12, height = 1, command = reset)
    dlbl0.place(x=50,y=125)
    dlbl1.place(x=50,y=175)
    dlbl2.place(x=50,y=225)
    dlbl3.place(x=50,y=275)
    dlbl4.place(x=50,y=325)
    dlbl9.place(x=50,y=375)
    dbtn1.place(x=110,y=425)
    dbtn2.place(x=270,y=425)

#Exit Accont Enquiry Data
def dexit():
    enquiry.destroy()

#Reset Password
def reset():
    global reset
    reset = Toplevel(enquiry)
    reset.title("Reset Password")
    reset.geometry("500x550+500+200")
    Label(reset,text = "Bank Application", bg = "grey", width = "500", height = "5", font = ("Calibri", 16)).pack()
    global rtxt1,rtxt2,rtxt3
    rlbl1=Label(reset,text='Enter Current Password: ')
    rtxt1=Entry(reset,show='*')
    rlbl2=Label(reset,text='Enter New Password: ')
    rtxt2=Entry(reset,show='*')
    rlbl3=Label(reset,text='Enter New Password Again: ')
    rtxt3=Entry(reset,show='*')

    rbtn1 = Button(reset, text = "Reset", width = 10, height = 1, command = reset_pass)
    rbtn2 = Button(reset, text = "Home", width = 10, height = 1, command = rhome)

    rlbl1.place(x=50,y=200)
    rtxt1.place(x=250,y=200)
    rlbl2.place(x=50,y=250)
    rtxt2.place(x=250,y=250)
    rlbl3.place(x=50,y=300)
    rtxt3.place(x=250,y=300)
    rbtn1.place(x=120,y=350)
    rbtn2.place(x=290,y=350)

#Reset Password Function
def reset_pass():
    cpass = rtxt1.get()
    npass = rtxt2.get()
    nnpass = rtxt3.get()

    if npass == nnpass:
        try:
            con=mysql.connector.connect(user='root',password='root',host='localhost',port='8889',database='pro')
            cursor=con.cursor()
            get_sql="select pass from base where email='%s'"%\
                         (username)
            cursor.execute(get_sql)
            p=cursor.fetchone()
            con.commit()

            if cpass == p[0]:
                try:
                    con=mysql.connector.connect(user='root',password='root',host='localhost',port='8889',database='pro')
                    cursor=con.cursor()
                    update_sql="update base set pass='%s' where email='%s'"%\
                                (nnpass,username)
                    cursor.execute(update_sql)
                    con.commit()
                    messagebox.showinfo("Password Reset","Congratulations! Password Reset Successful")
                    reset.destroy()
                    enquiry.destroy()

                except mysql.connector.Error as err:
                    messagebox.showerror("Error",'Some problem in accessing details...')
        except mysql.connector.Error as err:
            messagebox.showerror("Error",'Some problem in accessing details...')

    else:
        messagebox.showerror("Error","Invalid Credentials!!!")

#Exit Reset Password Function
def rhome():
    reset.destroy()
    enquiry.destroy()

#Transfer Money
def transfer():
    global transfer
    transfer = Toplevel(root3)
    transfer.title("Transfer Money")
    transfer.geometry("500x550+500+200")
    Label(transfer,text = "Bank Application", bg = "grey", width = "500", height = "5", font = ("Calibri", 16)).pack()

    global ttext2,ttext3,ttext4
    tlabel1=Label(transfer,text='Account Number: '+str(account))
    tlabel2=Label(transfer,text='Enter Amount: ')
    ttext2=Entry(transfer)

    tlabel3=Label(transfer,text='Enter Account No.: ')
    ttext3=Entry(transfer)

    tlabel4=Label(transfer,text='Enter Password: ')
    ttext4=Entry(transfer,show='*')

    tlabel1.place(x=50,y=200)
    tlabel2.place(x=50,y=250)
    ttext2.place(x=250,y=250)

    tlabel3.place(x=50,y=300)
    ttext3.place(x=250,y=300)

    tlabel4.place(x=50,y=350)
    ttext4.place(x=250,y=350)

    button1 = Button(transfer,text = "Proceed",height = "3", width = "10", command = transferfun)
    button2 = Button(transfer,text = "Home",height = "3", width = "10", command = home3)
    button1.place(x=110,y=400)
    button2.place(x=240,y=400)

#Transfer Money Function
def transferfun():
    amt=int(ttext2.get())
    acno=int(ttext3.get())
    tpass=ttext4.get()
    if tpass == password:
        try:
            con=mysql.connector.connect(user='root',password='root',host='localhost',port='8889',database='pro')
            cursor=con.cursor()
            get_sql="select bal from base where email='%s'"%\
                         (username)
            cursor.execute(get_sql)
            l=cursor.fetchone()
            con.commit()
            if(amt>=l[0]):
                print("Insufficient Fund...")
            else:
                new=l[0]-amt
                try:
                    con=mysql.connector.connect(user='root',password='root',host='localhost',port='8889',database='pro')
                    cursor=con.cursor()
                    withdraw_sql="update base set bal='%d' where email='%s'"%\
                                (new,username)
                    cursor.execute(withdraw_sql)
                    con.commit()

                except mysql.connector.Error as err:
                    messagebox.showerror("Error",'Some problem in transferring...')

        except mysql.connector.Error as err:
            messagebox.showerror("Error",'Some error in accessing account details...')

        try:
            con=mysql.connector.connect(user='root',password='root',host='localhost',port='8889',database='pro')
            cursor=con.cursor()
            get_sql="select bal from base where acno='%d'"%\
                         (acno)
            cursor.execute(get_sql)
            l=cursor.fetchone()
            con.commit()
            new1=l[0]+amt

            try:
                con=mysql.connector.connect(user='root',password='root',host='localhost',port='8889',database='pro')
                cursor=con.cursor()
                deposit_sql="update base set bal='%d' where acno='%d'"%\
                            (int(new1),int(acno))
                cursor.execute(deposit_sql)
                con.commit()
                messagebox.showinfo("Transfered","Amount Transfered! Thank you...\nCurrent Balance : "+str(new))
                transfer.destroy()

            except mysql.connector.Error as err:
                messagebox.showerror("Error",'Some problem in transferring...')

        except mysql.connector.Error as err:
            messagebox.showerror("Error",'Some error in accessing account details...')

    else:
        messagebox.showerror("Error","Invalid Password!!!")

#Exit Transfer Money Function
def home3():
    transfer.destroy()

#Debit Money
def debit():
    global debt
    debt = Toplevel(root3)
    debt.title("Debit Money")
    debt.geometry("500x550+500+200")
    Label(debt,text = "Bank Application", bg = "grey", width = "500", height = "5", font = ("Calibri", 16)).pack()
    global text2,text3
    label1=Label(debt,text='Account Number: '+str(account))
    label2=Label(debt,text='Enter Amount: ')
    text2=Entry(debt)
    label3=Label(debt,text='Enter Password: ')
    text3=Entry(debt,show='*')
    label1.place(x=50,y=200)
    label2.place(x=50,y=250)
    text2.place(x=250,y=250)
    label3.place(x=50,y=300)
    text3.place(x=250,y=300)

    button1 = Button(debt,text = "Proceed",height = "3", width = "10", command = debitfun)
    button2 = Button(debt,text = "Home",height = "3", width = "10", command = home)
    button1.place(x=110,y=350)
    button2.place(x=240,y=350)

#Exit Debit Money Function
def home():
    debt.destroy()

#Debit Money Function
def debitfun():
    amt = int(text2.get())
    dpass = (text3.get())
    if dpass == password :
        try:
            con=mysql.connector.connect(user='root',password='root',host='localhost',port='8889',database='pro')
            cursor=con.cursor()
            get_sql="select bal from base where email='%s'"%\
                         (username)
            cursor.execute(get_sql)
            money=cursor.fetchone()
            con.commit()

            if(amt >= money[0]):
                messagebox.showerror("Error","Insufficient Balance!!!")
            else:
                new = money[0]-amt
                try:
                    con=mysql.connector.connect(user='root',password='root',host='localhost',port='8889',database='pro')
                    cursor=con.cursor()
                    withdraw_sql="update base set bal='%d' where email='%s'"%\
                                (new,username)
                    cursor.execute(withdraw_sql)
                    con.commit()
                    messagebox.showinfo("Debited","Money Debited\nCurrent Balance : "+str(new))
                    debt.destroy()

                except mysql.connector.Error as err:
                    messagebox.showerror("Error",'Some problem in debiting...')
        except mysql.connector.Error as err:
            messagebox.showerror("Error",'Some error in accessing account details...')

    else:
        messagebox.showerror("Error","Invalid Password!!!")

#Credit Money
def credit():
    global credit
    credit = Toplevel(root3)
    credit.title("Credit Money")
    credit.geometry("500x550+500+200")
    Label(credit,text = "Bank Application", bg = "grey", width = "500", height = "5", font = ("Calibri", 16)).pack()
    global text5,text6
    label11=Label(credit,text='Account Number: '+str(account))
    label5=Label(credit,text='Enter Amount: ')
    text5=Entry(credit)
    label6=Label(credit,text='Enter Password: ')
    text6=Entry(credit,show='*')
    label11.place(x=50,y=200)
    label5.place(x=50,y=250)
    text5.place(x=250,y=250)
    label6.place(x=50,y=300)
    text6.place(x=250,y=300)

    button1 = Button(credit,text = "Proceed",height = "3", width = "10", command = creditfun)
    button2 = Button(credit,text = "Home",height = "3", width = "10", command = home2)
    button1.place(x=110,y=350)
    button2.place(x=240,y=350)

#Exit Credit Money Function
def home2():
    credit.destroy()

#Credit Money Function
def creditfun():
    amt = int(text5.get())
    dpass = (text6.get())
    if dpass == password :
        try:
            con=mysql.connector.connect(user='root',password='root',host='localhost',port='8889',database='pro')
            cursor=con.cursor()
            get_sql="select bal from base where email='%s'"%\
                         (username)
            cursor.execute(get_sql)
            money=cursor.fetchone()
            con.commit()

            new = money[0]+amt
            try:
                con=mysql.connector.connect(user='root',password='root',host='localhost',port='8889',database='pro')
                cursor=con.cursor()
                deposit_sql="update base set bal='%d' where email='%s'"%\
                            (new,username)
                cursor.execute(deposit_sql)
                con.commit()
                messagebox.showinfo("Credited","Money Credited\nCurrent Balance : "+str(new))
                credit.destroy()

            except mysql.connector.Error as err:
                messagebox.showerror("Error",'Some problem in crediting...')
        except mysql.connector.Error as err:
            messagebox.showerror("Error",'Some error in accessing account details...')

    else:
        messagebox.showerror("Error","Invalid Password!!!")

#Exit Program
def exitFunc():
    sys.exit(0)

#Admin Function
'''
global ad_pass1,ad_pass2
ad_pass1 = "admin1"
ad_pass2 = "admin2"
'''
def admin_check():
    global ad_check
    ad_check = Toplevel(root)
    ad_check.title("Admin Panel")
    ad_check.geometry("500x550+500+200")
    Label(ad_check,text = "Bank Application", bg = "grey", width = "500", height = "5", font = ("Calibri", 16)).pack()
    global actext1,actext2
    aclabel1=Label(ad_check,text='Enter Password 1: ')
    actext1=Entry(ad_check,show='*')
    aclabel2=Label(ad_check,text='Enter Password 2: ')
    actext2=Entry(ad_check,show='*')

    aclabel1.place(x=50,y=250)
    actext1.place(x=250,y=250)
    aclabel2.place(x=50,y=300)
    actext2.place(x=250,y=300)

    button1 = Button(ad_check,text = "Admin Login",height = "3", width = "10", command = admin)
    button2 = Button(ad_check,text = "Home",height = "3", width = "10", command = ad_home2)
    button1.place(x=110,y=350)
    button2.place(x=240,y=350)

#Admin Exit Function
def ad_home2():
    ad_check.destroy()

#Admin Login Function
def admin():
    ad_pass1 = actext1.get()
    ad_pass2 = actext2.get()

    if ( ad_pass1 == "admin1" and ad_pass2 == "admin2" ):
        dispadmin()
    else:
        messagebox.showerror("Error","Invalid Credentials!!!")

def dispadmin():
    global disp
    disp = Toplevel(ad_check)
    disp.title("User Data")
    disp.geometry("500x550+500+200")
    Label(disp,text = "Bank Application", bg = "grey", width = "500", height = "5", font = ("Calibri", 16)).pack()
    Label(disp,text = "Accont Number  || Username || DOB || Mobile || Email Id || Balance\n", width = "500", height = "3").pack()

    try:
        con=mysql.connector.connect(user='root',password='root',host='localhost',port='8889',database='pro')

        cursor=con.cursor()
        display_sql="select acno,name,dob,mob,email,bal from base"
        cursor.execute(display_sql)
        l=cursor.fetchall()
        con.commit()
        for a in l:
            Label(disp,text = str(a[0])+" || "+a[1]+" || "+a[2]+" || "+a[3]+" || "+a[4]+" || "+str(a[5])+"\n" , width = "500", height = "3").pack()

    except mysql.connector.Error as err:
        print('some problem in updating......',err)

    Button(disp,text = "Home",height = "3", width = "10", command = disp_home).pack()

def disp_home():
    disp.destroy()
    ad_check.destroy()



#Starting Page
def main_screen():
    global root
    root = Tk()
    root.geometry("500x550+500+200")
    root.title("Banking Application")
    Label(text = "Bank Application", bg = "grey", width = "500", height = "5", font = ("Calibri", 16)).pack()
    Label(text = "").pack()
    Label(text = "").pack()
    Label(text = "").pack()
    Button(text = "Login", height = "3", width = "20", command = login).pack()
    Button(text = "Register",height = "3", width = "20", command = register).pack()
    Button(text = "Exit",height = "3", width = "20", command = exitFunc).pack()

    buton1 = Button(text = "Admin panel",height = "3", width = "20", command = admin_check)
    buton1.place(x=155,y=450)

    root.mainloop()

main_screen()
