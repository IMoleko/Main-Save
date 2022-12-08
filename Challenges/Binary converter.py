num = int(input())
binum = ""

while num != 0:
    n1 = num // 2
    n2 = num % 2
    num = n1
    binum = str(n2) + binum

print("The binary number is: " + binum)