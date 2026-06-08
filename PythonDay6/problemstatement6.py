List=list(map(int,input("Enter the Available Slots: ").split()))
required_slots=int(input("Enter the Requested Slots: "))
print("Available Slots: ",List)
print("Requested Slot: ",required_slots)
if required_slots in List:
    print("Slot is available")

else:
    print("Requested Slot is not available")
