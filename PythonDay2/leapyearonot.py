year=int(input("Enter the Year that need to be Checked: "))



if(year%4==0 and year%100!=0) or (year%400==0):
        print(year, " is a Leap Year")
else:
        print(year, " is Not a leap year")

