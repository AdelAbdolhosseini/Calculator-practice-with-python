import math

number1 = input("Please insert the first number: ")
number2 = input("Please insert the second number: ")
operation = input("Please insert desired operation among: + , - , * , / , %, **, math.sqrt: ")
if operation == "+":
    result = float(number1) + float(number2)
elif operation == "+":
    result = float(number1) + float(number2)
elif operation == "*":
    result = float(number1) * float(number2)
elif operation == "/":
    result = float(number1) / float(number2)
elif operation == "%":
    result = float(number1) % float(number2)
elif operation == "**":
    result = float(number1) ** float(number2)

else:
    result = "not exist"

print(result)



