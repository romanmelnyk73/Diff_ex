# A classic game of tic-tac-toe with a bot
#
from random import randint
list_field = []
list_win_options = ['012', '345', '678', '036', '147', '258', '048', '246']
move = input('What are you going to play by: \n 1 - X ; 2 - 0\n')
if move == '1':
   var1 = True
else:
    var1 = False
for i in range(9):
    list_field.append(0)
isX = True
Game = True
while Game:
    # SHOW FIELD
    for i in range(len(list_field)):
        if list_field[i] == 0:
            print('-', end='  ')
        elif list_field[i] == 1:
            print('X', end='  ')
        elif list_field[i] == 2:
            print('O', end='  ')
        if i == 2 or i == 5:
            print()
    print('\n___________________')
    # USER's MOVE
    if 0 not in list_field:
        print('*REMISE*')
        break
    if var1:
        if isX:
            user_choice = int(input('\n*******\nEnter your choice: '))
        if not isX:
            user_choice = randint(1,9)
    if not var1:
        if isX:
            user_choice = randint(1, 9)
        if not isX:
            user_choice = int(input('\n*******\nEnter your choice: '))
    if 1 <= user_choice <= 9 and list_field[user_choice - 1] == 0:
        if isX:
            list_field[user_choice - 1] = 1
            isX = False
        else:
            list_field[user_choice - 1] = 2
            isX = True
        for i in range(len(list_win_options)):
            text = list_win_options[i]
            if list_field[int(text[0])] == list_field[int(text[1])] and list_field[int(text[1])] == list_field[int(text[2])] and list_field[int(text[2])] != 0:
                if list_field[int(text[0])] == 1:
                    print('*WIN X*')
                    Game = False
                else:
                    print('*WIN O*')
                    Game = False
                for i in range(len(list_field)):
                    if list_field[i] == 0:
                        print('-', end='  ')
                    elif list_field[i] == 1:
                        print('X', end='  ')
                    elif list_field[i] == 2:
                        print('O', end='  ')
                    if i == 2 or i == 5:
                        print()
                break
    else:
        print('\n\tThis field already used\n')
