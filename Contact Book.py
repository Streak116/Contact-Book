// Branch 1 updated again
def add_contact():
    
    def save():
        name_entry=name.get()
        num_entry=num.get()
        fname=name_entry+".txt"
        if(os.path.exists('C:\\Users\\Streak\\Desktop\\contact\\all\\'+fname)):
            k=Label(scr1,text="    Contact already exist       ",font=("Arial Bold",20),fg="red")
            k.place(x=75,y=400)
            return
        fp=open('C:\\Users\\Streak\\Desktop\\contact\\all\\'+fname,"w")
        fp.write(name_entry+"\n")
        fp.write(num_entry)
        fp.close()
        L1=Label(scr1,text="Contact Saved Successfully",font=("Arial Bold",20),fg="green").place(x=70,y=400)

    scr1=Toplevel()
    scr1.geometry("500x500")
    name=StringVar()
    num=StringVar()
    lab1=Label(scr1,text="Add Contact",font=("Arial Bold",20),fg="blue").pack()
    lab1=Label(scr1,text="Enter Name",font=("Arial Bold",15)).place(x=100,y=100)
    name_entry=Entry(scr1,textvariable=name)
    name_entry.place(x=250,y=100)
    lab1=Label(scr1,text="Enter Number",font=("Arial Bold",15)).place(x=100,y=200)
    num_entry=Entry(scr1,textvariable=num)
    num_entry.place(x=250,y=200)
    B1=Button(scr1,text = "Save Contact",font=("calibre",15),command=save).place(x=175,y=300)
    B1=Button(scr1,text = "Cancel",font=("calibre",15),command=scr1.destroy).place(x=200,y=350)
    
    mainloop()

def search():
    scr2=Toplevel()
    scr2.geometry("500x500")
    scr2.title('search')

    def seaname():
        un=username.get()
        if (os.path.exists('C:\\Users\\Streak\\Desktop\\contact\\all\\'+un+'.txt')):
            file=open('C:\\Users\\Streak\\Desktop\\contact\\all\\'+un+'.txt','r')
            name=file.readline()
            number=file.readline()
            Label(scr2,text=name,font=("Arial Bold",20)).place(x=100,y=200)
            Label(scr2,text=number,font=("Arial Bold",20)).place(x=300,y=200)
        else:
            Label(scr2,text='Contact Doesn\'t Exits',font=("Arial Bold",20),fg='red').place(x=100,y=230)
            scr2.update()
            sleep(2)
            scr2.destroy()

    '''def seanum():
        un=usernum.get()
        if (os.path.exists('C:\\Users\\Streak\\Desktop\\contact\\all\\'+un+'.txt')):
            file=open('C:\\Users\\Streak\\Desktop\\contact\\all\\'+un+'.txt','r')
            name=file.readline()
            number=file.readline()
            Label(scr2,text=name,font=("Arial Bold",20)).place(x=100,y=200)
            Label(scr2,text=number,font=("Arial Bold",20)).place(x=200,y=200)
        else:
            Label(scr2,text='Contact Doesn\'t Exits',font=("Arial Bold",20)).place(x=100,y=230)
            scr2.update()
            sleep(2)
            scr2.destroy()'''
    
    def byname():
        btn1.destroy()
        #btn2.destroy()
        global username
        global name
        username=StringVar()
        Label(scr2,text='',font=('calibre',16)).pack()
        Label(scr2,text='Enter Name',font=('calibre',16)).pack()
        name=Entry(scr2,textvariable=username,font=('times',15))
        name.pack()
        btn=Button(scr2,text='Search',height=2,width=16,command=seaname).pack()
        #btn=Button(scr2,text='Cancel',height=2,width=16,command=scr2.destroy).pack()
	
	
    '''def bynum():
        btn1.destroy()
        global usernum
        global num
        usernum=StringVar()
        Label(scr2,text='',font=('calibre',16)).pack()
        Label(scr2,text='Enter Number',font=('calibre',16)).pack()
        num=Entry(scr2,textvariable=usernum,font=('times',15))
        num.pack()
        btn=Button(scr2,text='Search',height=2,width=16,command=seanum).pack()'''

    global btn1
    global btn2
    btn1=Button(scr2,text='Search by Name',height=2,width=16,command=byname)
    btn1.pack()
    '''btn2=Button(scr2,text='Search by Number',height=2,width=16,command=bynum)
    btn2.pack()'''
    btn3=Button(scr2,text='Cancel',height=2,width=16,command=scr2.destroy)
    btn3.pack()

    mainloop()

