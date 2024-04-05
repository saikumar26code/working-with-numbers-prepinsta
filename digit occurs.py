n=int(input())
r=int(input())
d=0
while n!=0:
    rem=n%10
    if rem==r:
        d+=1
    n//=10
print(d)
