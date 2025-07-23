'''                              OOPS '''
# related fun and op wrapped together and structure - remove unwanted operations
# object, class, methods
# methods - function 
# class - blueprint of obj- design pattern - template of obj
# obj - instance of classes

# behaviour - fun\method
# attributes - variable,color

# class Mobile:
#     def calling(self):         # self - refering the current obj
#         print("calling...")


# # or
# Mobile1=Mobile()   # obj created  ''' when using obj an ref numbewr is sent as argument '''
# Mobile1.calling() # there will be an error or for fix set an parameter in the class


                                                     # Class and Object

# class Class(): # PascalCase
#     # initialising variables
#     def set_student(self,name, age, place, email): # snake_case
#         self.name = name # stud1.name = "abc"  # stud2.name = "xyz"
#         self.age = age
#         self.place = place
#         self.email = email 

    
    
#     def student_info(self):
#         print(f"Name: {self.name}\nAge: {self.age}\nPlace: {self.place}\nE-Mail: {self.email}")

# stud1=Class()
# stud1.set_student("abc",24,"Kozhikode","spm@gmail.com")
# stud1.student_info()

# print()

# stud2=Class()
# stud2.set_student("xyz",25,"Malappuram","shuh@gmail.com")
# stud2.student_info()

                                              # constructores - special method to initialize variables

# __init__ - special method - created when obj created


# class Class(): # PascalCase
#     # initialising variables
#     def __init__ (self,name, age, place, email): # constructor
#         self.name = name # stud1.name = "abc"  # stud2.name = "xyz"
#         self.age = age
#         self.place = place
#         self.email = email
#     def student_info(self):
#         print(f"Name: {self.name}\nAge: {self.age}\nPlace: {self.place}\nE-Mail: {self.email}")

# stud1 = Class("Peru",28,"cpt","em@gmail.com") # constructor initialised 
# stud1.student_info()




# qn-1


# class Bank():
#     bank_name = "AU Bank"      # class variable - common data
#     def __init__(self,name,acc_no):
#         self.name = name
#         self.acc_no = acc_no                # instance variable - oro obj kkum defferent data
#         self.balance = 1000
    
#     def account(self):
#         print(f"Greatings from {self.bank_name}\nDear {self.name}, Your account number {self.acc_no} have balance {self.balance}.\nThank You")
#         print()
#     def deposite(self,amount):
#         self.balance += amount
#         print(f"Greatings from {self.bank_name}\nDear {self.name}, Your account {self.acc_no} is Credited INR ₹{amount} and Current Balance is {self.balance}.\nThank You")
#         print()    
#     def withdraw(self,amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f"Greatings from {self.bank_name}\nDear {self.name} Your account is Debited amount INR {amount} and Current Balance is {self.balance}.\nThank You")
#             print()
#         else:
#             print(f"Greatings from {self.bank_name}\nDear {self.name}. You have insufficient Balance")
#             print()

# cust1 = Bank("manu",1025659854)
# cust1.account()
# cust1.deposite(1000)
# cust1.withdraw(3000)

# print(cust1.balance)   # can access instance var outside the class using obj

# print(cust1.bank_name)  # can access class variable outside the class using obj
# print(Bank.bank_name)  # we can also call the class variable using class name

# cust2 = Bank("Manju",1165454635)
# cust2.bank_name = "SBI"

# print(Bank.bank_name)
# print(cust1.bank_name)
# print(cust2.bank_name)




# qn - 2


# Ekart - add_product(name,quantity)
# cart =[(),()]
# remove from cart
# total quantity


class Ekart():
    def __init__(self,name,quantity):
        self.cart=[]
        self.cart.append((name,quantity))
    def add_product(self):
        print(f"Your Cart!\nItem Name: {self.cart[0][0]}\nQuantity: {self.cart[0][1]}")
    def remove_from(self,name):
        if self.cart[0][0] != name:
            print(f"{name} is not in the list")
        else: 
            
            self.cart[0] = (self.cart[0][0],self.cart[0][1]-1)
            
            print(self.cart)
    def count(self):
        print(f"Total count: {self.cart[0][1]}")



pro1 = Ekart("onion",12)
pro1.add_product()
pro1.remove_from("onion")
pro1.count()

        