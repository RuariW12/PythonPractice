# conditional expression = A one line shortcut for the if else statement (ternary operator)
# Print or assign one of two values based on a condition
# x if condition else Y

num = 5

print("Positive" if num > 0 else "Negative")

num1 = 6

result = "Even" if num1 % 2 == 0 else "Odd"
print(result)

a = 6
b = 7

max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)
print(min_num)
