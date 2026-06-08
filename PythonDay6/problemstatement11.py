ifsc = input().strip()

if len(ifsc) != 11:
    print("Invalid — IFSC must be 11 characters")
elif not ifsc[:4].isalpha():
    print("Invalid — First 4 characters must be alphabets")
elif ifsc[4] != '0':
    print("Invalid — 5th character must be '0'")
else:
    print("Valid IFSC Code")