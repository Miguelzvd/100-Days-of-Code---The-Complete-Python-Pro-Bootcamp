import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


calculator_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(art.logo)
    num1 = int(input("What's the first number?: "))

    continue_with_result = True

    while continue_with_result:

        operation = input("+\n"
                          "-\n"
                          "*\n"
                          "/\n"
                          " Pick an operation: ")

        num2 = int(input("What's the second number?: "))

        result = calculator_operations[operation](num1, num2)

        print(f"{num1} {operation} {num2} = {result}")

        should_calculating = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new "
                                   f"calculation: ")

        continue_with_result = False

        num1 = result

        if should_calculating == "y":
            continue_with_result = True

    calculator()


calculator()

