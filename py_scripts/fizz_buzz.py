"""
Write a program that prints the numbers from 1 to 20. But for multiples of three, print 'Fizz'
instead of the number and for the multiples of five print 'Buzz'.
For numbers which are multiples of both three and five print 'FizzBuzz'.
"""

for num in range(1,20):
    string = ""
    if num % 3 == 0:
        string += "Fizz"
    if num % 5 == 0:
        string += "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string += str(num)
    print(string)
