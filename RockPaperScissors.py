#this program plays rock paper scissors
game = 0
import random

#loop the program and make a way to stop it

stop = 't'
while stop != 's':
#prompt the user to pick rock, paper, or scissors?
    you = input("Rock, Paper or Scissors?\n").lower()

    print('you chose: ' + you)

#create a random variable for cpu
    list = [1, 2, 3]
    game = random.choice(list)
#assign number to rock, paper and scissors
    if game == 1:
        game = 'rock'
    elif game == 2:
       game = 'paper'
    else : game = 'scissors'
    print("the cpu chose: " + game)
#assign win loss rules
    if you == 'rock' and game == 'paper':
        print('cpu wins')
    elif you == 'paper' and game == 'scissors':
        print('cpu wins')
    elif you == 'scissors' and game == 'rock':
        print('cpu wins')
    elif game == 'rock' and you == 'paper':
        print('you win')
    elif game == 'paper' and you == 'scissors':
        print('you win')
    elif game == 'scissors' and you == 'rock':
        print('you win')
    elif game == 'rock' and you == 'rock':
        print('tie')
    elif game == 'paper' and you == 'paper':
        print('tie')
    elif game == 'scissors' and you == 'scissors':
        print('tie')
    else:
        print('your input was invalid')
    stop = input("type: 's' to stop the game, press enter to continue\n")
    input('Press ENTER to exit')
