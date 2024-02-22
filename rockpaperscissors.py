#lets play rock paper scissors with imports ig
import random as rand

random_number = rand.randint(1, 3)

if random_number == 1:
    computer = "rock"
elif random_number == 2:
    computer = "paper"
elif random_number == 3:
    computer = "scissors"
play = 'Y'

while play == 'Y':
    
    invalid = True
    while invalid == True:
        player = input("rock, paper or scissors? ")

        if player not in ['rock', 'paper', 'scissors']:
            print("invalid input") 
        else:
            invalid = False
            if player == computer:
                print(f"it's a tie, computer chose {computer}")
            elif player == "rock":
                if computer == "scissors":
                    print(f"player wins, computer chose {computer}")
                else:
                    print(f"you lose, computer chose {computer}")
            elif player == "paper":
                if computer == "rock":
                    print(f"player wins, computer chose {computer}")
                else:
                    print(f"computer wins, computer chose {computer}")
            elif player == "scissors":
                if computer == "paper":
                    print(f"player wins, computer chose {computer}")
                else:
                    print(f"computer wins, computer chose {computer}")
            
            random_number = rand.randint(1, 3)
            if random_number == 1:
                    computer = "rock"
            elif random_number == 2:
                    computer = "paper"
            elif random_number == 3:
                    computer = "scissors"
            

            play = input('want to play again? Y/N ')
            if play == 'N':
                    exit()