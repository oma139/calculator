import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

# Using functions as KEYS
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    num1 = float(input("Write the first number"))

    while True:
        operator = input("pick an operation (+, -, *, /): ")
        num2 = float(input("Write the second number"))

        if operator in operations:
            result = operations[operator](num1,num2)
            print(f"result = :{result}")
        else:
            print("invalid operator")

        cont = input(f"type 'y' to continue calculating with {result}, or 'n' to start a new calculation").lower()

        if cont == "y":
            num1 = result
        else:
            calculator()



calculator()
