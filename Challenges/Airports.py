airports = {"LHR":"London Heathrow", "MAN":"Manchester","BHX":"Birmingham","EDI":"Edinburgh","LTN":"London Luton"}
def menu():
    print("Choose one of the following:")
    print("1 - Add new")
    print("2 - Search")
    print("3 - Exit")
    ans = input()
    if ans == "1":
        add_more()
    elif ans == "2":
        search()
    elif ans == "3":
        leave()
    else:
        menu()
def add_more():
    print("Would you like to add an airport?")
    ans = input()
    if ans == "yes": #Upper case need to be accepted
        add_airport()
    else:
        menu()
def add_airport():
    print("Enter AirPort Code: ") #add restriction to 3 letters else retry
    key = input()
    digits = len(key)
    count = 0
    while digits !=3:
        print("Invalid input")
        count +=1
        if count >=3:
            print("Too many attempts have been inputted goodbye.")
            leave()
    print("Enter Airport Name: ")
    value = input()
    airports[key] = value
    print(airports)
    menu()
def search():
    print("Searching options:")
    print("Search for Airport code - 1")
    print("Search for Airport name - 2")
    print("Go back to menu - 3")
    ans = input()
    if ans == "1":
        code_search()
    elif ans =="2":
        name_search()
    elif ans =="3":
        menu()
    else:
        search()
def code_search():
    print("Enter airport name: ")
    name = input()
    code = airports.get(name)
    print(name)
def name_search():
    print("Enter airport code: ")
    code = input()
    value = {i for i in airports if airports[i] == code}
    print("key by value:", value)
def leave():
    exit
menu()