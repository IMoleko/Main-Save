def menu():
    operartions = ["Addition - 1", "Multiplication - 2", "Subtraction - 3", "Division - 4", "Quadratic solver - 5"]
    print("Here are your options: ")
    w = len(operartions)
    for k in range(0, w):
        print(operartions[k])
    print("")
    selection = input()
    match selection:
        case "1":
            addition()
        case "2":
            multiplication()
        case "3":
            subtraction()
        case "4":
            division()
        case "5":
            quadsolver()
        case other:
            print("no option available, retry")
            menu()


def quadsolver():
    a = float(input("Please enter A"))
    b = float(input("Please enter B"))
    c = float(input("please enter C"))
    d = b * b - 4 * a * c

    if d == 0:
        x1 = -b / (2 * a)
        x2 = x1
        print(x1, x2)
    elif d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print(x1, x2)
    else:
        print("There is no real answer")


def addition():
    print("Enter the first number: ")
    x = float(input())
    print("Enter the second number: ")
    y = float(input())
    answer = x + y
    print(answer)
    retry()


def multiplication():
    print("Enter the first number: ")
    x = float(input())
    print("Enter the second number: ")
    y = float(input())
    answer = x * y
    print(answer)
    retry()


def subtraction():
    print("Enter the first number: ")
    x = float(input())
    print("Enter the second number: ")
    y = float(input())
    answer = x - y
    print(answer)
    retry()


def division():
    print("Enter the first number: ")
    x = float(input())
    print("Enter the second number: ")
    y = float(input())
    answer = x / y
    print(answer)
    retry()


def retry():
    print("Would you like to reuse the calculator? ")
    n = input()
    if n.lower() == "yes":
        menu()
    else:
        print("Goodbye, thank you for using Ivan's Incredible Calculator.")
        exit()


print("Welcome to Ivan's incredible calculator")
menu()
