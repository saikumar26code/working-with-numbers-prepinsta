
def fact(n):
    f=1
    while n>0:
        f*=n
        n=n-1
    return f
seats=int(input())
chairs=int(input())
print(fact(seats)//fact(seats-chairs))


