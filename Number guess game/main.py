import random

top_of_range = input("type a number. ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0 :
        print("Please type a number larger than 0 next time")
        quit()
else :
    print('Please type a number next time')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    guess = input("Make a guess. ")    
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Please enter a number next time')
        continue

    if guess == random_number:
        print("You got it correct!")
        break
    elif guess > random_number:
        print('you were above the number.')
    else :
        print('you were below the number.')

print(f'you got it in {guesses} guesses!')

