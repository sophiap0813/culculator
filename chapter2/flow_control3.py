# for i in range(12,16):
#print(i)
# for i in range(0,10,2):
#     print(i)
# for i in range(5,-1,-1):
#     print(i)

# import random
# for i in range(5):
#     print( random.randint(1,10))
# import random
# secretNumber =  random.randint(1,50)
# print('I am thinking of a number between 1 and 50')
# for guessesTaken in range(1, 7):
#     print('Take a guess.')
#     guess = int(input())
#     if guess < secretNumber:
#         print('Your guess is too low.')
#     elif guess > secretNumber:
#         print('Your guess is too high')
#     else:
#         break
# if guess == secretNumber:
#     print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
# else:
#     print('Nope. The number I was thinking of was ' + str(secretNumber))
# import random, sys
# print('ROCK, PAPER, SCISSORS')
# wins = 0
# losses = 0
# ties = 0
# while True:
#     print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
#     while True:
#         print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
#         playerMove = input()
#         if playerMove == 'q':
#             sys.exit()
#         if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
#             break
#         print('Type one of r, p, s, or q.')
#
#
#     if playerMove == 'r':
#         print('ROCK versus...')
#     elif playerMove == 'p':
#         print('PAPER versus...')
#     elif playerMove == 's':
#         print('SCISSORS versus...')
#
#
#     randomNumber = random.randint(1, 3)
#     if randomNumber == 1:
#         computerMove = 'r'
#         print('ROCK')
#     elif randomNumber == 2:
#         computerMove = 'p'
#         print('PAPER')
#     elif randomNumber == 3:
#         computerMove = 's'
#         print('SCISSORS')
#
#
#     if playerMove == computerMove:
#         print('It is a tie!')
#         ties = ties + 1
#     elif playerMove == 'r' and computerMove == 's':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 'p' and computerMove == 'r':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 's' and computerMove == 'p':
#         print('You win!')
#         wins = wins + 1
#     elif playerMove == 'r' and computerMove == 'p':
#         print('You lose!')
#         losses = losses + 1
#     elif playerMove == 'p' and computerMove == 's':
#         print('You lose!')
#         losses = losses + 1
#     elif playerMove == 's' and computerMove == 'r':
#         print('You lose!')
#         losses = loss
# spam = 4
# if spam == 1 :
#     print('hello')
# if spam == 2:
#     print('Howdy')
# else:
#     print('Greetingr
# for i in range(1, 11):
#       print(i)
i = 1
while i < 11:
     print(i)
     i= i+1

