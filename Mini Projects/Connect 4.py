board = [
    [0,0,0,0,0,0,0], #0
    [0,0,0,0,0,0,0], #1
    [0,0,0,0,0,0,0], #2
    [0,0,0,0,0,0,0], #3
    [0,0,0,0,0,0,0], #4
    [0,0,0,0,0,0,0], #5
    [0,0,0,0,0,0,0], #6
    ["A","B","C","D","E","F","G"]] #7

p1_name = ""
p2_name = ""
p1_colour = ""
p2_colour = ""


def Show_Board():
    global board,p1_name,p1_colour,p2_name,p2_colour
    for i in range(0,len(board)):
        print(board[i])

def Data_entry():
    global p1_name,p2_name,p1_colour,p2_colour
    p1_name = input("Enter the name of player 1 ")
    p2_name = input("Enter the name of player 2 ")
    print(p1_name+" select a colour Red or Blue (R/B)")
    p1_colour = input().upper()
    if p1_colour == "R":
        p2_colour = "B"
    else:
        p2_colour = "R"

    #command is crtl + /
    # print("p1 name " ,p1_name)
    # print("p1 colour: ",p1_colour)
    # print("p2 name ",p2_name)
    # print("p2 colour: ",p2_colour)
def Upadate_Board():
    #p1 enters collum, then update board
    #update checks the row of list then adds to lowest rank but check if "" first
    #then check winner, after p2 enters and places
    while not Winner():
        print(f"Its {p1_name}'s turn")
        collumn = input("Which column would u like to place in? ").upper()
        for i in range (0,7):
            if collumn == board[7][i]:
                for n in range (0,8):
                    if not board[n][i] == 0:
                        board[n-1][i] = p1_colour
                    else:
                        pass
            else:
                pass
        Show_Board()
        print(f"Its {p2_name}'s turn")
        collumn = input("Which column would u like to place in? ").upper()
        for i in range(0, 7):
            if collumn == board[7][i]:
                for n in range(0, 8):
                    if not board[n][i] == 0:
                        board[n - 1][i] = p2_colour
                    else:
                        pass
            else:
                pass
            #show moves counter pending addition
        Show_Board()

def Winner():
    #3 types of wins = verical, horizontal, diagonal
#horizontal - uses previous input location if [+/-3][n] (+/- plus minus to indicate both directions) if same end
#vertical - uses previous input, checks coloumn for loop [n][+/-3] by if same end
#diagonal - does previous input for loop y in range(0,4) [n+/-y][n+/-y]
    pass

def main():
    print("Welcome to connehct 4!")
    Data_entry()
    Show_Board()
    Upadate_Board()

main()
#add a validation system for inputing columns