num = ['0', '1', '2', '3', '4', '5', '6', '7', '8' ]

def printBoard():
    print(num[0] + ' | ' + num[1] + ' | ' + num[2] + ' | ')
    print('__+___+___+')
    print(num[3] + ' | ' + num[4] + ' | ' + num[5] + ' | ')
    print('__+___+___+')
    print(num[6] + ' | ' + num[7] + ' | ' + num[8] + ' | ')

def move_input_x():
    move = input('You are X. Enter the number corresponding to your move: ')
    if int(move) > 8 or int(move) < 0:
        print('Incorrect input, please try again.')
        move_input_x()
    elif num[int(move)] == move:
        num[int(move)] = 'X'
    else:
        print('Incorrect input, please try again.')
        move_input_x()

def move_input_o():
    move = input('You are O. Enter the number corresponding to your move: ')
    if int(move) > 8 or int(move) < 0:
        print('Incorrect input, please try again.')
        move_input_o()
    elif num[int(move)] == move:
        num[int(move)] = 'O'
    else:
        print('Incorrect input, please try again.')
        move_input_o()

def check_if_over():
    player = ['X', 'O']
    for x_o in player:
        if num[0] == x_o and num[1] == x_o and num[2] == x_o:
            printBoard()
            print('Congratulations! ' + x_o + ' won the game.')
            return True
        elif num[3] == x_o and num[4] == x_o and num[5] == x_o:
            printBoard()
            print('Congratulations! ' + x_o + ' won the game.')
            return True
        elif num[6] == x_o and num[7] == x_o and num[8] == x_o:
            printBoard()
            print('Congratulations! ' + x_o + ' won the game.')
            return True
        elif num[0] == x_o and num[3] == x_o and num[6] == x_o:
            printBoard()
            print('Congratulations! ' + x_o + ' won the game.')
            return True
        elif num[1] == x_o and num[4] == x_o and num[7] == x_o:
            printBoard()
            print('Congratulations! ' + x_o + ' won the game.')
            return True
        elif num[2] == x_o and num[5] == x_o and num[8] == x_o:
            printBoard()
            print('Congratulations! ' + x_o + ' won the game.')
            return True
        elif num[0] == x_o and num[4] == x_o and num[8] == x_o:
            printBoard()
            print('Congratulations! ' + x_o + ' won the game.')
            return True
        elif num[2] == x_o and num[4] == x_o and num[6] == x_o:
            printBoard()
            print('Congratulations! ' + x_o + ' won the game.')
            return True
    if num[0] != '0' and num[1] != '1' and num[2] != '2' and num[3] != '3' and num[4] != '4' \
         and num[5] != '5' and num[6] != '6' and num[7] != '7' and num[8] != '8':
        printBoard()
        print('The game is a tie!')
        return True
    else:
        return False

check = False

while (check == False):
    printBoard()
    move_input_x()
    check = check_if_over()
    if check == False:
        printBoard()
        move_input_o()
        check = check_if_over()