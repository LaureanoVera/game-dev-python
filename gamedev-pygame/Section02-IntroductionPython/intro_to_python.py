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

# OPERATIONS WITH STRINGS
lauri = 'I love programming and I learn every day'

print(lauri.upper())
print(lauri.lower())
print(lauri.find('e'))
print(lauri.replace('love', 'just like'))
print(lauri.find('programming'))

# ARITHMETIC OPERATIONS
x = 5
y = 11

x += y 
y -= x
x *= y
y /= x

# COMPARISONS AND LOGICAL OPERATIONS
x = 5 > 4
print(x)
x = 5 < 4
print(x)
x = 5 == 4
print(x)
x = 5 != 4
print(x)
x = True and False
print(x)
x = True or False
print(x)

# IF STATEMENT
car_speed = 60
if car_speed > 100:
  print('You drive too fast')
elif car_speed < 20:
  print('You drive too slow. This is a highway')
else:
  print('You speed is good')

# EXERSICE 2: If Statements
degree = input('What us yout degree? Master, Bachelor or PhD? ')
experience = input('How many years of experience do you have? ')

if degree == 'Master' or degree == 'PhD':
  if int(experience) >= 2:
    print('You are accepted for the interview')
  else:
    print("You don't have enough experience")
else:
  print("You don't have the required degree")
