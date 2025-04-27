a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
operation = input("Введіть операцію (+, -, *, /): ")

if operation == '+':
    result = a + b
    print(f"Результат: {result}")
elif operation == '-':
    result = a - b
    print(f"Результат: {result}")
elif operation == '*':
    result = a * b
    print(f"Результат: {result}")
elif operation == '/':
    if b == 0:
        print("Ділення на нуль!")
    else:
        result = a / b
        print(f"Результат: {result}")
else:
    print("Невідома операція!")