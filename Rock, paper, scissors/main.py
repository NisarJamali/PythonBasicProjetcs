import random

print("Welcome to the game.")

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    play = input("Enter rock/paper/scissors to play and Q to quit: ").lower()
    if play == 'q':
        break
    if play not in options:
        continue

    random_number = random.randint(0, 2)
    # 0 : rock, 1: paper, 2: scissors
    computer_pick = options[random_number]
    print(f'Computer picked {computer_pick}.')
    if play == 'rock' and computer_pick == 'scissors':
        print('You Won!')
        user_wins += 1
    elif play == 'paper' and computer_pick == 'rock':
        print('You Won!')
        user_wins += 1
    elif play == 'scissors' and computer_pick == 'paper':
        print('You Won!')
        user_wins += 1

    elif play == 'scissors' and computer_pick == 'scissors':
        print("It was a Tie")
        continue

    elif play == 'paper' and computer_pick == 'paper':
        print("It was a Tie")
        continue
    elif play == 'rock' and computer_pick == 'rock':
        print("It was a Tie")
        continue
    else:
        print("You Lost!")
        computer_wins += 1

print(f'You won {user_wins} times.')
print(f'Computer won {computer_wins} times.')
print('Goodbye!')