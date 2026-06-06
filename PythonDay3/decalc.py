def add(a,b):
    print(f"Addition of {a} and {b} is {a+b}")

def sub(a,b):
    print(f"Subtraction of {a} and {b} is {a-b}")
def multiply(a,b):
    print(f"Multiplication of {a} and {b} is {a*b}")
def divide(a,b):
    print(f"Division of {a} and {b} is {a//b}")
def rem(a,b):
    print(f"Remainer  of {a} and {b} is {a+b}")

while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Divide")
    print("5.Modulus")
    choice = int(input("Enter Your Choice: "))
    if choice == 6:
        break 
a=int(input("Enter the first Number: "))
b=int(input("Enter the second Number: "))

if choice==1:
    add(a,b)
elif  choice==2:
    sub(a,b)
elif  choice==3:
    multiply(a,b)
elif choice==4:
    divide(a,b)
elif choice==5:
    rem(a,b)

