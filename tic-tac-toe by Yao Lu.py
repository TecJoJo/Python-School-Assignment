player0_char = 'X'
player1_char = 'O'
gameRunning = True


def printGameboard():
    print(gameboard['A'])
    print(gameboard['B'])
    print(gameboard['C'])


def setUserPointTo(alpha, number, player):
    if player:
        player_char = player0_char
    else:
        player_char = player1_char
    gameboard[alpha][number] = player_char


def end_game(alpha, number, game_progress, player):
    if game_progress[alpha][0] + game_progress[alpha][1] + game_progress[alpha][2] == 3 \
            or game_progress['A'][number] + game_progress['B'][number] + game_progress['C'][number] \
            == 3:
        print(f'{player} won the game')
        return True

    if game_progress['A'][0] + game_progress['B'][1] + game_progress['C'][2] == 3 \
            or game_progress['A'][2] + game_progress['B'][1] + game_progress['C'][0] == 3:
        print(f'{player} won the game')
        return True

    index = 0
    for place in gameboard:
        for element in gameboard[place]:
            if element != " ":
                index += 1
    if index == 9:
        print('it is a draw game')
        return True


                  # 0    1    2
gameboard = {'A': [" ", " ", " "],
             'B': [" ", " ", " "],
             'C': [" ", " ", " "]}

game_progress_player0 = {'A':[0,0,0],
                         'B':[0,0,0],
                         'C':[0,0,0]}
game_progress_player1 = {'A':[0,0,0],
                         'B':[0,0,0],
                         'C':[0,0,0]}

player0_parameter = True
player1_parameter = False

while gameRunning:
    alpha0 = input("player0's turn, please input the coordinate alphabet, from A to C").upper()
    number0 = int(input("player0's turn, please input the coordinate number, from 0 to 2"))

    while True:
        if gameboard[alpha0][number0] != " ":  # why here start infinite loop
            alpha0 = input(
                "player0's turn, place is already taken, please input the coordinate alphabet, from A to C").upper()
            number0 = int(
                input("player0's turn, place is already taken, please input the coordinate number, from 0 to 2"))
        else:
            break


    game_progress_player0[alpha0][number0] += 1
    setUserPointTo(alpha0, number0, player0_parameter)

    printGameboard()
    if end_game(alpha0,number0,game_progress_player0,'player0'):
        break

    alpha1 = input("player1's turn, please input the coordinate alphabet, from A to C").upper()
    number1 = int(input("player1's turn, please input the coordinate number, from 0 to 2"))

    while True:
        if gameboard[alpha1][number1] != " ":
            alpha1 = input(
                "player1's turn, place is already taken, please input the coordinate alphabet, from A to C").upper()
            number1 = int(
                input("player1's turn, place is already taken, please input the coordinate number, from 0 to 2"))
        else:
            break

    game_progress_player1[alpha1][number1] += 1
    setUserPointTo(alpha1, number1, player1_parameter)

    printGameboard()
    if end_game(alpha1,number1,game_progress_player1,'player1'):
        break
