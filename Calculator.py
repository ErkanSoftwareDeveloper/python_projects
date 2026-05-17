print("---Mini Calculator---")

num1 = float(input("1st number: "))
num2 = float(input("2nd number: "))

print("---Choose operation---:")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")

select = input("Operation: ")

if  select == "+":
    print("Result:", num1 + num2)

elif select == "-":
    print("Result:", num1 - num2)

elif select == "*":
    print("Result:", num1 * num2)

elif select == "/":
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        print("Result:", num1 / num2)

else:
    print("Invalid operation!")
