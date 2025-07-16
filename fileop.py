'''Python file operations'''

                                                                    # methods


# open() - open("path","mode") open and create new file
#   r - read - default
#   w - write
#   a - append - not clear existing data
# EOF - \n



# read()
# readlines() - returns all lines as list -
# readline() 
# write()
# writelines()
# rename()
# remove()
# close()
# tell() - read and returns the pointer position
# seek() - seek(pointer position) - change pointer position

# with

# python handling files as text file 


# f=open("file1.txt","r")
# print(f)
# print(f.read())
# f.close()


# with open("file1.txt") as f1:                              # here we dont need to close the file and if there is no file ERROR will see
#     print(f1.read())

# f = open("file1.txt","w")
# f.write("hi daa")
# f.close()

# with open("file1.txt","w") as f:
#     f.write("welcome python")

# f = open("file2.txt","w")
# f.write("second file created by open func")
# f.read()
# f.close()

# f = open("file2.txt","a")
# f.write("append -  a mode")
# f.close()


# f = open("file2.txt","r")
# print(f.readlines())                 # ['second file \n', 'created by open \n', 'funcappend -  a mode']
# f.close()

# f = open("file2.txt","r")
# print(f.read())
# print(f.readlines())
# f.close()
# op 
# second file 
# created by open
# funcappend -  a mode
# []

'''here first read() reads all texts then the pointer is in the last position then the readlines() is executed, so there is mo text after the cursor'''

# f = open("file2.txt","r")
# print(f.read(5))                    # secon
# f.close()

# f = open("file2.txt","r")
# print(f.readline(3))
# print(f.read(3))
# f.close()

# f = open("file2.txt","w")
# # f.write("hi\nwelcome back")
# f.writelines(["welcome\n","back"])
# f.close()

# f = open("file2.txt","r")       # count the number of lines
# list=f.readlines()
# print(len(list))

# count the number of letters in the fisrt line
# f = open("file2.txt","r")      
# list = f.readlines()
# print(len(list[0]))



# count the number of words in the fisrt line
# f = open("file2.txt","r")      
# content = f.readline()
# word = content.split()   # it wil split the content in to words
# print(len(word))   #25
# f.close()


# #total words in the file
# f = open("file2.txt","r")
# all_content = f.readlines()
# length = 0
# for i in all_content:
#     content = i.split()
#     length += len(content)
# print(length)
# f.close()

#or

# print(len(f.read().split()))

# starting with i word in the file

# f = open("file2.txt","r")
# words = f.read().split()
# count = 0
# for i in words:
#     if i.startswith("i"):
#         count +=1
#     elif i.startswith("I"):
#         count += 1
# print(count)
# f.close()

#i stating lines

# f = open("file2.txt","r")
# line_list = f.readlines()
# count = 0
# for i in line_list:
#     if i.startswith("i"):
#         count +=1
#     elif i.startswith("I"):
#         count += 1
# print(count)
# f.close()

f = open("file2.txt","r")
content = f.read()
print(f.tell())   # 1297
f.seek(5)                             # pointer moved to 5
print(f.tell()) # 5