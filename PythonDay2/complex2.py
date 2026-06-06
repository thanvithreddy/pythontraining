#summation of each digit in the number


n=int(input("Enter the Digits that need to  be Sum up: "))
m=n
sum=0
rem=0
while(n!=0):
    rem=n%10
    sum=sum+rem
    n=n//10
    

print(f"Sum of the Digits of {m} is {sum}")