taxis = [
    ["", -99],
    ["", -99],
    ["", -99],
    ["", -99],
    ["", -99],
    ["", -99],
    ["", -99],
    ["", -99],
    ["", -99],
    ["", -99],
    ["", -99]]
head = 0
next_free = 0


def add():
    global taxis, head, next_free
    new_taxi = input("Enter car reg")
    taxis[head][0] = new_taxi
    taxis[head][1] = -1
    next_free += 1
    print(taxis)
    n = 1
    while n < 10:
        print("Would you like to add more?")
        ans = input()
        if ans == "yes":
            new_taxi = input("Enter car reg")
            taxis[next_free][0] = new_taxi
            taxis[next_free][1] = -1
            taxis[next_free - 1][1] = next_free
            next_free += 1
            print(taxis)
            n += 1
        else:
            break


def swap():
    print("Would you like to swap 2 taxis?")
    ans = input()
    if ans == "yes":
        pass
    else:
        print("Do you want to exit or return?")
        ans = input()
        if ans == "exit":
            exit(0)
        else:
            add()

    global driver2_index, driver1_index
    driver1 = input("Which driver are you?")
    driver2 = input("which driver would you like to switch ranks with?")

    for i in range(0, 10):
        if driver1 == taxis[i][0]:
            driver1_index = i
        if driver2 == taxis[i][0]:
            driver2_index = i

    temp = taxis[driver1_index][1]
    taxis[driver1_index][1] = taxis[driver2_index][1]
    taxis[driver2_index][1] = temp
    print(taxi)


def leaving():
    taxi_left = input("Has the head taxi left?")
    if taxi_left == "yes":
        pass

def main():
    add()
    swap()
    main()


main()