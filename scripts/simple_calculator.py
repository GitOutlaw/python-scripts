print()
print('Simple Calculator | Version: 0.03')
print('Addition: + | Subtract: - | Multiply: * | Divide: / ')
print()


def operation():
    while True:
        user_input = input('Please enter a calculation: ')
        result = eval(user_input)
        end = ''
        print('The result of your entered calculations is: ', result)
        print('Enter exit to end the program')
        if user_input == 'end':
            print('End Program')
            break
        else:
            continue
        

operation()

