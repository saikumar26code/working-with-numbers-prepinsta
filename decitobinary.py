n=int(input())
arr=[]
while n!=0:
    arr.append(n%2)
    n//=2
for i in arr:
    print(i)