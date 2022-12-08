def decider():
    print("Does your animal have wings?")
    answer = input()
    match answer:
        case "yes":
            print("Does your animal fly?")
            n = input()
            if n == "yes":
                insect()
            else:
                birds()
        case "no":
            print("Does your animal breathe underwater?")
            w = input()
            if w == "yes":
                mollusk()
            else:
                mammals()

def mammals():
    print("Is your animal aquatic (Yes/No)")
    Answer = input()
    match Answer:
        case "yes":
            print("fish")
        case "no":
            print("dog")
def birds():
    print("bird")
def insect():
    print("insect")
def mollusk():
    print("mollusk")

decider()