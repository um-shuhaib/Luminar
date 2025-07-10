# dynamically typed language

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





#membership operator - in, not in
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
                            # break, continue, pass                          #pass for empty statement

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


                                            # splitting


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

# l= [1,2,3,4,2,1,1]
# print(l.count(1))
# print(l.index(2))
# print(sum(l))
# print(min(l))
# print(max(l))

#swapping

# a=10
# b=20
# print(a,b)                                        a=a+b
# t=a                                               b=a-b    swapping wihout 3rd variable
# a=b                                               a=a-b
# b=t 
# print(a,b)


# a = 0
# b = 1
# results = [0,1]
# for i in range(2,11):
#     next = a + b
#     results.append(next)
#     a=b 
#     b=next
# print(results)

                                                                 # Fibanoocci series

# a=0
# b=1
# result = []
# num = int(input("Enter the number: "))
# if num <=0:
#     print("enter a positive number")
# elif num==1:
#     result.append(a)
# else:
#     t = [0,1]
#     result.extend(t)
#     for i in range(2,num):
#         next = a + b
#         result.append(next)
#         a,b=b,next
# print(result)

# or

# a = 0
# b = 1
# for i in range(10):
#     print(a)
#     next = a + b
#     a=b
#     b = next 


# a = 0
# b = 1
# result =[]
# for i in range(10):
#     result.append(a)
#     next = a + b
#     a=b
#     b = next 
# print(result)




                                                                       # prime number

# num = int(input("Enter the number: "))

# prime = 0
# for i in range(2,num):
#     if num%i==0:
#         prime = 1
#         break
# if prime == 0:
#     print("prime")
# else:
#     print("not prime")

                                                                          # range of prime numbers

# n = int(input("enter the range: "))

# for i in range(3,n):
#     flag = True
#     for j in range(2,i):     # flag should be i the scop
#         if i%j==0:
         
#             flag = False
#             break 
#     if flag:
#        print(i)


                                                                            # amstrong number

# num = int(input("enter the number: "))
# num1 =num
# l=len(str(num))
# res = 0
# while num>0:  
#     rem = num % 10 
#     res += rem**l 
#     num //= 10 
# if res == num1:
#     print(f"{num1} is amstromg")
# else:
#     print(f"{num1} not amstrong")



                                                               #dictionary


# dict={"key":"value"}
# dict={}
# key - immutable only , no duplicate
# valus - anything
# dict1=dict()

# no duplicate keys - if added then NO ERROR will shows - it will automatically assign the latest value 


                                                        #  only immutable as key in dict = no list as key in dict

# student = {"name":"shuhaib","age":24,"place":"vazhakkad"}

# print(student["name"])
# print(student["place"])
# student["place"]="choorappata"
# print(student["place"])
# student["email"]="shuaib@gmail.com"            # email is not in the dict so it will add it to the dict
# print(student)


                                                       # dictioanary methods
        
                                                                                    # get()
                                                                                    # values() - values as list
                                                                                    # keys() - keys as list
                                                                                    # items() - seperate data as tuple - 

# student1 = {"name":"manu","place":"cpt"}

# print(student1.get("name"))
# print(student1.values())
# print(student1.keys())
# print(student1.items())

# op 
# dict_values(['manu', 'cpt'])
# dict_keys(['name', 'place'])
# dict_items([('name', 'manu'), ('place', 'cpt')])


                                                                              # update() - to add new item or update existing item.
                                                                              # dict["key"] = value - same as update()
                                                                              # pop("key") - remove and return last item 


# student1 = {"name":"manu","place":"cpt"}

# student1["email"]="shuhaib@gmail.com"
# student1.update({"phone":1234564586})
# student1.update({"place":"oorkkadavu"})
# print(student1)
# l = [1,2,3]
# print(l)
# ret = l.pop()
# print(ret) 
# print(l)


                                                                            # pop("key") - argument must be pass
                                                                            # popitem() - no argument needed, last item will delete
                                                                            # clear() - empty the dictionary
                                                                            # del disctioanary_name - delete complete dict and list
                                                                            # del dict_name["key"]

# student1 = {"name":"manu","place":"cpt"}
# print(student1)
# # student1.pop("place")
# # student1.popitem()
# # student1.clear() #{'name': 'manu', 'place': 'cpt'}   #{}
# del student1["place"]
# print(student1)
# del student1
# print(student1)



