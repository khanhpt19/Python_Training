listItem = ['clothes', 'cap', 'phone']
listItem += list(input('Enter list item: ').split(','))

k = 0
while k == 0:
    item = input('Enter item need check: ')
    if item != '':
        if item in listItem:
            print('Available')
        else:
            print('Out of stock!')
    else:
        k = 1
