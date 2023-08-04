class Owner:
    def __init__(self):
        self.name="owner"
        self.owner_check()

    def owner_check(self):
        file1=open("Owner_password.txt","r")
        old_password=file1.read( )
        a=1
        while(a<=3):
            owner_pass = input("\nEnter the password:")
            if (owner_pass == old_password):
                print("\n\nUNLOCKED SUCCESSFULLY\n\n")
                print("hello",self.name)
                self.owner_menu()
                a=5
            else:
                a+=1            
        else:
            if(a==4):
                print("enter valid password")
    
    def owner_menu(self):
        user_input=int(input('''how can i help you???
                   1. View Receipts
                   2. Check customer data
                   3. Reset Password
                   4. EXIT'''))
        if (user_input==1):
            self.view_receipts()
            self.owner_menu()
        elif(user_input==2):
            self.check_customer_data()
            self.owner_menu()
        elif(user_input==3):
            self.reset_password()
            self.owner_menu()
        elif(user_input==4):
            print("thank you!!!!")
    
    def view_receipts(self):
        print("--------------VIEW RECEIPTS---------------")
        f=open("Receipts.txt","r")
        re_ch=0
        while re_ch==0:
            choicex=int(input("\n1.All receipts\n\n2.View selected receipt\n\n3.for menu\n\nEnter your choice: "))
            if choicex==1:  
                print(f.read())
                re_ch=1
                self.owner_menu()
            elif choicex==2:
                work_id=input("enter work id:")
                for line in f:
                    if line.strip("\n").startswith(work_id):
                        print("\n")
                        print("Work_id     Name          Address      Device    Order        Cost(Rupees)")
                        print(line)  
                        re_ch=1
                        self.owner_menu()                        
                else:
                    print("data not found")
                    re_ch=0
            elif choicex==3:
                self.owner_menu()
            else:
                print("INVALID INPUT!!\nEnter correct choice")
                re_ch=0
    
    def check_customer_data(self):
        print("-------------CUSTOMER DATA-------------")
        f=open("Customer_Data.txt","r")
        cu_da=0
        while cu_da==0:
            choicex=input("\n1.View all customer's data\n\n2.View selected customer data\n\n3.for menu\n\nEnter your choice: ")
            if choicex=='1':
                print(f.read())
                cu_da=1
            elif choicex=='2':
                cust_name=input("\nEnter name of the customer: ")
                for line in f:
                    if line.strip("\n").startswith(cust_name):
                        print("\n")
                        print("Cust_name     Address    Phone No.")
                        print(line)
                        cu_da=1
                        break
                else:
                    print("\nData not found!!")
                    cu_da=0  

            elif choicex=='3' :
                self.owner_menu() 
            else:
                print("Enter the correct choice!!")
                cu_da=0

    def reset_password(self):
        print("--------Reset Password--------")
        file1=open("Owner_password.txt","r")
        old_password=file1.read()
        file1.close()
        rp=0
        while rp==0:
            password=input("Enter Old Password:")
            if password==old_password:
                c=0
                while c<3:
                    new_password=input("Enter New Password:")
                    if len(new_password)>=5:
                        file2=open("Owner_password.txt","w")
                        file2.write(new_password)
                        c=4
                        rp=1
                        file2.close()
                    else:
                        print("Enter the new password with minimum length of 5!!")
                        c+=1
            else:
                print("enter correct password!!")
                rp=0