def edit():
    scr2=Toplevel()
    scr2.geometry("500x500")
    lab1=Label(scr2,text="Edit Contact",font=("Arial Bold",20),fg="blue").pack()
    
    def edit_name():
        un=username.get()
        fname=un+".txt"
        if (os.path.exists('C:\\Users\\Streak\\Desktop\\contact\\all\\'+fname)):
            file=open('C:\\Users\\Streak\\Desktop\\contact\\all\\'+fname,'r')
            nw=newname.get()
            nwfname=nw+".txt"
            name=file.readline()
            number=file.readline()
            fp=open('C:\\Users\\Streak\\Desktop\\contact\\all\\'+nwfname,"w")
            fp.write(nw+"\n")
            fp.write(number)
            file.close()
            os.remove('C:\\Users\\Streak\\Desktop\\contact\\all\\'+fname)
            Label(scr2,text="Name changed Successfully",font=("Arial Bold",20),fg='blue').place(x=70,y=300)
        else:
            Label(scr2,text='Contact Doesn\'t Exits',font=("Arial Bold",20),fg="red").place(x=100,y=300)
            scr2.update()
            sleep(2)
            scr2.destroy()

    def edit_number():
        un=username.get()
        fname=un+".txt"
        if (os.path.exists('C:\\Users\\Streak\\Desktop\\contact\\all\\'+fname)):
            file=open('C:\\Users\\Streak\\Desktop\\contact\\all\\'+fname,'r')
            name=file.readline()
            number=newnum.get()
            file.close()
            os.remove('C:\\Users\\Streak\\Desktop\\contact\\all\\'+fname)
            file=open('C:\\Users\\Streak\\Desktop\\contact\\all\\'+fname,"w")
            file.write(un+"\n")
            file.write(number)
            file.close()
            
            Label(scr2,text="Number changed Successfully",font=("Arial Bold",20),fg='blue').place(x=60,y=300)
        else:
            Label(scr2,text='Contact Doesn\'t Exits',font=("Arial Bold",20),fg="red").place(x=100,y=300)
            scr2.update()
            sleep(2)
            scr2.destroy()
            
    def ed_name():
        btn1.destroy()
        btn2.destroy()
        global username
        global name
        global newname
        username=StringVar()
        newname=StringVar()
        Label(scr2,text='',font=('calibre',16)).pack()
        Label(scr2,text='Enter Name',font=('calibre',16)).pack()
        name=Entry(scr2,textvariable=username,font=('times',15))
        name.pack()
        Label(scr2,text='Enter New Name',font=('calibre',16)).pack()
        new_name=Entry(scr2,textvariable=newname,font=('times',15))
        new_name.pack()
        btn=Button(scr2,text='Search',height=2,width=16,command=edit_name).pack()
    
    def ed_num():
        btn1.destroy()
        btn2.destroy()
        global username
        global name
        global newnum
        username=StringVar()
        newnum=StringVar()
        Label(scr2,text='',font=('calibre',16)).pack()
        Label(scr2,text='Enter Name',font=('calibre',16)).pack()
        name=Entry(scr2,textvariable=username,font=('times',15))
        name.pack()
        Label(scr2,text='Enter New Number',font=('calibre',16)).pack()
        name=Entry(scr2,textvariable=newnum,font=('times',15))
        name.pack()
        btn=Button(scr2,text='Search',height=2,width=16,command=edit_number).pack()



    global btn1
    global btn2
    btn1=Button(scr2,text='Edit Name',height=2,width=16,command=ed_name)
    btn1.pack()
    btn2=Button(scr2,text='Edit Number',height=2,width=16,command=ed_num)
    btn2.pack()
    btn3=Button(scr2,text='Cancel',height=2,width=16,command=scr2.destroy)
    btn3.pack()

    mainloop()

def del_contact():
    
    def delete():
        name_entry=name.get()
        fname=name_entry+".txt"
        if(os.path.exists('C:\\Users\\Streak\\Desktop\\contact\\all\\'+fname)==False):
            k=Label(scr1,text="    Contact Does not exist       ",font=("Arial Bold",20),fg="red")
            k.place(x=75,y=400)
        else:
            os.remove('C:\\Users\\Streak\\Desktop\\contact\\all\\'+fname)
            L1=Label(scr1,text="Contact Deleted Successfully",font=("Arial Bold",20),fg="green").place(x=70,y=400)

    
    scr1=Toplevel()
    scr1.geometry("500x500")
    name=StringVar()
    
    lab1=Label(scr1,text="Delete Contact",font=("Arial Bold",20),fg="blue").pack()
    lab1=Label(scr1,text="Enter Name of the contact to be deleted",font=("Arial Bold",17)).place(x=40,y=100)
    name_entry=Entry(scr1,textvariable=name,font=('times',15))
    name_entry.place(x=150,y=200)
    B1=Button(scr1,text = "Delete Contact",font=("calibre",15),command=delete).place(x=175,y=250)
    B1=Button(scr1,text = "Cancel",font=("calibre",15),command=scr1.destroy).place(x=210,y=300)
    mainloop()

