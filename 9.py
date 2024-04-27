list=input().split()
n=len(list)
k=list[n-1]
for i in range(1,n):
    h=list[i]
    list[i]=list[i-1]
    list[i-1]=h

print(list)