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


answer = input("do you want to solve quadratic? ").lower()

while answer == "yes":
    quadsolver()
    answer = input("do you want to solve another quadratic? ").lower()
print("Thank you for using program")
