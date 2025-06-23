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

input = int(input("Enter the number to check: "))
if input % 2 == 0 :
    print("the number ",input, " is even number")
else:
    print("The number ",input," is odd number")

name = "shuhaib"
age = 24
print(f"My name is {name} and my age is {age}")      #printing formate 