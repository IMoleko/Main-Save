def get_Total(card_no):
    total = 0
    card_no.replace({"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8,"9":9,"0":0})

    return total


def format_check():
    pass


def length_check(card_no):
    k = len(card_no)
    if k == 11:
        return True
    else:
        return False


def isValid(total):
    r = total % 10
    if r == 0:
        return True
    else:
        return False


def main():
    count = 0
    card_no = input("Enter card number")
    while length_check(card_no) == False:
        count += 1
        if count >= 3:
            print(" too many attempts")
            exit(0)
        else:
            print("Invalid - Try again")
            card_no = input("Enter card number")

    total = get_Total(card_no)
    while isValid(total) == False:
        print("Invalid - Try again")
        card_no = input("Enter card number")
        total = get_Total(card_no)
        count += 1
        if count >= 3:
            print(" too many attempts")
            exit(0)

main()