"""
    This is a command line tic-tac-toe game, a simple beginner level project
    Used os module for cleaning the display in every new game
    OS is a optional module. It can be ignored
"""
import os


# creating the board of the game
def board(v):
    print("""
            |       |
        {}   |   {}   |   {}
    ________|_______|________
            |       |
        {}   |   {}   |   {}
    ________|_______|________
            |       |
        {}   |   {}   |   {}
            |       |
    """.format(v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[8], v[9]))


# check for any three point matches. Matches are :
#               1 - 2 - 3
#               1 - 5 - 9
#               1 - 4 - 7
#               2 - 5 - 8
#               3 - 6 - 9
#               3 - 5 - 7
#               7 - 8 - 9

def check(values):
    if values[1] != ' ' and values[1] == values[2] and values[2] == values[3]:
        return values[1]
    elif values[1] != ' ' and values[1] == values[5] and values[5] == values[9]:
        return values[1]
    elif values[1] != ' ' and values[1] == values[4] and values[4] == values[7]:
        return values[1]
    elif values[2] != ' ' and values[2] == values[5] and values[5] == values[8]:
        return values[2]
    elif values[3] != ' ' and values[3] == values[6] and values[6] == values[9]:
        return values[3]
    elif values[3] != ' ' and values[3] == values[5] and values[5] == values[7]:
        return values[3]
    elif values[4] != ' ' and values[4] == values[5] and values[5] == values[6]:
        return values[4]
    elif values[7] != ' ' and values[7] == values[8] and values[8] == values[9]:
        return values[7]
    else:
        return - 1


def game():
    values = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    count = 0

    while count < 9:
        board(values)

        if count % 2 == 0:
            try:
                player1 = input("Player1 : ")
                if player1 == 'exit':
                    break
                player1 = int(player1)
                if 0 <= player1 <= 9:
                    if values[player1] == ' ':
                        values[player1] = '0'
                    else:
                        print('Place already occupied. select another')
                        continue
                else:
                    print("select a place between 1-9")
                    continue
            except:
                print("invalid move")
                continue
        else:
            try:
                player2 = input("Player2 : ")
                if player2 == 'exit':
                    break
                player2 = int(player2)
                if 0 <= player2 <= 9:
                    if values[player2] == ' ':
                        values[player2] = 'X'
                    else:
                        print('Place already occupied. select another')
                        continue
                else:
                    print("select a place between 1-9")
                    continue
            except:
                print('invalid move')
                continue
        c = check(values)
        if c != -1:
            board(values)
            if c == '0':
                print("Player1 is winner")
            else:
                print("Player2 is winner")
            break

        count += 1
        if count == 9:
            print("Match drawn\n")
    again = input("Play again ? [y/any] : ").lower()
    if again == 'y':
        return True
    else:
        return False


while True:
    g = game()
    if g:
        os.system('clear')
        continue
    else:
        break
