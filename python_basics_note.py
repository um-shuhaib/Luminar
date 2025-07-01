# age = int (input ("hey..Whats your age? :")) 
# if age >= 18:
#     print("you can vote")
# else:
#     print("you cant vote")
# print(type(age))
# dic={
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
# lst=[1, 2, 3, 4, 5]

# mutable and immutable - related to modification


#int(), float(), str(), bool(), tuple(), list(), set() - coversion methods


# a = 5
# b = 5
# c = a + b 
# print(c) 
# a = int(input("Enter First number: "))               
# b = int(input("Enter Second number: "))
# c = a + b 
# print("The Sum is : ",c) 

#operators
# arithmetic - // = floor division --- 10//3 = 3  ... no points
# % and // are opposite operators 


#identity operator - is , is not - comparing two objs

# #  ( check whether it is )

# a = 110
# b = 110
# print(a is b)





#membersjip operator - in, not in
# (is there )

# s= "hello"
# print("h" in s )                 #True or False
# print("h" not in s)

# greeting= "good morning"
# print("good" in greeting)     #sub sequent ayittanu check cheyyuka
# print("hey" in greeting)

# check whether the give number is odd or even

# input = int(input("Enter the number to check: "))
# if input % 2 == 0 :
#     print("the number ",input, " is even number")
# else:
#     print("The number ",input," is odd number")

# name = "shuhaib"
# age = 24
# print(f"My name is {name} and my age is {age}")      #printing formate 


#Largest amoung 2 numbersw

# num1 = int(input("Enter the number1 to check: "))
# num2 = int(input("Enter the number2 to check: "))
# if num1 < num2:
#     print(f"The number {num2} is Largest Number")
# else:
#     print(f"the number {num1} is Largest number")


#Largest amoung 3 numbers

# num1 = int(input("Enter the First number: "))
# num2 = int(input("Enter the Second number: "))
# num3 = int(input("Enter the Third number: "))
# if num1>num2 and num1 >num3:
#     print(f"{num1} is largest")
# elif num2>num3:
#     print(f"{num2} is largest")
# else:
#     print(f"{num3} is largest")

#divisible by 2 and 5

# num1 = int(input("Enter a number: "))
# if num1 % 2 == 0 and num1 % 5 ==0:
#     print(f"The number {num1} is divisible byy both")
# elif num1 % 2 != 0 and num1 % 5 != 0:
#     print(f"the number {num1} is not divisible by both")
# elif num1 % 2 != 0 and num1 % 5 == 0:
#     print(f"the number {num1} is not divisible by 2 but divisible by 5")
# else:
#     print(f"the number {num1} is not divisible by 5 but divisible by 2")


# num1 = int(input("Enter a number: "))
# if num1 % 2 == 0 and num1 % 5 ==0:
#     print(f"The number {num1} is divisible byy both")
# else:
#     if num1%2==0:
#         print(f"{num1} is div by 2 but not 5")
#     elif num1%5==0:
#         print(f"{num1} is div by 5 but not 2")
#     else:
#         print(f"{num1} is not div by both")

# num1 = int(input("Enter a number: "))
# if num1 % 2 == 0:
#     if num1 % 5 == 0:
#         print("The number div by both")
#     else:
#         print("The number div by 2 but not 5")
# else:
#     if num1 % 5 ==0:
#         print("The number div by 5 nut not 2")
#     else:
#         print("The number not div by both")

# print("* ",end=" ")
# print("* ",end=" ")
# print("* ",end=" ")
# print("* ",end=" ")


# for 

# for i in range(start,end,increment)

# for i in range(1,10): #by default incremented by 1
#     for j in range(1,i): #by default incremented by 1
#         print("*",end=" ")
#     print()
# o/p 

# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *

# for i in range(6):
#     for k in range(5):
#         print(k+1,end=" ")           
#     print()

#  o/p
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# for i in range(5):
#     for k in range(5):
#         print(i,end=" ")
#     print()

# o/p
# 0 0 0 0 0 
# 1 1 1 1 1 
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4

