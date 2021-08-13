# If bill was $150.00, split between 5 people 12% tip.
# Each person should pay (150.00 /5) * 1.12
# Round the result to 2 decimal points = 33.60

print('Welcome to the tip calculator')

bill = float(input('What was the total of the bill $'))
tip = float(input('What percentage tip would you like to give? 10, 12, 15? '))
people = float(input('How many people to split the bill? '))

tip_percent = tip / 100
total = bill * tip_percent
final_total = total + bill
split = round(final_total, 3) // people

print(f'${split:.2f}')
