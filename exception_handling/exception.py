'''                                                                           Exception Handling'''


# try: if try except is must
# except:
# else: exception illengil work aakm
# finally:
# raise : need on;y one line - raise ZeroDivisionError
#


# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# try:
#     print(n1/n2)
# except:
#     print("an error occured")
# print(n1*n2)

# op 
# Enter the first number: 10
# Enter the second number: 0
# an error occured
# 0



# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# try:
#     n1/n2
# except: # generic except block
#     print("an error occured")
# else:
#     print(n1/n2)
# finally:
#     print("finally block")
# print(n1*n2)

# op1
# Enter the first number: 10
# Enter the second number: 2
# 5.0
# finally block
# 20

# # op2
# Enter the first number: 10
# Enter the second number: 0
# an error occured
# finally block
# 0





# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# try:
#     # n1/n2                                         # n,0 - zerodivisionexcepion
#     # print(n) nameerror
#     print(n1.upper())                               # AttributeError
# except ZeroDivisionError:                           # seperate except block
#     print("an zero error occured")
# except NameError: 
#     print("an name error occured")
# except: # generic ecept block
#     print("generic block")



'''                                                              user defined exception classes'''

# create a class name the exception name 

# class ValueLargeError(Exception):  # need to use Exception classs for creatig the exception int the brackets - class ExceptionName(exception):
#     pass
# class ValueSmallError(Exception):
#     pass 

# x = 10

# while True:
#     n = int(input("Enter the number: "))
#     try:
#         if n<x:
#             raise ValueSmallError
#         elif n>x:
#             raise ValueLargeError
#         else:
#             print("Correct! ")
#             break
#     except ValueSmallError:
#         print("Value small")
#     except ValueLargeError:
#         print("Value Large")
#     finally:
#         print("Good PLay")