# number = int(input("Enter the number: "))
# for j in range(1,11):
#     result = j*number
#     print(f"{j} X {number} = {result}")


    # 1 * 10 = 10
    # 2 * 10 = 20

# for i in range(1,100):
#     if i % 2 == 0:
#         print(i)

# sum=0
# for i in range(101):
#     sum += i
# print(sum)    #5050

#factorial of a number
# n=int(input("Enter the number: ")) #5
# fact = 1
# for i in range(1,n+1):
#     fact *= i                        #fact = 1*2*3*4*5
# print(fact) 


                                        # for loop using because we knows the end/range


# n = int(input("Enter the number: "))
# count = 0
# while n>0:
#     n = n//10
#     count+=1
# print(count)

# o/p
# Enter the number: 156845
# 6

#reverse of a number also find pallindrome   for NUMBERS
# n = int(input("Enter the Number: "))
# rev = 0
# p = n
# while n>0:
#     rem = n%10
#     rev = rev*10+rem
#     n = n//10
# print("riverse is ",rev)
# if rev==p:
#     print("it is pallindrome")
# else:
#     print("not pallindrome")

# For BOTH NUMBER AND STRING

# string = input('enter the somthing: ')
# rev_sring = string[::-1]
# print(rev_sring)
# if string == rev_sring:
#     print("pallindrome")
# else:
#     print("not pallindrome")


# for row in range(6):
#     for col in range(0,row):
#         print("*",end=" ")
#     print()

# o/p

# * 
# * *
# * * *
# * * * *
# * * * * *

# for row in range(6):
#     for col in range(6,row,-1):
#         print("*",end=" ")
#     print()

# o/p 
# * * * * * * 
# * * * * * 
# * * * *
# * * *
# * *
# *

# n=10
# for raw in range(n):
#     for col in range(n-raw):    
#         print(" ",end=" ")
#     for sec_col in range(raw):
#         print("*",end=" ")
#     print()

    # o/p 
    
#           * 
#         * *
#       * * *
#     * * * *
#   * * * * *


# for raw in range(6):
#     if raw==0 or raw==5:
#         for col in range(6):
#             print("*",end=" ")

#     else:
#         print("*",end=" ")
#         for col in range(4):
#             print(" ",end=" ")
#         print("*",end=" ")
#     print()

#o/p
# * * * * * * 
# *         * 
# *         *
# *         *
# *         *
# * * * * * *

#or

# for raw in range(6):
#     for col in range(6):
#         if raw==0 or raw==5 or col==0 or col==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

    # o/p 
# * * * * * * 
# *         * 
# *         *
# *         *
# *         *
# * * * * * *

# for raw in range(5):
#     for col in range(5):
#         if col==0 or raw==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

    # o/p 
# *
# *
# *
# *
# * * * * *

# for raw in range(5):
#     for col in range(5):
#         # if (raw==0 and col!=0 and col!=4)or (raw==4 and col!=0 and col!=4)or (col==0 and raw!=0 and raw!=4)or (col==4 and raw!=0 and raw!=4):
#         if (raw==0 or raw==4) and (col!=0 and col!=4) or (col==0 or col==4)and (raw!=0 and raw!=4):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# o/p 

#   * * *   
# *       * 
# *       *
# *       *
#   * * *


# for raw in range(6):
#     for col in range(6):
#         if (raw==0 and col!=0 and col!=5 ) or (col==0 or col==5)and raw!=0 or (raw==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# #o/p

# #   * * * *   
# # *         * 
# # *         *
# # * * * * * *
# # *         *
# # *         *

# for raw in range(6):
#     for col in range(6):
#         if (raw==0 or raw==5) and col!=5 or (col==0 or col==5)and (raw!=0 and raw!=5):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# o/p

# * * * *  
# *       *
# *       *
# *       *
# *       * 
# * * * * 

# square of the list element

# number = [10,11,12,13,14,15]
# for i in number:
#     print(i**2)

    #o/p

# 100
# 121
# 144
# 169
# 196
# 225

# Total sum of the list

