List=list(map(int,input("Enter the list of numbers: ").split()))
List.sort(reverse=True)
print("The sorted list is: ",List)
print(List[-3:])
