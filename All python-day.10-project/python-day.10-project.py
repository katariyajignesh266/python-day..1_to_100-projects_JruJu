import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculate():
    print(art.logo)
    abc = True
    num1 = int(input("What's the first number?:"))

    while abc:
        for oper in operations:
            print(oper)
        oper = input("Pick an operation: ")
        num2 = int(input("What's the next number?:"))

        Result = operations[oper](num1, num2)

        print(f"{float(num1)} {oper} {float(num2)} = {float(Result)}")

        choose = input(f"Type 'y' to continue calculating with {float(Result)}, or type 'n' to start a new calculation:")

        if choose == "y":
            num1 = Result
        else:
            abc = False
            print("\n" *2)
            calculate()


calculate()
