number=int(input("Enter the Number of Pizzas: "))
size=(input("Enter the Size of the Pizza: "))

toppings=int(input("Enter the Number of Toppings: "))
list=['Cheese','Pepporoni','Olive','Jalapenos']
print("Available Toppings: ",list)

topping_price = 0

for j in range(1, toppings + 1):

    toppings_name = input("Enter Your Topping : ")

    if toppings_name == "Cheese":
        topping_price += 2

    elif toppings_name == "Pepporoni":
        topping_price += 3

    elif toppings_name == "Olive":
        topping_price += 5

    elif toppings_name == "Jalapenos":
        topping_price += 5

    else:
        print("Selected Topping Not Available")
for i in range(1,number+1,1):
    
        if(size=="small" or size=="Small"):
               billamount=10
               
            

        elif(size=="Medium" or size=="medium"):
               billamount=15
              
           
        

        elif(size=="large" or size=="Large"):
               billamount=20

print("Total Bill : ",(number*billamount+topping_price))
              
        



            
