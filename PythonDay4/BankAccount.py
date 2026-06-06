pin=int(input("Enter the PIN: "))
acc_bal=0
if pin==1234:
    print("Welcome to the Bank")

    while True:
        print("1.Deposit")
        print("2.Withdrawal")
        print("3.Balance Enquiry")
        print("4.Exit")

        choice=int(input("Enter Your Choice: "))
        print("\n")
        if(choice==1):
            amount=int(input("Enter the Amount to Deposit : "))
            acc_bal=acc_bal+amount
            print(f"Dear Customer your account XXXXXXXX2055 is credited with {amount}")
        elif(choice==2):
            amount=int(input("Enter the amount to withdraw: "))

            if(amount<acc_bal):
                print(f"Dear Customer your account XXXXXXXX2055 is debited with {amount}")
                acc_bal=acc_bal-amount
            else:
                print("Insufficient Balance.......!")
                break
else:
    print("Entered the Wrong PIN: ")

    