age=int(input("Enter you age: "))

if(age>=18):
    print("He/She can eligible to vote")
else:
    print("Not Eligible to vote")


res="Eligible" if age>=18 else "Not Eligible"
print("You are ",res," to vote")