List1=list(map(int,input("Enter the numbers in List : ").split))
#List2=list(map(int,input().split()))

if len(List1) > 0:
    average = sum(List1) / len(List1)
    print("Average NPS Score:", average)
else:
    print("Average NPS Score: 0")
