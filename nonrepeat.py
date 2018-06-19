n=int(input())
arr=[int(x) for x in input().split()]
k=0
for i in arr:
k=0
for j in arr:
if i==j:
k+=1
if k==1:
print(i)
