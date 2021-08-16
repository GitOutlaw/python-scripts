# Leap Year Check

year = int(input("Which year do you want to check?: "))

if year % 4 != 0:
    print("Not Leap Year")

elif year % 100 != 0:
    print("Leap Year")

elif year % 400 == 0:
    print("Leap Year")
