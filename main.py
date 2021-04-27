import Signup
import Login
while True:
    print('1.Signup\n2.Login\n3.Show database\n4.Delete all records\n5.Exit')
    n=int(input('Enter your choice:'))
    try:
        if  n==1:
            sp=Signup.S()
            sp.sign()
        elif n==2:
            lg=Login.L()
            lg.log()
        elif n==3:
            sp=Signup.S()
            sp.show()
        elif n==4:
            n=input('Enter the password to delete records!:')
            if n=='1538':
                sp=Signup.S()
                sp.drop()
            else:
                print('Password incorrect! Please contact Admin')
        else:
            break
    except:
        print('Enter the correct input!')
