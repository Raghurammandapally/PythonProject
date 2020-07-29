from tkinter import *
import pymysql
from tkinter import messagebox
#from AddContact import *




root = Tk()
root.title("Contacts")
root.minsize(width=400,height=400)
root.geometry("600x500")

try:
    con = pymysql.connect(user='root',password='root', 
                          database='db_proj',host='localhost')
    cur = con.cursor()


except:
    messagebox.showinfo("Unable to connect to DB","try again")

################################################################################################################################################

def insertContact():

    cid = en0.get()
    fname = en1.get()
    mname =en2.get()
    lname = en3.get()
    addressType = en4.get()
    address = en5.get()
    city = en6.get()
    state = en7.get()
    zipp = en8.get()
    phonetype = en9.get() 
    areacode = en10.get()
    phone = en11.get()
    datetype = en12.get() 
    date = en13.get() 

    query1 = "INSERT INTO contact_table VALUES('"+cid+"','"+fname+"','"+mname+"','"+lname+"')"
    query2 = "INSERT INTO address_table(Contact_id,Address_type,Address,City,State,Zip) VALUES('"+cid+"','"+addressType+"','"+address+"','"+city+"','"+state+"','"+zipp+"')"
    query3 = "INSERT INTO phone_table(Contact_id,Phone_type,Area_code,number) VALUES ('"+cid+"','"+phonetype+"','"+areacode+"','"+phone+"')"
    query4 = "INSERT INTO date_table(Contact_id,Date_type,Date) VALUES('"+cid+"','"+datetype+"','"+date+"')"
    try:

        cur.execute(query1)
        cur.execute(query2)
        cur.execute(query3)
        cur.execute(query4)
        
        messagebox.showinfo("Success","Added to Database")
    except:
        messagebox.showinfo("Failure","Please check values and try again.")
    
    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)
    en6.delete(0, END)
    en7.delete(0, END)
    en8.delete(0, END)
    en9.delete(0, END)
    en10.delete(0, END)
    en11.delete(0, END)
    en12.delete(0, END)
    en13.delete(0, END)

#########################################################################################################################################

def insertUpdateContact():
   
    cid = cid_en.get()
    fname = en1.get()
    mname =en2.get()
    lname = en3.get()
    addressType = en4.get()
    address = en5.get()
    city = en6.get()
    state = en7.get()
    zipp = en8.get()
    phonetype = en9.get() 
    areacode = en10.get()
    phone = en11.get()
    datetype = en12.get() 
    date = en13.get() 
    print("CID:",cid)

    query1 = "UPDATE contact_table SET Fname='"+fname+"' , Mname='"+mname+"' , Lname='"+lname+"' where Contact_id = '"+cid+"'"
    query2 = "UPDATE address_table SET Address_type='"+addressType+"', Address='"+address+"', City='"+city+"', State='"+state+"',Zip='"+zipp+"' where Contact_id = '"+cid+"'"
    query3 = "UPDATE phone_table SET Phone_type = '"+phonetype+"',Area_code='"+areacode+"',NUMBER='"+phone+"' where Contact_id = '"+cid+"'"
    query4 = "UPDATE date_table SET Date_type= '"+datetype+"',Date='"+date+"' where Contact_id = '"+cid+"'"
    print(cid)

    try:
        if(len(cid_en.get()) != 0):
            print("11")
            cur.execute(query1)
            cur.execute(query2)
            cur.execute(query3)
            cur.execute(query4)
            con.commit()
            messagebox.showinfo("Success","Updated")
        else:
             messagebox.showinfo("Failure","Check contactID")
             root.quit()
    except:
        messagebox.showinfo("Failure","Check ContactID")

    cid_en.delete(0, END)

###########################################################################################################################################

def deleteContact():
   
    cid = cid_en.get()

    try:
        if(len(cid_en.get()) != 0):
            cur.execute("DELETE FROM contact_table where Contact_id='"+cid+"'")
            con.commit()
            messagebox.showinfo("Success","Contact deleted from  Database")
        else:
             messagebox.showinfo("Failure","Contact is not there in database to be deleted")
             root.quit()
    except:
        messagebox.showinfo("Failure","Contact is not there in database to be deleted")

    cid_en.delete(0, END)


