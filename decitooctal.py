n=int(input())
arr=[]
while n!=0:
    arr.append(n%8)
    n//=8
for j in reversed(arr):
    print(j)