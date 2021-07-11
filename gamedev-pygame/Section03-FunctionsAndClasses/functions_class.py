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