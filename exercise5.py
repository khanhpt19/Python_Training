listBook = {'history': 10, 'math': 20, 'literature': 0}
k = 0
while k == 0:
    item = input('Enter item to check: ')
    if item != '':
        if item in listBook and listBook[item] > 0:
            print(listBook[item], ' items available')
        else:
            print('Out of stock!')
    else:
        k = 1
