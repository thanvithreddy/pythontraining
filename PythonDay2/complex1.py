#write a python program to read as input from user and fined the count of digits without using builtin functions
# import math
# n=int(input("Enter the Number: "))
# m=math.log10(n)
# print("The Number of digits in the Number: ",math.ceil(math.log10(n)))


n=int(input("Enter the Number: "))
count=0
res=0
while(n>0):
    res=n%10
    count+=1
    n=n//10

print("The total digits in the number: ",count)
