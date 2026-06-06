# sentence = input("Enter the Feedback: ")

# words = sentence.split()

# longest_word = words[0]

# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word

# print(longest_word)
# # print("Length:", len(longest_word))

marks = int(input("Enter a value : "))
if (marks>=90):
    print("A")
elif(marks>=75 and marks<90):
    print("B")
elif(marks>=60 and marks<75):
    print("C")
elif(marks>=40 and marks <60):
    print("D")
else:
    print("Fail")