##############################################################################################################################################

def addContact():

    global Canvas1,labelFrame,lb0,en0,lb1,en1,lb2,en2,lb3,en3,lb4,en4,lb5,en5,lb6,en6,lb7,en7,lb8,en8,lb9,en9,lb10,en10,lb11,en11,lb12,en12,lb13,en13
    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#FFF9C4",width = 1200, height = 1200)
    Canvas1.pack(expand=False,fill=BOTH) 
        
    labelFrame = Frame(root,bg='#044F67',height=0.9)
    labelFrame.place(relx=0.22,rely=0.01,relwidth=0.6,relheight=0.92)

    lb0 = Label(labelFrame,text="ContactID : ", bg='#044F67', fg='white')
    lb0.place(relx=0.05,rely=0.01)
    
    en0 = Entry(labelFrame)
    en0.place(relx=0.3,rely=0.01, relwidth=0.5)
    
    # firstname
    lb1 = Label(labelFrame,text="FirstName : ", bg='#044F67', fg='white')
    lb1.place(relx=0.05,rely=0.08)
    
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.08, relwidth=0.5)

    #Middle name
    lb2 = Label(labelFrame,text="MiddleName : ", bg='#044F67', fg='white')
    lb2.place(relx=0.05,rely=0.14)
    
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.14, relwidth=0.5)
    
    #Last Name
    lb3 = Label(labelFrame,text="LastName : ", bg='#044F67', fg='white')
    lb3.place(relx=0.05,rely=0.20)
    
    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.20, relwidth=0.5)
    print("ram")

    #Address type
    lb4 = Label(labelFrame,text="AddressType : ", bg='#044F67', fg='white')
    lb4.place(relx=0.05,rely=0.27)
    
    en4 = Entry(labelFrame)
    en4.place(relx=0.3,rely=0.27, relwidth=0.5)
    
    #Address
    lb5 = Label(labelFrame,text="Address : ", bg='#044F67', fg='white')
    lb5.place(relx=0.05,rely=0.34)
    
    en5 = Entry(labelFrame)
    en5.place(relx=0.3,rely=0.34, relwidth=0.5)

    #City
    lb6 = Label(labelFrame,text="City : ", bg='#044F67', fg='white')
    lb6.place(relx=0.05,rely=0.42)
    
    en6 = Entry(labelFrame)
    en6.place(relx=0.3,rely=0.42, relwidth=0.5)

    #State
    lb7 = Label(labelFrame,text="State : ", bg='#044F67', fg='white')
    lb7.place(relx=0.05,rely=0.50)
    
    en7 = Entry(labelFrame)
    en7.place(relx=0.3,rely=0.50, relwidth=0.5)

    #zip
    lb8 = Label(labelFrame,text="Zip : ", bg='#044F67', fg='white')
    lb8.place(relx=0.05,rely=0.58)
    
    en8 = Entry(labelFrame)
    en8.place(relx=0.3,rely=0.58, relwidth=0.5)
    
    #Phone type
    lb9 = Label(labelFrame,text="PhoneType : ", bg='#044F67', fg='white')
    lb9.place(relx=0.05,rely=0.66)
    
    en9 = Entry(labelFrame)
    en9.place(relx=0.3,rely=0.66, relwidth=0.5)

    #Area_code
    lb10 = Label(labelFrame,text="AreaCode : ", bg='#044F67', fg='white')
    lb10.place(relx=0.05,rely=0.74)
    
    en10 = Entry(labelFrame)
    en10.place(relx=0.3,rely=0.74, relwidth=0.5)
    
    #Phone
    lb11 = Label(labelFrame,text="Phone : ", bg='#044F67', fg='white')
    lb11.place(relx=0.05,rely=0.80)
    
    en11 = Entry(labelFrame)
    en11.place(relx=0.3,rely=0.80, relwidth=0.5)

    #Date type
    lb12 = Label(labelFrame,text="DateType : ", bg='#044F67', fg='white')
    lb12.place(relx=0.05,rely=0.86)
    
    en12 = Entry(labelFrame)
    en12.place(relx=0.3,rely=0.86, relwidth=0.5)

    #date
    lb13 = Label(labelFrame,text="Date: ", bg='#044F67', fg='white')
    lb13.place(relx=0.05,rely=0.93)
    
    en13 = Entry(labelFrame)
    en13.place(relx=0.3,rely=0.93, relwidth=0.5)
    
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#5F9EA0', fg='#333945',command=insertContact)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    quitBtn = Button(root,text="Quit",bg='#5F9EA0', fg='#333945',command=root.quit)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)




