#Code Counts from 10-1 to help user with counting  0
count = 10

while count > 0:
    print(count)
    user_input = input('Enter "stop" to cancel or press Enter: ')

    if user_input == 'stop':
        print('Countdown stopped!')
        break

    count -= 1
