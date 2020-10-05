

def calculation():
    while True:
        try:
            num_1 = int(input("Enter a number: "))
            num_2 = int(input("Enter another number: "))
            total = num_1 * num_2
        except ValueError:
            print("Sorry, I didn't understand that, starting over")            
            continue
        else:            
            print("Multiply")
            print(f'{num_1} x {num_2} = {total}')
        if input('Do You Want To Multiply more numbers? y/n ') != 'y':
            break
            
calculation()
 
 
                
        # if total >= 100:
        #     print("Thats a big number!")
        # else:
        #     print("That's not a big number")
           



