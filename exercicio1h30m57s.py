command = ""
print('Type "help" to see the options.')
car_started = 0
car_stopped = 1

while command != 'QUIT':
    command = input('> ').upper()
    if command == 'HELP':
        print('Start - To start the car\n'
          'Stop - To stop the car\n'
          'Quit - To exit\n')
    elif command == 'START':
        if car_started == 0:
            print('Car started. Ready to go.\n')
            car_started = 1
            car_stopped = 0
        else:
            print('Car is already started!\n')
    elif command == 'STOP':
        if car_stopped == 0:
            print('Car stopped.\n')
            car_stopped = 1
            car_started = 0
        else:
            print('HEY! The car is already stopped. What are you doing?\n')
    elif command == 'QUIT':
        break
    else:
        print("I don't understand that.\n")
