n=int(input("Enter The Number: "))

for i in range(1,n+1):
    print("Multiplication Table of : ",i) 
    for j in range(10,0,-1):
            
            print(f"{i} × {j} = {i*j}")


