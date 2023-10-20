a = int(input("Напишете първото число: "))
b = int(input("Напишете второто число: "))
operator = str(input("Изберте оператор: "))

if operator == "+":
    c = a + b
    print(c)
elif operator == "-":
    c = a - b
    print(c)
elif operator == "*":
    c = a * b
    print(c)
else:
    c = a / b
    print(int(c))
