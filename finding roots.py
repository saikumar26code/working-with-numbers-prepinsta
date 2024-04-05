from math import*
def roots(a,b,c):
    if a==0:
        print("Invalid")
        return -1
    d=b*b - 4*a*c
    sq=sqrt(abs(d))
    if d>0:
        print("roots are real and diffrent")
        print((-b + sq)/2*a)
        print((-b - sq)/2*a)
    elif d==0:
        print("roots are real and same")
        print(-b/2*a)
    else:
        print("roots are complex")
        print(-b/(2*a),"+i",sq)
        print(-b/(2*a),"-i",sq)
a=1
b=8
c=1
roots(a,b,c)