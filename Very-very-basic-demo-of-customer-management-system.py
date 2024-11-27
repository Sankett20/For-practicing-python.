class CMS:
    print("--------Customer Management System--------")
    def cms(self):
        print()
        self.customer_details={"C1":{"Name":"Sanket Thange","Age":24,"Place":"Chakan"},
                               "C2":{"Name":"Mayur Kale","Age":25,"Place":"Pune"}}
        #print(self.customer_details)
        print("-----Current Present Customers-----")
        for code,details in self.customer_details.items():
            print(f"Customer Code : {code}")
            for details,subdetails in details.items():
                print(f"{details}:{subdetails}")
            print()

    def check_customer_details(self):
        for code,details in self.customer_details.items():
            print(f"Customer Code : {code}")
            for details,subdetails in details.items():
                print(f"{details}:{subdetails}")
            print()
    
    def add_customer(self):
        input_cus_code=input("Enter next customer code = ")
        input_name=input("Now Enter Name = ")
        input_age=input("Now Enter age = ")
        input_place=input("Now Enter Place = ")
        self.customer_details[input_cus_code]={"Name":input_name,"Age":input_age,"Place":input_place}
        print("Customer added press 1 to check customer details again")
        
    def update_customer(self):
        print("Enter customer code to change it's details")
        input_cus_code=input("Enter customer code = ")
        if input_cus_code in self.customer_details:
                print("\n1. Change name\n2. Change age\n3. Change place\nEnter correct option to change details")
                print()
                option=int(input("Enter your option = "))
                if option == 1:
                    input_name=input("Now Enter new Name = ")
                    self.customer_details[input_cus_code]["Name"]=input_name
                    print("Name is changed now. You can check them by pressing 1")
                    print()
                elif option == 2:
                    input_age=input("Now Enter new Age = ")
                    self.customer_details[input_cus_code]["Age"]=input_age
                    print("Age is changed now. You can check them by pressing 1")
                    print()
                elif option == 3:
                    input_place=input("Now Enter new Place = ")
                    self.customer_details[input_cus_code]["Place"]=input_place
                    print("Place is changed now.  You can check them by pressing 1")
                    print()
        else:
            print("customer code not found")

    def delete_customer(self):
        print("Enter customer code to delete it")
        input_cus_code=input("Enter customer code = ")
        if input_cus_code in self.customer_details:
                del self.customer_details[input_cus_code]
                print("Customer deleted")
                print()
        else:
            print("customer code not found")
        
        print("Customer details updated")

    def exit(self):
        breakpoint

obj_cms=CMS()
obj_cms.cms()
print("""
      1. Check customer details
      2. Add customer
      3. Update customer
      4. Delete customer
      0. Exit
""")
choice=int(input("Enter your choice = "))
while choice!=0:
    if choice==1:
        obj_cms.check_customer_details()
        choice=int(input("Enter 0 to exit or Enter other option to do further steps = "))
        print()
    elif choice==2:
        obj_cms.add_customer()
        choice=int(input("Enter 0 to exit or Enter other option to do further steps = "))
        print()
    elif choice==3:
        obj_cms.update_customer()
        choice=int(input("Enter 0 to exit or Enter other option to do further steps = "))
        print()
    elif choice==4:
        obj_cms.delete_customer()
        choice=int(input("Enter 0 to exit or Enter other option to do further steps = "))
        print()
    elif choice==0:
        obj_cms.exit()
    else:
        choice=int(input("Please enter correct option = "))
        if choice == 0:
            break
print("""
      ------------Thanks--------------
      ---------Sanket Thange----------""")
