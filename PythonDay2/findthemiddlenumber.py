a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
c=int(input("Enter the Third Number: "))

if((a<b)and(a<c)and(b<c)):
    print(b," is the Middle Number")
elif((b<a)and(b<c)and(a<c)):
    print(a," is the Middle Number")
else:
    print(c," is the Middle Number")