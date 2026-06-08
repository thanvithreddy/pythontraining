grades = eval(input())
avg = sum(grades.values()) / len(grades)
top = max(grades, key=grades.get)
risk = [n for n, s in grades.items() if s < 50]
print(f"Average: {avg} | Top: {top}({grades[top]}) | At Risk: {risk}")