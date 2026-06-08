n=7
Revenue=[]
for i in range(n):
    ele=int(input("Enter the Revenue of the day :"))
    Revenue.append(ele)
print(f"Total Revenue :{sum(Revenue)} | Best Day:{max(Revenue)} | Worst Day:{max(Revenue)}")