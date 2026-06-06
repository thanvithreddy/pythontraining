# List=[i for i in range (2,10,2)]
# Set=[i for i in range (2,10,2)]
# print(List)
# print(sorted(Set))

def add_item(lst, item):
    lst.append(item)

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    else:
        print(item, "not found")














































































items = []

n = int(input("Enter number of operations: "))

for i in range(n):
    operation = input("Enter operation (add/remove): ").lower()

    if operation == "add":
        item = input("Enter item to add: ")
        add_item(items, item)

    elif operation == "remove":
        item = input("Enter item to remove: ")
        remove_item(items, item)

items.sort()

print("\nFinal List:")
for item in items:
    print(item)