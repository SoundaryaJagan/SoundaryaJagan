n=int(input())
a=[]
for x in range(0,n):
    b=input()
    a.append(b)
for i in range(0,n):
    for j in range(i+1,n):
        if(a[i]<a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t
for i in range(0,n):
print(a[i],end='')
