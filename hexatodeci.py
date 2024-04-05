n=input().upper()
l=len(n)-1
dic={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
i,res1,res2=0,0,0
for char in n:
    if char.isalpha():
        y=dic.get(char)
        res1+=y*16**l
        l-=1
    else:
        res2+=int(char)*16**l
        l-=1
print(res1+res2)