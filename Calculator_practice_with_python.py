number1 = input("Please insert the first number: ")
number2 = input("Please insert the second number: ")
operation = input("Please insert desired operation among: + , - , * , / :  ")
if operation == "+":
    result = float(number1) + float(number2)
if operation == "-":
    result = float(number1) - float(number2)
if operation == "*":
    result = float(number1) * float(number2)
if operation == "/":
    result = float(number1) / float(number2)

print(result)



