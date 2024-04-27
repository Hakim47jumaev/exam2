list=input().split()
a=max(list)
b=min(list)
j=0
for i in range(0,len(list)):
    if list[i]==a:
        k=i
    if list[i]==b:
        t=i
j=a
list[k]=b
list[t]=a
print(list)