################################################################################################################################################

def addUpdateContact():

    global Canvas1,labelFrame,lb1,en1,lb2,en2,lb3,en3,lb4,en4,lb5,en5,lb6,en6,lb7,en7,lb8,en8,lb9,en9,lb10,en10,lb11,en11,lb12,en12,lb13,en13
    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#FFF9C4",width = 1200, height = 1200)
    Canvas1.pack(expand=False,fill=BOTH) 
        
    labelFrame = Frame(root,bg='#044F67',height=0.9)
    labelFrame.place(relx=0.22,rely=0.01,relwidth=0.6,relheight=0.92)
    
    # firstname
    lb1 = Label(labelFrame,text="FirstName : ", bg='#044F67', fg='white')
    lb1.place(relx=0.05,rely=0.02)
    
    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.02, relwidth=0.62)

    #Middle name
    lb2 = Label(labelFrame,text="MiddleName : ", bg='#044F67', fg='white')
    lb2.place(relx=0.05,rely=0.10)
    
    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.10, relwidth=0.62)
    
    #Last Name
    lb3 = Label(labelFrame,text="LastName : ", bg='#044F67', fg='white')
    lb3.place(relx=0.05,rely=0.18)
    
    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.18, relwidth=0.62)
    print("ram")

    #Address type
    lb4 = Label(labelFrame,text="AddressType : ", bg='#044F67', fg='white')
    lb4.place(relx=0.05,rely=0.26)
    
    en4 = Entry(labelFrame)
    en4.place(relx=0.3,rely=0.26, relwidth=0.62)
    
    #Address
    lb5 = Label(labelFrame,text="Address : ", bg='#044F67', fg='white')
    lb5.place(relx=0.05,rely=0.34)
    
    en5 = Entry(labelFrame)
    en5.place(relx=0.3,rely=0.34, relwidth=0.62)

    #City
    lb6 = Label(labelFrame,text="City : ", bg='#044F67', fg='white')
    lb6.place(relx=0.05,rely=0.42)
    
    en6 = Entry(labelFrame)
    en6.place(relx=0.3,rely=0.42, relwidth=0.62)

    #State
    lb7 = Label(labelFrame,text="State : ", bg='#044F67', fg='white')
    lb7.place(relx=0.05,rely=0.50)
    
    en7 = Entry(labelFrame)
    en7.place(relx=0.3,rely=0.50, relwidth=0.62)

    #zip
    lb8 = Label(labelFrame,text="Zip : ", bg='#044F67', fg='white')
    lb8.place(relx=0.05,rely=0.58)
    
    en8 = Entry(labelFrame)
    en8.place(relx=0.3,rely=0.58, relwidth=0.62)
    
    #Phone type
    lb9 = Label(labelFrame,text="PhoneType : ", bg='#044F67', fg='white')
    lb9.place(relx=0.05,rely=0.66)
    
    en9 = Entry(labelFrame)
    en9.place(relx=0.3,rely=0.66, relwidth=0.62)

    #Area_code
    lb10 = Label(labelFrame,text="AreaCode : ", bg='#044F67', fg='white')
    lb10.place(relx=0.05,rely=0.74)
    
    en10 = Entry(labelFrame)
    en10.place(relx=0.3,rely=0.74, relwidth=0.62)
    
    #Phone
    lb11 = Label(labelFrame,text="Phone : ", bg='#044F67', fg='white')
    lb11.place(relx=0.05,rely=0.82)
    
    en11 = Entry(labelFrame)
    en11.place(relx=0.3,rely=0.82, relwidth=0.62)

    #Date type
    lb12 = Label(labelFrame,text="DateType : ", bg='#044F67', fg='white')
    lb12.place(relx=0.05,rely=0.88)
    
    en12 = Entry(labelFrame)
    en12.place(relx=0.3,rely=0.88, relwidth=0.62)

    #date
    lb13 = Label(labelFrame,text="Date: ", bg='#044F67', fg='white')
    lb13.place(relx=0.05,rely=0.93)
    
    en13 = Entry(labelFrame)
    en13.place(relx=0.3,rely=0.93, relwidth=0.62)
    
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#5F9EA0', fg='#333945',command=insertUpdateContact)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root,text="Quit",bg='#5F9EA0', fg='#333945',command=root.quit)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)


