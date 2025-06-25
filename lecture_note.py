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

# a = 5
# b = 5
# c = a + b 
# print(c) 
# a = int(input("Enter First number: "))              #int(), float(), str(), bool(), tuple(), list(), set() - coversion methods
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


''' for loop using because we knows the end/range '''


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

string = input('enter the somthing: ')
rev_sring = string[::-1]
print(rev_sring)
if string == rev_sring:
    print("pallindrome")
else:
    print("not pallindrome")


