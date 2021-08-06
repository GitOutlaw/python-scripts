"""
Write a program that prints the numbers from 1 to 20. But for multiples of three, print 'Fizz'
instead of the number and for the multiples of five print 'Buzz'.
For numbers which are multiples of both three and five print 'FizzBuzz'.
"""

# standard solution

for num in range(1,20):
  string = ""
  if num % 3 == 0:
    string += 'Fizz'
  if num % 5 == 0:
    string += 'Buzz'
  if num % 3 != 0 and num % 5 != 0:
    string += str(num)
  print(string)

# lambda solution

print(*map(lambda i: 'Fizz'*(not i%3)+'Buzz'*(not i%5) or i, range(1,20)),sep='\n')
    
  


