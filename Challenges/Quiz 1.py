print("Welcome to my program")

name =""
while len(name)==0:
    name = input("Enter name: ")
print("Hello "+name)

re_enter =""

score = 0

answer = input("Would you like to take a quiz or make a list? ")

if answer.lower() =="quiz":
    quiz = input("What does RNG stand for? ")
    if quiz.lower()== "random number generator":
        print("Correct!")
    score+=1
else:print("incorrect!")



#elif answer.lower() =="list":
    #list = input("lo")





