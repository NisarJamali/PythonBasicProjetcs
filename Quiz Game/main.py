print('Welcome to my computer quiz. ')
score = 0


play = input('Do you want to play? ')
if play.lower() != 'yes':
    quit()

answer = input('What does cpu stands for? ')
if answer.lower() == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('First page of website is termed as? ')
if answer.lower() == 'homepage' or 'home page':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('RAM stands for? ')
if answer.lower() == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('PSU stands for? ')
if answer.lower() == 'power supply':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('Who is the father of computer science? ')
if answer.lower() == 'charles babbage':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('Computers, combine both measuring and counting are known as? ')
if answer.lower() == 'hybrid':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('What does E-mail stands for? ')
if answer.lower() == 'electronic mail':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('Who is the father of personal computer? ')
if answer.lower() == 'edward robert':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('The scrambling of code is known as? ')
if answer.lower() == 'encryption':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input('OS stands for? ')
if answer.lower() == 'operating system':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print(f'You got {score} Questions corrent!')
print(f'You got {(score / 10) * 100}%.')