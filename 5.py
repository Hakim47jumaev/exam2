def polindrom(n, f=-1):
    for i in range(len(a)//2):
        if a[i] != a[f]:
            return False
        f-=1
        i+=1
    return True
while True:
    a = input()
    print(polindrom(a))