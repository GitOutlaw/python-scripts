# If bill was $150.00, split between 5 people 12% tip.
# Each person should pay (150.00 /5) * 1.12
# Round the result to 2 decimal points = 33.60

print('Welcome to the tip calculator')

bill = float(input('What was the total of the bill $'))
tip = int(input('What percentage tip would you like to give? 10, 12, 15? '))
people = int(input('How many people to split the bill? '))

tip_as_percent = tip / 100
total_tip_ammount = bill * tip_as_percent
total_bill = bill + total_tip_ammount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)


print(f'Each person should pay ${final_amount:.2f}')
