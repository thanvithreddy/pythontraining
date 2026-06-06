import copy

a=[10,20,30]

b=[25,25]
a=copy.copy(b)
print(a)

b.append(45)