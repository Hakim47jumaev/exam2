list=[(2, 7), (2, 6), (1, 8), (4, 9)]
for i in range(0,len(list)):
    list[i]=list[i][0]*list[i][1]
a=max(list)
b=min(list)
print(b,a)