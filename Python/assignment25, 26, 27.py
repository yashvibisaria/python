from tkinter import *
import sqlite3

screen=Tk()
screen.configure(bg="gray")
screen.geometry("600x600")


con=sqlite3.connect("database.db")
csrs=con.cursor() 
sql="""
create table if not exists school(
Id integer, 
name text,
class integer,
marks integer,
phone_number integer
)
"""
csrs.execute(sql)  
con.commit() 

# We cannot directly pass variables to the queries in which our data is there because when we pass variables it becomes text as all th equeries 
# are written in quotation marks so rather than passing variables directly in query we pass question mark (?) a temporary sign in place
# of variables/data and later on when we execute we pass those variables where data is there 

def add():
    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=e4.get()
    e=e5.get()
    sql="""
    insert into school(Id, name, class, marks, phone_number) values(?,?,?,?,?)


"""
    csrs.execute(sql, (a,b,c,d,e))
    con.commit()

def getdetails():

    a=e6.get()
    sql="""
    select * from school where ID=?

"""
    csrs.execute(sql, (a,))
    f=csrs.fetchall()
    r=""
    for i in f:
        r+=str(i[0])+"\n"+i[1]+"\n"+str(i[2])+"\n"+str(i[3])+"\n"+str(i[4])+"\n" 
    l6.config(text=r)
    con.commit()

def delete():
    s=e6.get()
    csrs.execute("delete from school where Id=?", (s,)) 
    con.commit()

def edit():
    a=e11.get() 
    b=e12.get()
    c=e13.get()
    d=e14.get()
    e=e15.get()
    r=e6.get()
    sql="""update school set Id=?, name=?, class=?, marks=?, phone_number=? where Id=? """
    csrs.execute(sql, (a, b, c, d, e, r))
    con.commit()
def update():
    global e11, e12, e13, e14, e15
    s2=Tk()
    l1=Label(s2, text="ID", bg="gray")
    l1.grid(row=1, column=1)

    l2=Label(s2, text="Name", bg="gray")
    l2.grid(row=2, column=1)

    l3=Label(s2, text="Class", bg="gray")
    l3.grid(row=3, column=1)

    l4=Label(s2, text="Marks", bg="gray")
    l4.grid(row=4, column=1)

    l5=Label(s2, text="Phone Number", bg="gray")
    l5.grid(row=5, column=1)

    s1=StringVar()
    e11=Entry(s2, width=15, bg="white", textvariable=s1)
    e11.grid(row=1, column=2, ipadx=10)

    s6=StringVar()
    e12=Entry(s2, width=15, bg="white", textvariable=s6)
    e12.grid(row=2, column=2, ipadx=10)

    s3=StringVar()
    e13=Entry(s2, width=15, bg="white", textvariable=s3)
    e13.grid(row=3, column=2, ipadx=10)

    s4=StringVar()
    e14=Entry(s2, width=15, bg="white", textvariable=s4)
    e14.grid(row=4, column=2, ipadx=10)

    s5=StringVar()
    e15=Entry(s2, width=15, bg="white", textvariable=s5)
    e15.grid(row=5, column=2, ipadx=10)

    b8=Button(s2, text="update/edit", command=edit)
    b8.grid(row=7, column=1)

    a=e6.get()
    sql="""
    select * from school where Id=?

"""
    csrs.execute(sql, (a,))
    f=csrs.fetchall()
    con.commit()
   
    for a in f:
        e11.insert(0, a[0]) 
        e12.insert(0, a[1])
        e13.insert(0, a[2])
        e14.insert(0, a[3])
        e15.insert(0, a[4])
    

l1=Label(screen, text="ID", bg="gray")
l1.grid(row=1, column=1)

l2=Label(screen, text="Name", bg="gray")
l2.grid(row=2, column=1)

l3=Label(screen, text="Class", bg="gray")
l3.grid(row=3, column=1)

l4=Label(screen, text="Marks", bg="gray")
l4.grid(row=4, column=1)

l5=Label(screen, text="Phone Number", bg="gray")
l5.grid(row=5, column=1)

s1=StringVar()
e1=Entry(screen, width=15, bg="white", textvariable=s1)
e1.grid(row=1, column=2, ipadx=10)

s6=StringVar()
e2=Entry(screen, width=15, bg="white", textvariable=s6)
e2.grid(row=2, column=2, ipadx=10)

s3=StringVar()
e3=Entry(screen, width=15, bg="white", textvariable=s3)
e3.grid(row=3, column=2, ipadx=10)

s4=StringVar()
e4=Entry(screen, width=15, bg="white", textvariable=s4)
e4.grid(row=4, column=2, ipadx=10)

s5=StringVar()
e5=Entry(screen, width=15, bg="white", textvariable=s5)
e5.grid(row=5, column=2, ipadx=10)

b1=Button(screen, text="Add record", bg="grey", command=add)
b1.grid(row=6, column=1, columnspan=2)

b2=Button(screen, text="Search", bg="grey", command=getdetails)
b2.grid(row=7, column=1, columnspan=2)

b3=Button(screen, text="Update", bg="grey", command=update)
b3.grid(row=8, column=1, columnspan=2)

b4=Button(screen, text="Delete", bg="grey", command=delete)
b4.grid(row=9, column=1, columnspan=2)

s7=StringVar()
e6=Entry(screen, width=15, bg="white", textvariable=s7)
e6.grid(row=10, column=1)

l6=Label(screen, bg="gray")
l6.grid(row=11, column=1)

mainloop()