#################################################################################################################################################


def update():

    global Canvas1,labelFrame,cid_en,lb
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#FFF9C4",width = 120, height = 120)
    Canvas1.pack(expand=False,fill=BOTH) 
        
    labelFrame = Frame(root,bg='#044F67')
    labelFrame.place(relx=0.22,rely=0.01,relwidth=0.6,relheight=0.3)

    lb = Label(labelFrame,text="ContactID : ", bg='#044F67', fg='white')
    lb.place(relx=0.02,rely=0.16)
    
    cid_en = Entry(labelFrame)
    cid_en.place(relx=0.24,rely=0.16, relwidth=0.32)


    SubmitBtn = Button(labelFrame,text="UPDATE",bg='#5F9EA0', fg='#333945',command = addUpdateContact)
    SubmitBtn.place(relx=0.3,rely=0.4, relwidth=0.18,relheight=0.2)


    #SubmitBtn = Button(labelFrame,text="DELETE",bg='#5F9EA0', fg='#333945', command = deleteContact)
    #SubmitBtn.place(relx=0.6,rely=0.4, relwidth=0.18,relheight=0.2)
    ############################################################################################################################################

def UpdateView():
    global Canvas1,labelFrame,SubmitBtn,cid_en
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#FFF9C4",width = 1200, height = 1200)
    Canvas1.pack(expand=False,fill=BOTH) 
        
    labelFrame = Frame(root,bg='#044F67',height=0.9)
    labelFrame.place(relx=0.22,rely=0.01,relwidth=0.6,relheight=0.92)

    lb0 = Label(labelFrame,text="Enter row to modify : ", bg='#044F67', fg='white')
    lb0.place(relx=0.05,rely=0.01)
    
    cid_en = Entry(labelFrame)
    cid_en.place(relx=0.3,rely=0.05, relwidth=0.5)

    SubmitBtn = Button(root,text="SUBMIT",bg='#5F9EA0', fg='#333945',command=addUpdateContact)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

################################################################################################################################################

def DeleteView():
    global Canvas1,labelFrame,SubmitBtn,cid_en
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#FFF9C4",width = 1200, height = 1200)
    Canvas1.pack(expand=False,fill=BOTH) 
        
    labelFrame = Frame(root,bg='#044F67',height=0.9)
    labelFrame.place(relx=0.22,rely=0.01,relwidth=0.6,relheight=0.92)

    lb0 = Label(labelFrame,text="Enter row to delete : ", bg='#044F67', fg='white')
    lb0.place(relx=0.05,rely=0.01)
    
    cid_en = Entry(labelFrame)
    cid_en.place(relx=0.3,rely=0.05, relwidth=0.5)

    SubmitBtn = Button(root,text="SUBMIT",bg='#5F9EA0', fg='#333945',command=deleteContact)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
################################################################################################################################################

