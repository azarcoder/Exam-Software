import database as db
class S:
    def sign(self):
        while True:
            name=input('Enter your new username:')
            Rollno=input('Enter your Rollno:')
            password=input('Enter the new password (password must be in 8 digits):')
            if len(password)==8:
                print('Password Accepted!')
                values=(name,Rollno,password)
                sql='insert into signup(username,rollno,password) values(%s,%s,%s)'
                db.mycursor.execute(sql,values)
                db.mydb.commit()
                print(db.mycursor.rowcount,'record inserted ! Go to Login.')
                break
            else:
                print('Please enter your password under 8 digits')
                break
    def show(self):
        db.mycursor.execute('SELECT * FROM SIGNUP')
        myresult=db.mycursor.fetchall()
        for i in myresult:
            print(i)
    def drop(self):
        db.mycursor.execute('DELETE FROM SIGNUP')
        db.mydb.commit()
        print('Database all records deleted sucessfully!') 
        
         