# number = [10,11,12,13,14,15]
# sum = 0
# for i in number:
#     sum += i
# print(sum)

#o/p
# 75

# Largest number in a list

# number = [10,11,12,13,14,15]
# large = 0
# for i in number:
#     for j in number:
#         if i<j:
#             large = j
# print(large)

# o/p
#15


# number = [10,11,12,13,14,15]
# large = 0
# for i in number:
#     if large < i:
#         large=i
# print(large)

# # o/p                     OR
# # 15

# number = [10,11,12,13,14,15]
# print(sum(number))                            # BUILD IN FUNCTION
# print(max(number))                            # BUILD IN FUNCTION
# print(min(number))                            # BUILD IN FUNCTION



                            # LOOP CONTROLLING STTATEMENT
                            # break, continue, pass                          pass for empty statement

# number = [10,11,12,13,14,15]
# for i in number:
#     if i % 5 ==0:
#         break
#     else:
#         print(i)

# # o/p
# # nothing

# number = [10,11,12,13,14,15]
# for i in number:
#     if i % 5 ==0:
#         continue
#     else:
#         print(i)

# # o/p
# # 11
# # 12
# # 13
# # 14
# number = [10,11,12,13,14,15]
# for i in number:
#     if i % 5 ==0:
#         pass                       # 5 STAR DO NOTHING
#     else:
#         print(i)

# # o/p
# # 11
# # 12
# 13
# 14


# number = 100
# while True:
#     guess = int(input("Enter the guess: "))
#     if number < guess:
#         print("The guess is Greater than the number. Please guess again: ")
#     elif number > guess:
#         print("The guess is smaller than the number. Please guess again: ")
#     else:
#         print("Congrats ! YOU ARE CURRECT ")
#         break

                                        # camelCase in js
                                        # Pascalcase in python for class
                                        # snake_case in python for variable and function


# o/p 

# Enter the guess: 52
# The guess is smaller than the number. Please guess again: 
# Enter the guess: 187
# The guess is Greater than the number. Please guess again: 
# Enter the guess: 100
# Congrats ! YOU ARE CURRECT 

# n=1
# for raw in range(6):
#     for col in range(raw):
#         print(n,end=" ")
#         n+=1
    
#     print()

    #   o/p 
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15  

# k = 0
# for raw in range(5):
#     for col in range(5-raw):
#         print(5-k,end=" ")
#         k+=1
#     k=0
#     print()

#     o/p 

# 5 4 3 2 1 
# 5 4 3 2 
# 5 4 3
# 5 4
# 5

# for i in range(5):
#     for j in range(5,i,-1):
#         print(j,end=" ")
#     print()

#     o/p 

# 5 4 3 2 1 
# 5 4 3 2 
# 5 4 3
# 5 4
# 5

                                                 #DATA TYPES


# 1 - MUTABLE and INMUTABLE

# list, set, dictionary  - mutable
# int, float, char ...   - inmutable

# string is itrable and indexing

                                             # slicing

                                          # print(s[start,end,step]) 


# s[::]  fuill
# s[::-1] reverse

# s = "Good Morning"
# print(s[::])
# print(s[::-1])              # string reverse

# # length

# # len(s)         # lenght of a string

# print(len(s))
# print(s[::2])    #skips one
# print(s[:])                                     

#                                  # string      -      slicing, inmutable, indexing


                       # string methods

# s = " Good morning "
                            # print(s.upper())                       # .upper()   to upper case
                            # print(s.lower())                       # .lower()   To lower case
                            # print(s.title())                       # .title() change every first letter to UPPER CASE
                            # print(s.capitalize())                  # .capitalize() change only first letter to CAPITAL LETTER

                                # print(s.isupper())          # .isupper()    check full letters are in UPPER CASE or NOT
                                # print(s.islower())          # .islower()    check full letters are in LOWER CASE
                                # print(len(s))               # .len()
                                # print(len(s.strip()))       # .strip()    For removing first and last blank spaces
                                # print(len(s.lstrip()))      # .lstrip()    for removing first blank spaces
                                # print(len(s.rstrip()))      # .rstrip()   For removing last blank Spaces


                                            # splittind