# dict = {}
# print(dict)
# for i in range(5):
#     key = int(input("Enter the key: "))
#     value = input("Enter the value: ")
#     dict[key]=value                     #or dict.update({key:value})
# print(dict)


# keys = [1,2,3,4,5]
# values = ["one","two","three","four","five"]
# dict = {}
# for i in range (len(keys)):
#         dict.update({keys[i]:values[i]})
# print(dict)

# op
# {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

# list = [10,20,30,10,30,40,20,30]
# dict ={}
# for i in list:
#     count=0
#     for j in range(len(list)):
#         if i==list[j]:
#             count+=1
#     dict.update({i:count})
# print(dict)

# op 
# {10: 2, 20: 2, 30: 3, 40: 1}                        # OR


# list = [10,20,30,10,30,40,20,30]
# dict ={}
# for i in list:
#     dict.update({i:list.count(i)})
# print(dict)

# op 
# {10: 2, 20: 2, 30: 3, 40: 1}


# list = [10,20,30,10,30,40,20,30]
# dict ={}
# for i in list:
#     if i not in dict:
#         dict.update({i:1})
#     else:
#         dict[i] +=1
# print(dict)

# # op 
# # {10: 2, 20: 2, 30: 3, 40: 1}







# dict = {"name":"mani","place":"kkd"}
# for i in dict:
#     print(i)
#     print(dict[i])




# d1 = {1:"one",2:"two"}
# d2=d1.copy()
# d2.update({1:"ten"})
# print(d1)
# print(d2) 

# op 
# {1: 'one', 2: 'two'}
# {1: 'ten', 2: 'two'}

# d1 = {1:"one",2:"two"}
# d2=d1
# d2.update({1:"ten"})
# print(d1)
# print(d2) 

# op 
# {1: 'ten', 2: 'two'}
# {1: 'ten', 2: 'two'}


                                                                     # SET

# mutable - unordered - indexing is not possible - no duplicate values
# no mutable data type as elements in set {no list, dict and set} - only inmutable elements
# set1 = set()   - empty set
# set2 = {1,2,3}

# l = {1,2,1}
# s = set(l)                 # we can remove duplicate value of list using SET.
# print(list(s))

# op 
# [1, 2]


# set = {10,"python",20,10,"python"}
# print(set)

# op 
# {10, 20, 'python'}

                                                                       #set Methods

                                # .add() - only inmutable arguments
                                # .update() - iterable values only
                                # .remove() - set.remove(10) - if not exist there will be an error
                                # discard() - set.discard(10) - no error if not exist
                                # .pop() - no argument - removes random element and returns
                                # del name - delete set
                                # .clear() - remove all elements
                                #  
                                # .union()  - set1.union(set2)
                                # .intersection() - 
                                # .difference() - 
                                # .symmetric_difference() - 



# set = {10,20,30,40}
# set.add(100)
# print(set)
# set.add("python")
# print(set)

# op 
# {100, 40, 10, 20, 30}
# {100, 40, 10, 20, 'python', 30}

# set = {10,20,30}
# set.update([1,2,3])
# print(set)
# set.update("django")
# print(set)
# set.update(("s","b"))
# print(set)

# op 
# {1, 2, 3, 10, 20, 30}
# {1, 2, 3, 10, 'g', 'j', 'n', 20, 'd', 'o', 'a', 30}
# {'s', 1, 2, 3, 'b', 10, 'g', 'j', 'n', 20, 'd', 'o', 'a', 30}


# set = {10,20,30}
# print(set)
# set.remove(10)
# print(set)

# op 
# {10, 20, 30}
# {20, 30}

# set = {10,20,30}
# set.discard(10)
# print(set)
# set.discard(100)
# print(set)

# op 
# {20, 30}
# {20, 30}

# set = {10,20,30}
# print(set)
# ret = set.pop()
# print(ret)
# print(set)
# set.clear()
# print(set)
# del set 
# print(set)

# op 
# {10, 20, 30}
# 10
# {20, 30}
# set()
# <class 'set'>

