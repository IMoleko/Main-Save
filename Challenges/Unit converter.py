def meter_yrds():
    print("Enter mesurement in meters")
    meters = float(input())
    yards = meters * 1.09361
    print("This is " + str(meters) + "m" + " in yards: " + str(yards))
    print("would you like to use the program again?")
    opt = input()
    if opt.lower() == "yes":
        menu()
    else:
        print("Thank you for using the unit converter.")
        exit


def kg_pound():
    print("Enter mesurement in Kilograms")
    kg = float(input())
    pound = kg * 2.20462
    print("This is " + str(kg) + "kg" + " in pounds: " + str(pound))
    print("would you like to use the program again?")
    opt = input()
    if opt.lower() == "yes":
        menu()
    else:
        print("Thank you for using the unit converter.")
        exit


def litre_pint():
    print("Enter mesurement in liters")
    liters = float(input())
    pints = liters * 1.75975
    print("This is " + str(liters) + "l" + " in pints: " + str(pints))
    print("would you like to use the program again?")
    opt = input()
    if opt.lower() == "yes":
        menu()
    else:
        print("Thank you for using the unit converter.")
        exit


def pounds_dollars():
    print("Enter mesurement in pounds")
    pounds = float(input())
    dollars = pounds * 1.11
    print("This is £" + str(pounds) + " in dollars: $ " + str(dollars))
    print("would you like to use the program again?")
    opt = input()
    if opt.lower() == "yes":
        menu()
    else:
        print("Thank you for using the unit converter.")
        exit


def menu():
    print("Select from the options below:")
    print("1. Meter to Yards")
    print("2. Kg to Pounds")
    print("3. Litres to Pints")
    print("4. Pounds to Dollars")
    print("5. Exit program")
    option = input()
    if option == "1":
        meter_yrds()
    elif option == "2":
        kg_pound()
    elif option == "3":
        litre_pint()
    elif option == "4":
        pounds_dollars()
    elif option == "5":
        exit
    else:
        print("error with entery, try again")


print("Welcome to the unit converter")
menu()