def view():
    scr2=Toplevel()
    scr2.geometry("500x500")
    scroll1=Scrollbar(scr2,orient=VERTICAL,width=20)
    scroll1.pack(side=LEFT,fill=Y)
    scroll2=Scrollbar(scr2,orient=VERTICAL,width=20)
    scroll2.pack(side=RIGHT,fill=Y)
    mylist1=Listbox(scr2,bg='light blue',fg='red',font=("Arial Bold",15),yscrollcommand=scroll1.set)
    mylist2=Listbox(scr2,bg='pink',fg='green',font=("Arial Bold",15),yscrollcommand=scroll2.set)
    lab1=Label(scr2,text="List of Contacts",font=("Arial Bold",20),fg="blue").pack()
    lab2=Label(scr2,text="NAME",font=("Arial Bold",16)).place(x=75,y=60)
    lab3=Label(scr2,text="NUMBER",font=("Arial Bold",16)).place(x=275,y=60)
    i=0
    for file in os.listdir('C:\\Users\\Streak\\Desktop\\contact\\all\\'):
        i=i+1
        
        if (file.endswith(".txt")):
            fp=open('C:\\Users\\Streak\\Desktop\\contact\\all\\'+file,'r')
            name=fp.readline()
            num=fp.readline()
            mylist1.insert(END,str(i)+') '+name)
            mylist2.insert(END,str(i)+') '+num)
    
        fp.close()

    mylist1.place(x=25,y=100)
    mylist2.place(x=225,y=100)
    scroll1.config(command=mylist1.yview)
    scroll2.config(command=mylist2.yview)
            
    mainloop()
    
if __name__=='__main__':
    from tkinter import *
    import os
    from time import *
    import turtle as tt
    
    w=tt.Screen()
    let=tt.Turtle()
    w.bgcolor('light green')
    let.penup()

    let.goto(-180,60)
    let.pendown()
    let.pencolor('red')
    let.pensize(8)
    let.left(135)
    let.circle(30,270)
    let.penup()
    let.goto(-120,20)
    let.pendown()

    let.circle(30)
    let.penup()

    let.goto(-100,12)
    let.pendown()
    let.left(45)
    let.forward(58)
    let.right(140)
    let.forward(75)
    let.left(140)
    let.forward(58)
    let.penup()

    let.goto(-20,12)
    let.pendown()
    let.forward(60)
    let.left(90)
    let.forward(20)
    let.backward(40)
    let.penup()

    let.goto(3,12)
    let.pendown()
    let.right(110)
    let.forward(66)
    let.right(135)
    let.forward(66)
    let.penup()

    let.goto(10,35)
    let.pendown()
    let.left(66)
    let.forward(35)
    let.penup()

    let.goto(110,65)
    let.pendown()
    let.left(135)
    let.circle(30,270)
    let.penup()

    let.goto(140,13)
    let.pendown()
    let.left(45)
    let.forward(60)
    let.left(90)
    let.forward(20)
    let.backward(40)
    let.penup()


    let.goto(165,-13)
    let.write('S',move=True,font=('Arial',72))
    sleep(4)
    tt.Screen().bye()

    top=Tk()
    top.geometry("500x500")
    Label(text = "Contact Book",font=("Arial Bold",25),fg="red").pack()
    Label(text = "").pack()
    Label(text = "").pack()
    Label(text = "").pack()
    Label(text = "").pack()
    B1=Button(text = "Add Contact",font=("calibre",15),command=add_contact).pack()
    Label(text = "").pack()
    B2=Button(text = "Search Contact",font=("calibre",15),command=search).pack()
    Label(text = "").pack()
    B3=Button(text = "Edit Contact",font=("calibre",15),command=edit).pack()
    Label(text = "").pack()
    B4=Button(text = "Delete Contact",font=("calibre",15),command=del_contact).pack()
    Label(text = "").pack()
    B5=Button(text = "View Contacts",font=("calibre",15),command=view).pack()
    Label(text = "").pack()
    B6=Button(text = "Exit",font=("calibre",15),command=top.destroy).pack()
    mainloop()
