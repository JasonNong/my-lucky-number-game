''' from random import randint

print ("Do you want to play a game?")
good = input()
while good != "yes":
  print ("You have to answer yes you ding dong gong")
  good = input()
print ("Guess my number")

guess = int(input())
num = randint(1, 20)
while guess != num:
  print ("Wrong! U cusstard")
  print("Try again snoopy")
  guess = int(input())
print ("U are intelligent, this is good for mars", num, "is my number") '''

# How I would make it 6 months later

from random import randint

def yes():
    good = input("Play a game with me [Y/N]").upper()
    if good != 'Y':
        print ('U have no choice mortal')
        yes()
    elif good == 'Y':
        pass
  
yes()





def yoink():
    comp = randint(1, 20)
    z=1
    guess = int(input("Guess my number\n"))
    
    while z:
        if comp != guess and comp > guess:
            print ("It is bigger than that!")
            guess = int(input("Guess my number\n"))
        elif comp != guess and comp < guess:
            print ("It is smaller than that!")
            guess = int(input("Guess my number\n"))
        else:
            print("You got it")
            replay = input("Wanna play again [Y/N]").upper()
            if replay == 'Y':
                comp = randint(1, 20)
                yoink()
            else:
                exit()

        


yoink()