def view():

    root = Tk()
    root.title("Contact")
    root.minsize(width=1200,height=300)
    root.geometry("800x800")
    
    y = 0.25


    labelFrame = Frame(root,bg='black')
    canvas = Canvas(labelFrame,width=700,height=600)
    scrollbar = Scrollbar(labelFrame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar.set)

    #labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   

    SubmitBtn = Button(root,text="UPDATE",bg='#5F9EA0', fg='#333945',command = UpdateView)
    SubmitBtn.place(relx=0.3,rely=0, relwidth=0.05,relheight=0.05)


    SubmitBtn = Button(root,text="DELETE",bg='#5F9EA0', fg='#333945', command = DeleteView)
    SubmitBtn.place(relx=0.6,rely=0, relwidth=0.05,relheight=0.05)

    
    Label(labelFrame, text="%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s"%('Fname','Mname','Lname','Address_type','Address','State','Zip','Phone_type','Area_code','Number','Date_type','Date'),bg='black',fg='white').place(relx=0,rely=0.2)
   # Label(labelFrame, text="--------------------------------------------------------------",bg='black',fg='white').place(relx=0.005,rely=0.002)
    
    try:
        cur.execute("SELECT c.Fname,c.Mname,c.Lname,a.Address_type,a.Address,a.State,a.Zip,p.Phone_type,p.Area_code,p.Number,d.Date_type,d.Date FROM contact_table c, address_table a, date_table d, phone_table p \
                                                 WHERE c.Contact_id=a.Contact_id AND a.Contact_id=d.Contact_id AND d.Contact_id=p.Contact_id")

        con.commit()

        for i in cur:


            Label(scrollable_frame, text="%-1s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s%-10s"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11]),bg='black',fg='white' ).pack()

        labelFrame.place(relx=.5, rely=.5, anchor="c")
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    except:
        messagebox.showinfo("Bad Format","Can't fetch files from database")
    
##############################################################################################################################################

def searchdisplay():
    
    srch = en1.get()
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    
    y = 0.25
    
    Label(labelFrame, text="%-10s%-30s%-20s"%('First','Middle','Last'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    
    searchSql = "select Fname,Mname,Lname from contact_table c,address_table a, phone_table p where c.Contact_id = a.Contact_id  AND a.Contact_id = p.Contact_id AND (c.Contact_id = "+srch+" or c.Fname = '"+srch+"' or c.Mname ='"+srch+"' or c.Lname = '"+srch+"' or a.Address='"+srch+"' or p.NUMBER='"+srch+"')"
    try:
        cur.execute(searchSql)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-30s%-20s"%(i[0],i[1],i[2]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
            print(i)
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")

def search():
    global Canvas1,labelFrame,lb1,en1,SearchBtn
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#FFF9C4",width = 1200, height = 1200)
    Canvas1.pack(expand=False,fill=BOTH) 
        
    labelFrame = Frame(root,bg='#044F67',height=0.9)
    labelFrame.place(relx=0.22,rely=0.01,relwidth=0.6,relheight=0.92)

    lb1 = Label(labelFrame,text="Search:", bg='#044F67', fg='white')
    lb1.place(relx=0.15,rely=0.4)

    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.4, relwidth=0.42)

    SubmitBtn = Button(labelFrame,text="SEARCH",bg='#5F9EA0', fg='#333945',command = searchdisplay)
    SubmitBtn.place(relx=0.6,rely=0.5, relwidth=0.2,relheight=0.06)
################################################################################################################################################

Canvas1 = Canvas(root)

Canvas1.config(bg="grey",width = 500, height = 500)

Canvas1.pack(expand=True,fill=BOTH)

    
headingFrame1 = Frame(root,bg="black",bd=5)
headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
headingFrame2 = Frame(headingFrame1,bg="#5F9EA0")
headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
        
headingLabel = Label(headingFrame2, text="CONTACT MENU", bg='#5F9EA0',fg='black')
headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    
    
btn1 = Button(root,text="Add Contact",bg='black', fg='#333945', command = addContact)
btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Search Contact",bg='black', fg='#333945', command = search)
btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Contacts",bg='black', fg='#333945', command = view)
btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Modify Contacts",bg='black', fg='#333945', command = update)
btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    


root.mainloop()  