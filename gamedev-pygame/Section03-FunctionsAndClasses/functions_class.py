# Python Void Functions
def homework_task(lang):
  print('Your homework task: ')
  print(f'Declare a variable in "{lang}"')

print('===== Start =====')
homework_task('Python')
print('===== End =====')

# Return Functions
def name_uppercase(name):
  print(f'Hello {name}!')
  return name.upper()

name_res = name_uppercase('Laureano')
print(name_res)

# Classes, Objects and Methods
class Animal:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def run(self):
    print('Running...')

  def eat(self):
    print('Eating...')

dog = Animal('Perri', 'Brown')
dog.run()

print(dog.name)

# Modules
from module import random
print(random(8))