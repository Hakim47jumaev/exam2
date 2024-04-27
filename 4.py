list=input().split()
for i in range(0,len(list)):
    for j in range(0,1):
        list[i]=list[i][j]*list[i][j+1]
    
print(list)
