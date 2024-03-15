def ATM():
    username=["ramteja","kishore","santosh","sivaji","ravikumar"]
    password=["ramteja123","kishore123","santosh12","sivaji123","ravikumar123"]
    pin=[1111,2222,3333,4444,5555]
    bal=[1000,2000,3000,4000,4900]
    print("Enter the Username : ")
    userid=input() 
    if userid in username:
        ind=username.index(userid)
        print("Enter Password : ")
        passid=input()
        flag=0
        if passid != password[ind]:
            print("Password Wrong 2 more Chances")
            print("ReEnter Password : ")
            passid=input()
            if passid != password[ind]:
                print("Password Wrong 1 more chances")
                print("ReEnter Password : ")
                passid=input()
                if passid != password[ind]: 
                    print("Account blocked")
                else:
                    flag=1
            else:
                flag=1
        else:
            flag=1
        if flag==0:
            print("__________End__________")
            exit()
        else:
            print("1.Withdraw")
            print("2.Deposit")
            print("3.CheckBalance")
            print("4.Change Password")
            print("Enter your choice : ")
            while(1):
                choice=int(input())
                if choice in [1,2,3,4]:
                    break
                else:
                    print("Plesae Enter Valid Choice,ReEnter Choice")
            if(choice==1):
                withdraw(bal,ind,pin)
            elif(choice==2):
                deposit(bal,ind,pin,username)
            elif(choice==3):          
                checkbalance(pin,ind,bal)
            elif(choice==4):
                changepassword(pin,ind)
    else:
        print("Invalid User")
        exit()

def withdraw(bal,ind,pin):                      
    print("Enter the Amount of Withdrawl : ")
    with1=int(input())
    print("Enter pin : ")
    pinid=int(input())
    if pinid==pin[ind]:
        if with1<=bal[ind]:
            bal[ind]=bal[ind]-with1
            print("Collect You Amount ",with1)
            response(bal,ind)
        else:
            print("Insufficient Balance")
    else:
        print("Invalid Pin")
        print("__________End__________")
        exit()  
def deposit(bal,ind,pin,username):
                print("Enter the Amount of Deposit : ")
                deposit1=int(input())
                print("Enter pin : ")
                pinid=int(input())
                if pinid==pin[ind]:
                    bal[ind]=bal[ind]+deposit1
                    print("Amount ",deposit1," is Added to your account ",username[ind])
                    response(bal,ind)
                else:
                    print("Invalid Pin")
                    print("__________End__________")
                    exit()
def checkbalance(pin,ind,bal):
                print("Enter pin : ")
                pinid=int(input())
                if pinid==pin[ind]:
                    response(bal,ind)
                else:
                    print("Invalid Pin")
                    print("__________End__________")
                    exit()
def changepassword(pin,ind):
    print("Password Change Process : ")
    print("Enter pin : ")
    pinid=int(input())
    if pinid==pin[ind]:
        print("Your password must contain a capital letter,a small leter, a number , a special symbol")
        print("Enter New Password : ")
        while(1):
            newpass=input()
            if strongpassword(newpass)=="strongpasscode":
                break
            else:
                print("ReEnter the passward on above given conditions")
        print("Confirm Password : ")
        while(1):
            conpass=input()
            if(newpass==conpass):
                print("Password you entered is Strong")
                print("Password of account has been Updated Sucessfully")
                break
            else:
                print("Please Reenter the Confrim Password correctly")
    else:
        print("Invalid Pin")
        print("___________End__________")
        exit()
def response(bal,ind):
    print("Check Your Balance (yes or no) :")
    while(1): 
        resp=input()
        if(resp=="yes"):
            print("Current Balance : ",bal[ind])
            break
        elif(resp=="no"):
            print("Thank You!")
            print("__________End__________")
            exit()
        else:
            print("Please Enter Any of Above 2 options")   
def strongpassword(newpass):
    a,b,c,d="","","",""
    uc,lc,dg,sp=0,0,0,0
    for i in newpass:
        if(i.isupper()):
            a=a+i
            uc=uc+1
        elif(i.islower()):
            b=b+i
            lc=lc+1
        elif(not i.isalnum() and i!=" "):
            c=c+i
            sp=sp+1
        elif(i.isdigit()):
            d=d+i
            dg=dg+1
    if len(newpass)>=8:
        if uc>=1 and lc>=1 and dg>=1 and sp>=1:
            return "strongpasscode"
        else:
            print("Weak password")
            if uc>=1 and lc==0 and dg==0 and sp==0:
                print("Still Your Password doesn't contain a Small letter,Number,Special symbol.")
            elif uc==0 and lc>=1 and dg==0 and sp==0 :
                print("Still Your Password doesn't contain a Capital letter,Number,Special symbol.")
            elif uc==0 and lc==0 and dg>=1 and sp==0:
                print("Still Your Password doesn't contain a a Capital letter,Small letter,Special symbol.")
            elif uc==0 and lc==0 and dg==0 and sp>=1:
                print("Still Your Password doesn't contain a Capital letter,Small letter,Number.")
            elif uc>=1 and lc>=1 and dg==0 and sp==0:
                print("Still Your Password doesn't contain a Number,Special symbol.")
            elif uc>=1 and lc==0 and dg>=1 and sp==0:
                print("Still Your Password doesn't contain a Small letter,Special symbol.")
            elif uc>=1 and lc==0 and dg==0 and sp>=1:
                print("Still Your Password doesn't contain a Small letter,Number.")
            elif uc==0 and lc>=1 and dg>=1 and sp==0:
                print("Still Your Password doesn't contain a Capital letter,Special symbol.")
            elif uc==0 and lc>=1 and dg==0 and sp>=1:
                print("Still Your Password doesn't contain a Capital letter,Number.")
            elif uc==0 and lc==0 and dg>=1 and sp>=1:
                print("Still Your Password doesn't contain a Capital letter,Small letter.")
            elif uc>=1 and lc>=1 and dg>=1 and sp==0:
                print("Still Your Password doesn't contain a Special symbol.")
            elif uc>=1 and lc==0 and dg>=1 and sp>=1:
                print("Still Your Password doesn't contain a Small letter.")
            elif uc>=1 and lc>=1 and dg==0 and sp>=1:
                print("Still Your Password doesn't contain a Number.")
            elif uc==0 and lc>=1 and dg>=1 and sp>=1:
                print("Still Your Password doesn't contain a Capital letter.")
    else:
        print("Password must contain 10 letters",10-len(newpass)," Remaining")
ATM()