weight = float(input('Weight: '))
option = str(input('Press [L] to Lbs or [K] to Kg: ')).upper()

if option == 'L':
    print('You are {:.2f} kilos.'.format(weight * 0.453592))
elif option == 'K':
    print('You are {:.2f} pounds.'.format(weight * 2.20462))
else:
    print('Error! Error! Error! Error!')