# s = " Good,morning "

# print(s.split())              # .split()       space vach split cheyyunnu
# print(s.split(","))           # .split(",")                 , vach split cheythu


                                               # replace

                                     #   .replace(from,to,count)


# s = " Good morning "

                # print(s.replace("Good","happy"))           # .replace("cheyyandathu,cheyyunnadhu")
                # print(s.replace("o","*",1))                # .replace("cheyyandathu,cheyyunnadhu", no. of occarance) #1st one only op=g*od 
                # print(s.replace("o","*",2))                # .replace("cheyyandathu,cheyyunnadhu",no. of occarance)  #1st two only op=g**d


                                    # .ljust()

# s = "Good morning"

# print(s.ljust(10,"*"))          #good left lu bakki fill cheyyunnadhu right side lu  #.ljust(etra count koottanam, ndhu vach fill cheyyanam)
# print(s.rjust(10,"*"))   
# print(s.center(10,"*"))   

# op

# Good******
# ******Good
# ***Good***

# s = "Good morning"
# h = "12345"
# b = 12354
# # print(s.startswith("G"))  # true                    .startwith()
# # print(s.startswith("m"))  # false                   .endwith()
# # print(s.endswith("m"))  # false
# # print(s.endswith("G"))  # false
# # print(s.endswith("g"))  # true


# print(s.isnumeric()) #false             .isnumeric(), .isalpha(), .isalnum()
# print(h.isnumeric()) # true
# # print(b.isnumeric())         # ERROR not a string
# print(s.isalpha())
# print(s.isalnum())
# print(s.isspace())


# s= "abc @123"
# alpha=0
# number=0
# special=0
# space=0
# for i in s:
#     if i.isnumeric():
#         number+=1
#     elif i.isalpha():
#         alpha+=1
#     elif i.isspace():
#         space+=1
#     else:
#         special+=1
# print("letters:",alpha," numbers: ",number," spaces: ",space," special: ",special)

# op

# letters: 3  numbers:  3  spaces:  1  special:  1

                                                      # Indexing

# .index()    returns the index position
# if not exist then we ll get an Error 


# s = "Good morning"

# print(s.index("r"))
 
                                                                    # .find()

# print(s.find("j"))                                                 # -1 if not exist

                                                                   # .rfind()    #start with right side

# print(s.rfind("o"))

# print(s.find("o"))


#                                                                # .count()      # to find the count

# print(s.count("o"))

#                                                               # delete -    # del s

# del s
# print(s)


# replace all first letter to * but not the first one

# s = "python programming"
# a = s[0]
# print(s[0]+s[1:].replace(a,"*"))

# op 
# python *rogramming


# if the s have >3 letters and no "ing" in the end then add "ing". if it has tthen add "ly". if not min 3 letters then print the same.

# s = input("Enter the string: ")
# if len(s)>=3:
#     if s.endswith("ing"):
#         print(s+"ly")
#     else:
#         print(s+"ing")
# else:
#     print(s)

# op

# Enter the string: ikng
# iknging

# Enter the string: man
# maning

# Enter the string: ing
# ingly

# Enter the string: in
# in




# item = input("Enter the item: ")
# price = float(input(" Enter the price: "))
# night = int(input("over night (if yea = 0 , if no = 1): "))

# if night == 0:
#     if price >= 10:
#         print(f"Invoice: \n{item} : {price}\nshipping : {8}\nTotal : {price + 8}")
#     else:
#         print(f"Invoice: \n{item} : {price}\nshipping : {7}\nTotal : {price + 7}")
# elif night == 1:
#     if price >= 10:
#         print(f"Invoice: \n{item} : {price}\nshipping : {3}\nTotal : {price + 3}")
#     else:
#         print(f"Invoice: \n{item} : {price}\nshipping : {2}\nTotal : {price + 2}")