class Customer:
    def __init__(self):
        self.employee_menu()
    
    def employee_menu(self):
        employee_input=int(input("\n1.Customer login(To check work status)\n\n2.New Registration\n\nEnter your choice: "))
        if (employee_input==1):
            self.customer_login()
            self.employee_menu()
        elif(employee_input==2):
            self.new_registration()
            self.employee_menu()
        elif(employee_input==3):
            print("thank you!!!!")

    def customer_login(self):
        print("--------Customer Login--------")
        cust_id_input=input("\nEnter your customer username: ")
        f0=open("Customer_login.txt","r")
        for i in f0:
            if cust_id_input==i.split(",")[0]:
                    nn1=1
                    while nn1<=3:
                                cust_pass=input("\nEnter password: ")
                                if cust_pass==i.split(",")[1]:
                                    print("\n\nUNLOCKED SUCCESSFULLY")
                                    work_id=input("Enter your work id: ")
                                    with open("Done_works.txt", "r") as t:  
                                        for line in t:
                                            if  line.strip("\n").startswith(work_id):
                                                print("\n")
                                                print(line)
                                                print("Your work has been done")
                                                nn1=4
                                        else:
                                                print("Your work is pending!!")     
                                else:
                                    print("Incorrect Password!!")
                                    nn1+=1
                    if nn1>3:           
                        print("3 Incorrect Trials!!")
                        print("Returning to main Menu")


    def new_registration(self):
         
        print("--------NEW REGISTRATION--------")
        cust_name = str(input("\nEnter your name - "))
        cust_address = input("\nEnter your Address - ")
        qqw=0
        while valid_phone==0:
            phone_number = input("\nEnter your Phone Number - ")
            if phone_number.isdigit():
                if len(phone_number)==10:
                    pn=str(phone_number)
                    valid_phone=1
                else:
                    print("PHONE NUMBER IS NOT OF 10 DIGITS!!")
                    valid_phone=0
            else:
                print("INVALID")
                valid_phone=0
        cuust_id=input("\nGenerate your customer username: ")
        cuust_pass=input("\nGenerate your password: ")
        f2=open("Customer_Data.txt","a+")
        f2.write("\n")
        f2.write(cust_name)
        f2.write("  ")
        f2.write(cust_address)
        f2.write("  ")
        f2.write(pn)
        f2.close()
        f111=open("Customer_login.txt","a+")
        f111.write("\n")
        f111.write(cuust_id)
        f111.write(", ")
        f111.write(cuust_pass)
        f111.close()
        print("\nREGISTRATION COMPLETED SUCCESSFULLY")
        print("\n Remember your customer username and password for future reference!!")

        from random import choice
        from itertools import permutations
        while True:
            v = choice(list(permutations('0123456789', 4)))
            if v[0] != '0':
                break
            work_id=''.join(v)

        company=input("enter name of the company")
        type_of_device=input("enter type of device (mobile or laptop)")
        order=input("service you want to do")
        if(type_of_device=='laptop'):
            days=2
        else:
            days=1
        if(order=='service' and type_of_device=='laptop'):
            cost=3000
        elif(order=='service' and type_of_device=='mobile'):
            cost=2000
        elif(order=='repair' and type_of_device=='laptop'):
            cost=4000
        elif(order=='repair' and type_of_device=='mobile'):
            cost=3500

        """ here it will append new custoner data in receipts file which is only accessed by owner only ......"""


        fpp1=open("Receipts.txt","a+")
        fpp1.write(work_id)
        fpp1.write("    ")
        fpp1.write(cust_name)
        fpp1.write("     ")
        fpp1.write(cust_address)
        fpp1.write("      ")
        fpp1.write(type_of_device)
        fpp1.write("   ")
        fpp1.write(order)
        fpp1.write("       ")
        fpp1.write(cost)
        fpp1.close()
  
        """ here it will append new custoner data in pending_works file......"""  
    
        f8=open("Pending_works","a+")
        f8.write(work_id)
        f8.write("    ")
        f8.write(company)
        f8.write("     ")
        f8.write(type_of_device)
        f8.write("      ")
        f8.write(order)
        f8.write("   ")
        f8.write(days)
        f8.close()
        
print("||||||||||||||||||| Welcome to Computer and Mobile Service Centre|||||||||||||||||||")
c=0
while (c==0):
    user=input("Who's using the software?\n\n1.Customer\n\n2.Owner\n\nType the number:")
    if (user=='2'):
        print("------OWNER's PAGE------")
        a=Owner() 
    elif(user=='1'):
        print("------CUSTOMER's PAGE----------")
        b=Customer()
