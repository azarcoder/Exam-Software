import database as db
import question as qs
class L:
    def log(self):
        while True:
            print('1.Login as student\n2.login as staff\n3.exit()')
            a=int(input('Enter your choice:'))
            if a==1:
                print('Welcome to student login!')
                roll=int(input('Enter your roll no:'))
                password=input('Enter your password:')
                sql='select count(rollno) from signup where rollno=%s and password="%s"'%(roll,password)
                db.mycursor.execute(sql)
                result=db.mycursor.fetchone()
                if result[0]==1:
                    sql='select username from signup where rollno=%s'%roll
                    db.mycursor.execute(sql)
                    result=db.mycursor.fetchone()[0]
                    print('Welcome',result)                    
                    print('1.Attend Exam\n2.Report\n3.Logout()')
                    s=int(input('Enter the choice'))
                    if s==1:
                        q=qs.Q()
                        q.ques()
                    elif s==2:
                        w=qs.Q()
                        w.mark()
                    else:
                        break
                else:
                    print('Account not found')
            elif a==2:
                print('Welcome to Staff login!')
                user='t4teq'
                p='123'
                u=input('Enter your college id no:')
                pa=input('Enter your password:')
                if user in u and p in pa:
                    print('Welcome',u)
                    while True:
                        print('1.Watch all exam result\n2.Delete data\n3.Logout')
                        n=int(input('Enter your choice:'))
                        if n==1:
                           sql='select rollno,mark from result'
                           db.mycursor.execute(sql)
                           r=db.mycursor.fetchall()
                           for i in r:
                               print(i)
                        elif n==2:
                            sql='truncate table result'
                            db.mycursor.execute(sql)
                            print('All data deleted successfully!')
                        else:
                            break
                else:
                    print('Please check your id and password!')
                    
            elif a==3:
                break
            else:
                print('Incorrect Input please try again!')
                break