# set1 = {3,4,5,6}
# set2 = {1,2,3,4}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set2.symmetric_difference(set1))
#  op 
# {1, 2, 3, 4, 5, 6}
# {3, 4}
# {5, 6}
# {1, 2}
# {1, 2, 5, 6}

                                                                     # tuple

# NO MODIFICATION - () is not manditory - but , is manditory
# immutable - iterable - indexed - slicing - duplicates - any data types

# t1 =(1,2,3,4,5) # tuple
# t2 = 1,2,3,4,5 #also tiple   
# t3 = () #empty
# t4 = tuple() # empty

# t5 = (10) # integer
# t6 = (10,) # tuple
# t7 = 10, # tuple        # for tuple COMMA is important
# print(type(t5))
# print(type(t6))

# op 
# <class 'int'>
# <class 'tuple'>

                                                       # Tuple methods

                            # .index() - find index
                            # .count()
                            #
# t = (10,20,30,10)
# print(t.index(20)) # 1
# print(t.count(10)) # 2


                                                          # Tuple - packing and unpacking

# number = (10,20,30,40) # 4 elements so
# print(number) 
# a,b,c,d = number # each element is assigned to seperate variable 
# print(a)
# print(b)
# print(c)
# print(d)

# op 
# (10, 20, 30, 40)
# 10
# 20
# 30
# 40


# if lots of elements


# t = (1,2,3,4,5,6,7,8,9,5)
# a,b,c, *d = t
# print(a)
# print(b)
# print(c)
# print(d)

# op 
# 1
# 2
# 3
# [4, 5, 6, 7, 8, 9, 5]

# a,b, *c,d = t
# print(a)
# print(b)
# print(c)
# print(d)

# op 
# 1
# 2
# [3, 4, 5, 6, 7, 8, 9]
# 5

# *a,b,c,d = t
# print(a)
# print(b)
# print(c)
# print(d)

# op 
# [1, 2, 3, 4, 5, 6, 7]
# 8
# 9
# 5

                                                           # string - comtinues..

# name = "manu"
# age = 24
# print(f"my name is {name} and age is {age}") # my name is manu and age is 24   
# print("my name is {} and age is {}".format(age,name)) # my name is 24 and age is manu         #default formatting
# print("my name is {} and age is {}".format(name,age)) # my name is manu and age is 24         #default formatting  
# print("my name is {1} and age is {0}".format(age,name)) # my name is manu and age is 24       # positional formatting
# print("my name is {y} and age is {x}".format(x=age,y=name)) # my name is manu and age is 24   #keyword formatting

                                                     
                                                             # path in string
# path = "c:\newpython\task1"
# print(path)
# path = r"c:\newpython\task1"     # using "r" for raw string like "f" in printing
# print(path)

# op                             |
# c:                             |  #1st print
# ewpython        ask1           |
# c:\newpython\task1                # 2nd print



#functions

# buildin
# user defines
# lamda functions
# recursive functions

# def fun_name(parameters):
#     block of statement

# fun_name(arguments)

# sum()

# def su_m(a,b):
#     '''returns the sum of 2 numbers'''
#     s = a + b
#     print(s)
# su_m(100,200)
# print(su_m.__doc__)                            # returm the string comment in that fun
# print(print.__doc__)         # what is doc string - oru fun ndhann document cheythh veykkan

# same name two fun...last one will use 
# def su_m(a,b,c=0):  # default parameter value
#     s=a+b+c
#     print(s) 
# su_m(10,20)
# su_m(10,20,10)
# op 
# 30
# 40

# def user_det(name,age):        
#     print(f"my name is {name} and age is {age}")

# user_det(age=24,name="shu")              # keyword argument



# def info(*args):  # recieve args as tuple - arbitrary arguments (*args)
#     print(sum(args))

# info(1,2)
# info(3,1,2)
# info(1,5,8,2)

# def info(**kwargs):  #recive as dict - srbitrary keyword argumnts
#     print(kwargs)
#     print(f"name: {kwargs["name"]} and age: {kwargs["age"]}")

# info(age=25,place="kkd",name="spj")

# package - group of modules
# module - python file - we can use a module in another module (a file in another file)
# import fun

# import functions

# functions.find_sum(1,2,3) # 6

# import functions

# sum = functions.find_sum(1,2,3)
# print(sum)


# creating a folder to a package create "__init__.py" file

from packages import module1

module1.find_sum(1,2,3)











