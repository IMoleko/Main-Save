from random import randint

# possible symbols (the original task specifies words)
symbol = ("Cherry", "Bell", "Lemon", "Orange", "Star", "Skull")
# start off with £1, but work in pennies to avoid
# floating point errors
credit = 100
response = ""
print("Press Enter to play again; enter any symbol to stop.\n")
while credit >= 20 and response == "":
  # array containing slot machine results
  reel = []
  display = ""
  # 20 p spin fee
  credit -= 20
  # generate three random symbols
  for r in range(3):
    #our random value
    s = randint(0,5)
    reel.append(symbol[s])
    display += symbol[s] + " "
  print(display[:-1])
  # sort the list to facilitate comparison (as two
  # symbols the same will be next to each other
  reel.sort()
  # lose all your money if you get three skulls
  if reel.count("Skull") == 3:
    credit = 0
  # win £5 if you get three bells
  elif reel.count("Bell") == 3:
    credit += 500
  # win £1 for three symbols the same
  elif reel[0] == reel[2]:
    credit += 100
  # lost £1 for two skulls (but don't go negative)
  elif reel.count("Skull") == 2:
    credit -= min(100,credit)
  # win 50p for two symbols the same
  elif reel[0] == reel[1] or reel[1] == reel[2] or reel[0] == reel[2]:
    credit += 50
  # divide credit by 100 and display as £s
  print("Credit:","£%.2f" % (credit/100))
  if credit >= 20:
    response = input()