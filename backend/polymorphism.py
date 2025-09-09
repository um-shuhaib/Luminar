
'''                                                            # Polymorphism - many forms '''

# same method in defferent form 
# python violating method overloading for doing that it uses #multipledispatch

# multiple dispatch have @dispatch(int,int) decorator

# we cant use direct @dispatch - we neet to install it using pip 
# pip install multipledispatch

# from multipledispatch import dispatch
# @dispatch(int.str) - neet to set datatypes of the argument

# from multipledispatch import dispatch
# class FindSum:
#     @dispatch(int,int)
#     def find_sum(self,a,b):
#         print(a+b)
#     @dispatch(int,int,int)
#     def find_sum(self,a,b,c):
#         print(a+b+c)
#     @dispatch(str,str)
#     def find_sum(self,a,b):
#         print(a+b)

# f1 = FindSum()
# f1.find_sum(1,2)
# f1.find_sum(1,2,3)
# f1.find_sum("hi ","hello")

# # op

# # 3
# # 6
# # hi hello
# 
'''                                                    # operator over loading '''


# __init__()
# __add__()
# __sub__()
# __gt__()
# __lt__()
# 
# 

# class A():
#     def __init__(self,num):
#         self.num = num

#     def __add__(self,other):
#         return self.num + other.num

#     def __sub__(self,other):
#         return self.num - other.num
#     def __gt__(self,other):
#         if self.num > other.num:
#             return (f"{self.num} is Greater")
#         else:
#             return (f"{other.num} is Greater")
#     def __lt__(self,other):
#         if self.num < other.num:
#             return "less than - True"
#         else:
#             return "Less than _False"
#     def __ge__(self,other):
#         if self.num >= other.num:
#             return "geater and qual - True"
#         else:
#             return "Greater and equal - False"
#     def __le__(self,other):
#         if self.num <= other.num:
#             return "lesss than and equal - True"
#         else:
#             return "less than and equal - False"

# c1 = A(10)
# c2 = A(20)
# print(c1+c2)
# print(c1-c2)
# print(c1<c2)
# print(c1<=c2)
# print(c1>c2)
# print(c1>=c2)


# op

# 30
# -10
# less than - True
# lesss than and equal - True
# 20 is Greater
# Greater and equal - False


'''                                                Encapsulation'''

# _ - protected
# __ - private

# ristrict modification 
# self.name is public variable
#     UNDERSCORE ( _ ) for protection. 
#                   self.salery is public
#                   self._salery is protected - not manditory , covention, jst warning but we can
#                   self.__salery is private - strictly protected - only in the class we can modify not directli
# name maangling - ( _classname__variable ) internally changing when we use a protected variable outside the class. we cant mod directly
#   adhond ahn purath namukk private class var access cheyyan pattathadhu

class Employee():
    def __init__(self):
        # self._salery = 30000
        self.__salery = 30000
        # self.salery = 30000
    def get_salery(self):                    # getters
        # print(f"salery {self.salery}")
        # print(f"salery {self._salery}")
        print(f"salery {self.__salery}")
    def set_salery(self,sal):                    # setters
        # self.salery = sal
        # self._salery = sal
        self.__salery = sal

emp1 = Employee()
emp1.get_salery()
emp1.set_salery(5000)
# print(emp1._salery)
print(emp1.__salery)
# emp1._salery = 80000
emp1.__salery = 80000
emp1.get_salery()
# print(emp1.salery)