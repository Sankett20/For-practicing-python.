class Library:
    def book(self):
        self.books={"B1" : 5,
               "B2" : 10,
               "B3": 12,
               "B4" : 3}
        print()
        print("""
                    Book Library
              Specific codes for books
              B1 = Harry Poter
              B2 = Think and Grow Rich
              B3 = Rich Dad Poor Dad
              B4 = The Secret
              """)
        print("These books with specific quantities are available now")
        print("Book code : Quantity")
        for i in self.books:
            print(f"{i} : {self.books[i]}")
        print()
        
    def buy(self):
        b_n=input("Enter correct book code to buy book or enter 0 for exit = ")
        if b_n == "B1" or b_n == "B2" or b_n == "B3" or b_n == "B4":
            if self.books[b_n]>0:
                print("Book available, Order confirming")
                self.books[b_n]-=1
                print("Done, book will be sent to you shortly")
                print()
                print("Now current availabel books and quantity :")
                #print(self.books.items())
                print("Book code : Quantity")
                for i in self.books:
                    print(f"{i} : {self.books[i]}")
                print()
            else:
                print("Book is not availble currently")
        elif b_n == "0":
            breakpoint
        else:
            print("Please enter correct book code")
    breakpoint

    def Return(self):
        b_n=input("Enter correct book code to Return book or enter 0 for exit = ")
        if b_n == "B1" or b_n == "B2" or b_n == "B3" or b_n == "B4":
            if self.books[b_n]>=0:
                print("Adding Book to library")
                self.books[b_n]+=1
                print("Book is now added to library")
                print()
                print("Now current availabel books and quantity :")
                for i in self.books:
                    print(f"{i} : {self.books[i]}")
                print()
        elif b_n == "0":
            breakpoint
        else:
            print("Enter correct code")
         
    def exit(self):
        breakpoint

obj_book=Library()
obj_book.book()

option=input("\n1. Buy Book\n2. Return Book\n0. Exit\nEnter your option to do further steps = ")
while option!="0":
    if option=="1":
        obj_book.buy()
        option=input("Enter 0 to exit or Enter other option to do further steps = ")
    elif option=="2":
        obj_book.Return()
        option=input("Enter 0 to exit or Enter other option to do further steps = ")
    elif option=="0":
        obj_book.exit()
    else:
        option=input("Please enter correct option = ")
        if option == "0":
            break
print("""Thanks for using book library management
      - Sanket Thange""")
        
