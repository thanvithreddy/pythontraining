print("Program Starts")
a=10
print("A=",a
      )
try:
    print(a/0)
except ZeroDivisionError as e:
    print("You cannot divide a number by zero")
print("Program Ends")