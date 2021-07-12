from random import randint

start = 1
end = 100
value = randint(start, end)

print(f'The computer choose a number between {start} and {end}')

user_num = None

while user_num != value:
    user_num = int(input('Guess the number: '))

    if user_num < value:
      print('The number is Higher')
    elif user_num > value:
      print('The number is Lower')

print('Congratulations!!! You guess the number. You won.')