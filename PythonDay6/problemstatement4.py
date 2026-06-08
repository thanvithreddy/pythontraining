Godown_A=list(map(str,input("Enter the items in Godown A: ").split()))
Godown_B=list(map(str,input("Enter the items in Godown B: ").split()))
print("Unified Inventory : ",set(Godown_A+Godown_B))