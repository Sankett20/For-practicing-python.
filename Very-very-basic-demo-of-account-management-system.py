class AccountManagement:
    print("""
    Welcome to Account Management System
-------------------------------------------""")
    def __init__(self):
        self.users = {} 

    def register(self):
        print("""
            Register yourself
----------------------------------------------""")
        input_mobile_as_id=input("Enter your mobile number to create account = ")
        if len(input_mobile_as_id) ==10:
            input_name=input("Now Enter Name = ")
        else:
            print("Enter correct 10 digit number")
            return
        input_email=input("Now Enter email = ")
        if "@" not in input_email and "." not in input_mobile_as_id:
            print("Enter correct email id")
            return
        input_address=input("Now Enter address = ")
        input_mobile=input_mobile_as_id
        input_password=input("Enter password = ")
        
        self.users[input_mobile_as_id]={"Name":input_name,"Email":input_email,"Address":input_address,"Mobile number":input_mobile,"Password":input_password}
        print("Registration succesful")
    
    def login(self):
        print("""
                    Login
----------------------------------------------""")
        #print(self.users)
        check_mobile_no=input("Enter mobile number = ")
        if check_mobile_no in self.users.keys():
            check_password=input("Enter password = ")
            print()
            user_account=self.users[check_mobile_no]
            if check_mobile_no == user_account["Mobile number"] and check_password == user_account["Password"]:
                print("User found")
                print(f"Your Mobile number : {user_account["Mobile number"]}\nYour Email : {user_account["Email"]}\nYour Address : {user_account["Address"]}")
                print()
            else:
                print("invalid creditionals")
        else:
            print("Account with this number does not exist")

    def delete_account(self):
        print("""
                Delete account
----------------------------------------------""")
        check_mobile_no=input("Enter mobile number = ")
        if check_mobile_no in self.users.keys():
            check_password=input("Enter password = ")
            print()
            user_account=self.users[check_mobile_no]
            if check_mobile_no == user_account["Mobile number"] and check_password == user_account["Password"]:
                print("User found. Acount deleting..")
                del self.users[check_mobile_no]
                print("Account deleted")
                print()
            else:
                print("invalid creditionals")
        else:
            print("Account with this number does not exist")
      

    def exit(self):
        breakpoint

obj_ams=AccountManagement()
print("""
      1-Register
      2-Login
      3-Delete account
      0-Exit
""")
choice=int(input("Enter your choice = "))
while choice!=0:
    if choice==1:
        obj_ams.register()
        choice=int(input("Enter 0 to exit or Enter other option to do further steps = "))
        print()
    elif choice==2:
        obj_ams.login()
        choice=int(input("Enter 0 to exit or Enter other option to do further steps = "))
        print()
    elif choice==3:
        obj_ams.delete_account()
        choice=int(input("Enter 0 to exit or Enter other option to do further steps = "))
        print()
    elif choice==0:
        obj_ams.exit()
    else:
        choice=int(input("Please enter correct option = "))
        if choice == 0:
            break
print("""
          ----Thanks for using----
      ---------Sanket Thange----------""")
