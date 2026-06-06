month=int(input("Enter the Month: "))

if(month==1 or month==3 or month==5 or month==7 or month ==8 or month==10 or month==12):
    print("31 Days")

elif(month==4 or month==6 or month==9 or month==11):
    print("30 Days")

elif(month==2):
    print("28 Days/29 days")

else:
    print("Invalid Month")

