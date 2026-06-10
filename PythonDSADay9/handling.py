pin=input("Enter the Password: ")
try:
    if pin=="1234":
        print("Access Granted")
    else:
        raise ValueError("Invalid Password")
except TypeError as e:
    print(e)