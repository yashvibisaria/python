#---------------------------------Mysql------------------------------------------
#Mysql is not inbuilt database. it is an external database which we have to download, set user n password.
#connect here throught that and then we code. but Mysql is very and can hold lot of data. slite3 it is inbuilt in python but hold small data. 
#but qeries create table, insert, uodate, select, fetchall fun, delete all code is same as sqlite

#only two things are different
#1. connect part is different 
#2. wherever  we use ? in sqlite we use %s in mysql

import mysql.connector # install this in command prompt using the command pipinstall mysql-connector-python
# when we connect we need host, user, and password. All these 3 things we set when we install mysql
con=mysql.connector.connect(host="localhost", user="username", password="password", database="databasename")
    
from tkinter import *

screen=Tk()
screen.configure(bg="gray")
screen.geometry("600x600")

# Sqlite is a database which is used to store data, it is an inbuilt database which is already there inside python 
# There are many databases such as mysql, oracle, sqlite etc.. they all use one language called as sql language 
# sql is a coding language used for the database coding 
# sqlite is in the form of library so we have to import library at the top. Although we don't have to install it, saving our time, but 
# sqlite will store a limited data as it is a small database, If we want to store millions of data then we have to use big databases such as 
# mysql. Mysql is not there in python so we have to install it and then connect with python which might be a time taking thing
# Although sqlite doesn't mean installation, it can only store small data.
# Mysql needs installation and it can store large data.
# They all store data in the form of table. So we first have to create table, and then can do the basic things after creating table, like saving data
# into the table from the entry boxes, updating the data, deleting the data, getting data from the database on screen (example: if we are searching
# something, then there it goes to the database and get that detail and shows on screen)

# 5 main queries are: create a table, insert data in table, updating the data, getting the details, 

# Steps to use sqlite: 
# 1. import sqlite at top 
# 2. use connect function to conect with database 
# 3. create cursor object whcih will help later to execute all queries 
# 4. use query to create table 
# 5. inserting data into the database 
# 6. get/search the data
# 7. update the data 
# 8. delete the data 

csrs=con.cursor() # cursor executes all the queries once all these queries are written we have to use the cursor to execute them

# create table: here we have to give a table name and columns which will have a data type
# varchar is a datatype which accepts all characters like int, string, special characters. Same as string in python 
sql="""
create table if not exists emp(
Staff_no integer, 
f_name text,
l_name text,
gender text,
doj varchar(100) 
)
"""
csrs.execute(sql) # here we created a query in a sql variable and giving it to the cursor to execute 
con.commit() # commit is to save everything permanently and is used after every query 


def add():
    # using get function we will get the data from entry box to a variable and pass that variable and give the variable to insert query that
    # will insert the data into the table. Directly we cannot give the variables to insert query so we use ? temporarily and later on give the
    # variable names 
    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=e4.get()
    e=e5.get()
    sql="""
    insert into emp(Staff_no, f_name, l_name, gender, doj) values(%s,%s,%s,%s,%s)


"""
    csrs.execute(sql, (a,b,c,d,e))
    con.commit()

def getdetails():
    # here we can search anyones details stored. We will first enter the ID in the search box the employee who's detail we want to see and
    # get that detail in a variable. Then we use a select query whose work is to select a data and we pass this variable to this query
    # so that it can select only that person's detail whose ID is given in search box. Then we use fetchall function to fetch the selected data
    # then we use the label and forloop to display on screen
    a=e6.get()
    sql="""
    select * from emp where Staff_no=%s

"""
    csrs.execute(sql, (a,))
    f=csrs.fetchall()
    r=""
    for i in f:
        r+=str(i[0])+"\n"+i[1]+"\n"+i[2]+"\n"+i[3]+"\n"+i[4]+"\n" #\n is for new line
    l6.config(text=r)
    con.commit()

def delete():
    #so e6 is where we entry Staff_no whcih detail we want to delete
    s=e6.get()
    csrs.execute("delete from emp where Staff_no=%s", (s,)) #sis having detail of employee wich  we want to delete
    con.commit()

def edit():
    #use update to update. get all data from second input entryboxes and give to update so it can update
    a=e11.get() # set word is used to update and we write column names=value. directly we cannot give value so we use ? and later pass teh actual froma, b, c, d, e
    b=e12.get()
    c=e13.get()
    d=e14.get()
    e=e15.get()
    r=e6.get()
    sql="""update emp set Staff_no=%s, f_name=%s, l_name=%s, gender=%s, doj=%s where Staff_no=%s """
    csrs.execute(sql, (a, b, c, d, e, r)) # pass data here combine with sql query
    con.commit()
def update():
    global e11, e12, e13, e14, e15
    #to create second screen, where all 5 labels, 5 entrybox will eb shown  which are shown on first screen
    #but we will use select and fetchall to get data and inseet into entrybox
    s2=Tk()
    l1=Label(s2, text="Staff Number", bg="gray")
    l1.grid(row=1, column=1)

    l2=Label(s2, text="First Name", bg="gray")
    l2.grid(row=2, column=1)

    l3=Label(s2, text="Last Name", bg="gray")
    l3.grid(row=3, column=1)

    l4=Label(s2, text="Gender", bg="gray")
    l4.grid(row=4, column=1)

    l5=Label(s2, text="Date of Joining", bg="gray")
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
    select * from emp where Staff_no=%s

"""
    csrs.execute(sql, (a,))
    f=csrs.fetchall()
    con.commit()
    # we will user insert func to add data in entrybox. f is list. to get data from list
    # for loop we use 
    for a in f:
        e11.insert(0, a[0]) # in f position or index no start from 0, 1, 2, 3, 4...
        e12.insert(0, a[1])
        e13.insert(0, a[2])
        e14.insert(0, a[3])
        e15.insert(0, a[4])
    


#-------------------------------------------first screen------------------------------
l1=Label(screen, text="Staff Number", bg="gray")
l1.grid(row=1, column=1)

l2=Label(screen, text="First Name", bg="gray")
l2.grid(row=2, column=1)

l3=Label(screen, text="Last Name", bg="gray")
l3.grid(row=3, column=1)

l4=Label(screen, text="Gender", bg="gray")
l4.grid(row=4, column=1)

l5=Label(screen, text="Date of Joining", bg="gray")
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

b1=Button(screen, text="Add record to database", bg="grey", command=add)
b1.grid(row=6, column=1, columnspan=2)

b2=Button(screen, text="Search the database", bg="grey", command=getdetails)
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
#-------------------------------Assignment--------------------------------------------------
# create a student app with ID, student name, marks, class, phone number. Create label and entrybox for each. Create for buttons add, query, 
# update, delete. Connect with database, create table, do add function, create getdetails function,update function, eidt and delete function as well.