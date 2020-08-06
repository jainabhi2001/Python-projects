import time
import random

print(" __    __       __       __    _   ________   _      _       __       __    _  ")
print("|  |  |  |     /  \     |   \ | | |  ____  | | \    / |     /  \     |   \ | | ")
print("|  |__|  |    / -- \    | |\ \| | | |    | | |  \  /  |    / -- \    | |\ \| | ")
print("|   __   |   /  __  \   | | \   | | |_____   |   \/   |   /  __  \   | | \   | ")
print("|  |  |  |  /  /  \  \  | |  \  | |_____  |  | |\__/| |  /  /  \  \  | |  \  | ")
print("|__|  |__| /__/    \__\ |_|   \_|       |_|  |_|    |_| /__/    \__\ |_|   \_| ")
print("")


nam=input("Enter your name:")
print("Hey ",nam.upper()," welcome to Hangman game")

detail={'education':"Weapon of a literate ",
        'interview':"Formal conversation between people",
        'computer':"A machine ",
        'science':"World of experiments",
        'programming':"Not a normal typing",
        'hangman':"Game of luck and mind ",
        'foxglove':"cure of a disease",
        'felicitation':"Words of praise",
        'ceremony':"A event",
        'reverse':"Opposite",
        'blockchain':"Immutable technology ",
        'cryptocurrency':"It has value but invisible in real world",
        'ethical': "Legal",
        'covid':"What is 2020 known for.."}

answers=list(detail.keys())
ans=random.choice(answers)                                              # "choice" function of random module choose a random option from the list


guessedwords=""
all_wrong_letter_choosen=[]

print("")
time.sleep(1)                                                           # delays the program by 1 second

print("Game is going to start...")
time.sleep(0.5)                                                         # delays the program by 0.5 second
print("Ok start guessing the word:You have 10 chances")

print("")
hint=detail[ans]
print("So your hint is :",hint)

chance=10


while chance > 0:
    guess=input("\n Guess a letter:")
    guessedwords += guess

    wrong=0
    for each in ans:
        if each in guessedwords:
            print(each)
        else:
            print("_")
            wrong+=1


    if wrong==0:
        print("")
        print("Well done !!! You got the right word")
        print("The word is ",ans.upper())
        exit(0)

    if guess not in ans:
        print("")
        print("Guessed wrong letter")
        chance -= 1
        all_wrong_letter_choosen.append(guess)
        if chance==9:
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("")
            print("You have ",chance," chances left with you")
        elif chance==8:
            print("_|___________")
            print(" |           ")
            print(" |           ")
            print(" |           ")
            print(" |           ")
            print(" |           ")
            print(" |           ")
            print(" |")
            print("")
            print("You have ", chance, " chances left with you")
        elif chance==7:
            print("_|___________")
            print(" |           ")
            print(" |      O    ")
            print(" |           ")
            print(" |           ")
            print(" |           ")
            print(" |           ")
            print(" |")
            print("")
            print("You have ", chance, " chances left with you")
        elif chance==6:
            print("_|___________")
            print(" |           ")
            print(" |      O    ")
            print(" |      |    ")
            print(" |      |    ")
            print(" |           ")
            print(" |           ")
            print(" |")
            print("")
            print("You have ", chance, " chances left with you")
        elif chance==5:
            print("_|___________")
            print(" |           ")
            print(" |      O    ")
            print(" |      |    ")
            print(" |      |    ")
            print(" |     /     ")
            print(" |    /      ")
            print(" |")
            print("")
            print("You have ", chance, " chances left with you")
        elif chance==4:
            print("_|___________")
            print(" |           ")
            print(" |      O    ")
            print(" |      |    ")
            print(" |      |    ")
            print(" |     / \   ")
            print(" |    /   \  ")
            print(" |")
            print("")
            print("You have ", chance, " chances left with you")
        elif chance==3:
            print("_|___________")
            print(" |           ")
            print(" |      O    ")
            print(" |   ___|    ")
            print(" |      |    ")
            print(" |     / \   ")
            print(" |    /   \  ")
            print(" |")
            print("")
            print("You have ", chance, " chances left with you")
        elif chance==2:
            print("_|___________")
            print(" |           ")
            print(" |      O    ")
            print(" |   ___|___ ")
            print(" |      |    ")
            print(" |     / \   ")
            print(" |    /   \  ")
            print(" |")
            print("")
            print("You have ", chance, " chances left with you")
        elif chance==1:
            print("_|______|____")
            print(" |      |    ")
            print(" |      O    ")
            print(" |   ___|___ ")
            print(" |      |    ")
            print(" |     / \   ")
            print(" |    /   \  ")
            print(" |")
            print("")
            print("You have ", chance, " chances left with you")


    else:
        print("")
        print("Hurray guessed correct letter ")

    print("All wrong letter that you have guessed till now are (Don't press them again):", all_wrong_letter_choosen)

print("_|______|____")
print(" |      |    ")
print(" |    ( 0 )  ")
print(" |  ____|____")
print(" |      |    ")
print(" |     / \   ")
print(" |    /   \  ")
print(" |")
print("")
print("!!  DEAD  !!")
print(""" Sorry!! You lost the game.
        Better luck next time !! """)





