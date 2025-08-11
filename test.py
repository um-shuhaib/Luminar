l = [["beta",50],["chi",20],["alpha",50]]
print(l)
l.sort(key = lambda x:x[1])
l.sort()
sl = l[1]
for i in l:
    if i[1] == sl[1]:
        print(i[0])