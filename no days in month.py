month=int(input())
year=int(input())
arr=[31,28,31,30,31,30,31,31,30,31,30,31]
if month==2 and (year%400==0 or (year%100!=0 and year%4==0)):
    print("29")
else:
    print(arr[month-1])