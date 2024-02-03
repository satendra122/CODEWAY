A = eval(input())
operator = input()
B = eval(input())

res = 0
if operator == '+':
    res = A + B
    print(res)
elif operator == '-':
    res = A - B
    print(res)
elif operator == '*':
    res = A * B
    print(res)
elif operator == '/':
    if B != 0:
        res = A / B
        print(res)
    else:
        print("Error: Division by Zero is  not allowed.")
        exit()
else:
    print("Invalid opertor.")