#                                          #or
# item = input("Enter the item: ")
# price = float(input(" Enter the price: "))
# choice = int(input("over night (if yea = 0 , if no = 1): "))
# night = 0
# shipping = 2
# if price > 10:
#     shipping = 3
# if choice == 0:
#     night = 5
# print(f"invoice: \n{item} : {price}\nshipping : {shipping+night}\ntotal : {price+shipping+night}") 





                                                              # list

#s = ["hi","hello",12,True]
# s = [100,101,102,103,"python programmming"]

#print(s[0])
#print(s[1:3])

# slicing of list

#print(s[-1][0:6])   # s[select the element][slicing range]

                                                                    # we can modify list
                                                                    # duplicate items 
# s[0]=200
# print(s)

                                                 # list methods


# numbers = [10,20,30,40,50]

                                               # append() - single value to the end of the list
                                               #  extend() - multiple values iterate cheythit # "python" to "p","y","t" .. ,"n" {only iterable values}
                                                            # at the end 
                                               #  insert() - with position we can add one item data
                                                            # insert(pos,value)

# numbers.append(600)
# print(numbers)
# numbers.extend("hello")
# numbers.extend(["python"])

# op 
# [10, 20, 30, 40, 50, 600, 'h', 'e', 'l', 'l', 'o', 'python']
# numbers.insert(2,"second")
# print(numbers)

# op 
# [10, 20, 'second', 30, 40, 50, 600, 'h', 'e', 'l', 'l', 'o', 'python']

# l =[]
# l2 = list()    empty



# a list then seperate odd even numbers list 


# numbers = [10,11,12,13,14,15,16,17]
# odd = []
# even = []
# for i in numbers:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("odd: ",odd)
# print("even: ",even)

# op
# odd:  [11, 13, 15, 17]
# even:  [10, 12, 14, 16]

                                                               # pop()

# numbers = [10,11,12,13,14,15,16,17,"python"]

# # numbers.pop()         # last index
# # numbers.pop(0)         # last index
# # numbers.pop(-1)         # last index

# print(numbers)

#                                                                # remove()

# numbers.remove("python")
# print(numbers)

#                                                                # del
                
# del numbers[1]
# print(numbers)


# num = int(input("Enter the number: "))
# l = [10,20,30,40,50]
# if num in l:                                          # removing user inputed num from list
#     l.remove(num)
#     print(l)
# else:
#     print("not in the list")




# l = [10,20,30,10,30,40,50]
# result = []
# for i in l:
#     if i not in result:                                       # storing list without duplicate and printing
#         result.append(i)
# print(result)

# op
# [10, 20, 30, 40, 50]



# numbers = [1,2,3,4,5]
# result = []
# for i in numbers:
#     result.append((i,i**2))                # [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)] as tuple
# print(result)


                                                
                                                   # list comprehension

                                 # new_list = [expression for item in iterable if condition]

# result = []
# for i in range(1,8):
#     result.append(i)
# print(result)

# # or
                                                        # expresssion ahn append or return cheyyuka

# result = [i for i in range(1,11)]
# print(result)


# even = [i for i in range(1,11) if i%2==0]
# print(even)


# sqr = [i**2 for i in range(1,10) ]
# print(sqr)

# numbers = [1,2,3,4,5]
# result = [(i,i**2) for i in numbers]
# print(result)


                                          # new_list = [expression1 if condition1 else expression2 for item in iterable]
                                          # new_list = [expression1 if condition1 else expression2 if condition2 ... else expression_N for item in iterable]


# l = [1,2,3,4,5]
# result = ["even" if i%2==0 else "odd" for i in l]
# print(result)

# result = [(i,i**2) if i%2==0 else (i,i**3) for i in range(1,11)]
#print(result)

# l.reverse()
# l.sort()
# l.sort(reverse=true)

# in list we cant assign the list to another list. we need to use copy() method


# l1=l2        x
# l1=l2.copy   +

# l1 = [1,2,3]
# l2=l1.copy()
# l1[0]=100
# print(l1)
# print(l2)

l= [1,2,3,4,2,1,1]
print(l.count(1))
print(l.index(2))
print(sum(l))
print(min(l))
print(max(l))






