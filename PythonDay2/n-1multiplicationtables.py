n=int(input("Enter The Number: "))

for i in range(n,0,-1):
    print("Multiplication Table of : ",i) 
    for j in range(1,11):
            
            print(f"{i} × {j} = {i*j}")


