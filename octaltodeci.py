n=input()
num=int(n)
res,i=0,0
while num!=0:
    rem=num%10
    res+=8**i*rem
    i+=1
    num//=10
print(res)