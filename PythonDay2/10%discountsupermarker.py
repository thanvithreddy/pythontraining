amount=int(input("Enter the Bill Amount: "))

if(amount>500):
    print("Discount Applicable")
    discount=(amount/100)*10 
    print("Bill After Discount of 10% = ",amount-discount)

else:
    print("No Discount")

