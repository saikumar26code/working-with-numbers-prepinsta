n=input()
num=int(n)
i=0
res=0
for i in range(len(n)):
    rem=num%10
    res+=(2**i)*rem
    i+=1
    num//=10
print(res)