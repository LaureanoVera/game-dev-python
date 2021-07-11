print('Hello World')

date = 21
pi = 3.14
name = 'Laureano'
eat = True

# TAKING INPUTS FROM THE USER
game = input('Who is your favorite game: ')

print(f'My favorite game is {game}')

# LOGICAL OPERATIONS
your_age = int(input('How old are you? '))
birth_yaner = 2021 - your_age

print(birth_yaner)

# EXERSICE 1: Inputs and Logical Operations
num_a = float(input('Number a: '))
num_b = float(input('Number b: '))
subtract = num_a - num_b

print(f'Result: {subtract}')

if subtract < 0:
  print('Negative Number')
else:
  print('Positive Number')
