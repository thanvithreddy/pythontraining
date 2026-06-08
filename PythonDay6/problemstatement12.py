first = input("First Name: ")
last = input("Last Name: ")
phone = input("Phone Number: ")

pnr = first[:2].upper() + last[:2].upper() + phone[-2:]
print("PNR:", pnr)