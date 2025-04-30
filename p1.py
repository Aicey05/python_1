num1=int(input("Enter the first number:"))
operator=(input("Enter any operator(+,-,*,/)"))
num2=int(input("Enter the second number:"))
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"


print(f"{num1} {operator} {num2} = {result}")
