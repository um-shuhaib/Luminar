import re 
password = "123@kkj"
patters = "\d"
patter = "*"
print(re.search(patters,password))
print(re.findall(patters,password))
print(re.split("@",password))
# print(re.findall(patter,password))