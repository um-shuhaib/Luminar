# import re 
# num = input("enter the number: ")
# pattern = "^(\+91[\s|-]?)?([6-9][0-9]{9})$"
# if re.search(pattern,num):
#     print("valid")
# else:
#     print("invalid")




n = [1,2,5,6,6]
print(n)

big = max(n)
for i in n:
    if i == big:
        n.remove(i)
        print(n)
print(max(n))


