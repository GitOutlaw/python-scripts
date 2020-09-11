print('Simple Calculator | version: 0.001')
print('Addition: + | Subtract: - | Multiply: * | Divide: / ')
print()

def operation():
    while True:
        calculation = input('Please enter the calculation: ')
        result = eval(calculation)
        end = ''
        print('The result of your entered calculations is:', result)
        if (calculation == 'end'):
            print('<--- Program End --->')
            break
        else:
            continue
operation()

