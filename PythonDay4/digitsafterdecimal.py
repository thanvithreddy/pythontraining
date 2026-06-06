dec=(input("Enter the Decimal Number: "))
if("." in dec):
    print(dec.split('.')[1])
else:
    print("Error")