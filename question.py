import database as db
class Q:
    def ques(self):
        q={
            "What is the output? print('Hello')":'Hello',
            "What is the output? print('Python')":'Python',
            'What is the output? 1**2**2':'1',
            'What is the output? a=5;b=7;print(a+b)':'12',
            'What is the output? print(2**3**2)':'512'
            }
        mark=0
        roll=int(input('Enter your correct roll no to attend exam!:'))
        sql='select rollno from signup'
        db.mycursor.execute(sql)
        f=db.mycursor.fetchall()
        m=False
        for i in f:
            if i[0]==roll:
                m=True
        if m:                
            for i in q:
                print(i)
                a=input('Enter your answer:')
                if a==q[i]:
                    mark+=10
            sql='insert into result(mark,rollno) values(%s,%s)'%(mark,roll)
            db.mycursor.execute(sql)
            db.mydb.commit()
            print(db.mycursor.rowcount,'record inserted ! Go to check result')
        else:
            print('Roll no not exist!')
    def mark(self):
        print('Welcome to Result Page!')
        roll=int(input('Enter your rollno:'))
        password=input('Enter your password:')
        sql='select count(rollno) from signup where rollno=%s and password="%s"'%(roll,password)
        db.mycursor.execute(sql)
        result=db.mycursor.fetchone()
        if result[0]==1:
            uname='select username from signup where rollno=%s'%roll
            db.mycursor.execute(uname)
            result=db.mycursor.fetchone()[0]
            print('Welcome',result)
            
            res='select rollno,mark from result where rollno=%s'%roll
            db.mycursor.execute(res)
            total=db.mycursor.fetchall()
            for i in total:
                print(i,end=' ')
            print('Your marks:',total)
        
        
                
