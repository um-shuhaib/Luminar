l = [["hell",30],["hi",25],["beta",50],["alpha",50]]
# srt = []
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[j][1] > l[j+1][1]:
#             l[j][1],l[j+1][1]
l.sort(key=lambda x:x[1])
print(l)