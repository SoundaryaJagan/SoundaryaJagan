def decode(x,n):
    perm=[0]*(n+1)
    perm[0]=1
    perm[1]=1
    print(x)
    for i in range(2,n+1):
        perm[i]=0
        if x[i-1]>0:
            perm[i]=perm[i-1]
        if x[i-2]==1 or (x[i-2]==2 and x[i-1]<7):
            perm[i]+=perm[i-2]
    print(perm)
    return perm[n]
x=input()
str=[]
for i in x:
    str.append(int(i))
n=len(x)
print(decode(str,n))
