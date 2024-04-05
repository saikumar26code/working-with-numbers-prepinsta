
def lcm(d1,d2):
    for i in range(max(d1,d2),(d1*d2)+1):
        if i%d1==0 and i%d2==0:
            return i
n1,d1=map(int,input().split())
n2,d2=map(int,input().split())
sumofnum=(n1*lcm(d1,d2))//d1+(n2*lcm(d1,d2))//d2
print(sumofnum,"-",lcm(d1,d2))