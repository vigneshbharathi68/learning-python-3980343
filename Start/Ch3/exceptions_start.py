# LinkedIn Learning Python course by Joe Marini
# Example file for working with Exceptions
#

# Errors can happen in programs, and we need a clean way to handle them
# This code will cause an error because you can't divide by zero:
# x = 10 / 0

# Exceptions provide a way of catching errors and then handling them in 
# a separate section of the code to group them together
try:
  x = 10/0
except:
  print("Well that didn't work")


# You can also catch specific exceptions
try: 
  answer = input('enter a number for divide by 10')
  print(10 / answer)
except ZeroDivisionError as e:
  print('Number cannot be divide by zero')

