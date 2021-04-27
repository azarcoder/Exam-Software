import mysql.connector
mydb=mysql.connector.connect(
    host='HOSTNAME',
    user='USERNAME',
    password='XXXX YOUR DATABASE PASSWORD HERE XXXX',
    database='XXXX YOUR DATABASE NAME HERE XXXX '
) 
mycursor=mydb.cursor()
#mycursor.execute('create table signup(username varchar(30),Rollno int not null primary key,password varchar(8))')
#mycursor.execute('create table result (mark int,Rollno int not null primary key)')


