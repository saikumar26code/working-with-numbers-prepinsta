x,y=map(int,input().split())
if x>0 and y>0:
    print("1st")
elif x<0 and y>0:
    print("2nd")
elif x<0 and y<0:
    print("3rd")
elif x>0 and y<0:
    print("4th")
elif x==0 and y>0 or y<0:
    print("y")
elif x>0 or x<0 and y==0:
    print("x")

