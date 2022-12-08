def tempcheck():
    if temp in range(30, 45):
        print('ok')
        return True
    else:
        print("Error occured")
        return False


def weather():
    temp = 0
    hour = 1
    total = 0
    fever = 0
    while hour < 8:
        temp = input("Enter temperature: ")
        temp = float(temp)
        tempcheck()
        while tempcheck() == True
            continue
        fever > 37
        fever = fever + 1
        total = total + temp
        hour = hour + 1
    average = round(total / hour, 1)  # round to 1 decimal place
    print("Average temperature: ", average)
    print("Inc idents of fever: ", fever)


print("would you like to use the weather program")
answer = input().lower()
if answer == "yes":
    weather()
    answer = input().lower()