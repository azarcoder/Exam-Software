import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1538',
    database='t4teq'
) 
mycursor=mydb.cursor()
#mycursor.execute('create table signup(username varchar(30),Rollno int not null primary key,password varchar(8))')
#mycursor.execute('create table result (mark int,Rollno int not null primary key)')


