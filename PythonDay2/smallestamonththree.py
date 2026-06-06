a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
c=int(input("Enter the Third Number: "))

if((a<b)and(a<c)):
    print(a," is Smallest Among Three Numbers")
elif((b<a)and(b<c)):
    print(b," is Smallest Among Three Numbers")
else:
    print(c," is Smallest Among Three Numbers")