from asyncio.windows_events import NULL
from random import randrange


board = ["-", "-", "-",
         "-", "-", "-", 
         "-", "-", "-"]

def display():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play():

    display()

    check_win = False
    check_tie = False

    while (not check_win and not check_tie):

        take_turn()

        if check_winner():
            check_win = True
            print("The game has ended in a win!")

        if check_tier():
            check_tie = True
            print("The game has ended in a tie!")

        cpu_turn()

        if check_winner():
            check_win = True
            print("The game has ended in a win!")

        if check_tier():
            check_tie = True
            print("The game has ended in a tie!")


def take_turn():

    str_position = input("The board is labeled left to right 1-9. Choose a number for your next move: ")
    int_position = int(str_position) - 1

    if board[int_position] != "-":
        while board[int_position] != "-":
            str_position = input("That position has been filled. Please select another number 1-9: ")
            int_position = int(str_position) - 1

    board[int_position] = "X"
    display()

def cpu_turn():
    index = cpu_analyze_board()
    board[index] = "O"
    print("CPU turn: ")
    display()
    # pos = randrange(9)

    # if board[pos] == "-":
    #     board[pos] = "O"
    #     print("CPU turn: ")
    #     display()
    # else:
    #     while board[pos] != "-":
    #         pos = randrange(9)
    #     board[pos] = "O"
    #     print("CPU turn: ")
    #     display()

def cpu_analyze_board():
    # first check if there's any 2-in-a-row Os to complete a win
    if board[0] == "O" and board[1] == "O" and board[2] == "-":
        return 2

    if board[1] == "O" and board[2] == "O" and board[0] == "-":
        return 0

    if board[0] == "O" and board[2] == "O" and board[1] == "-":
        return 1

    if board[3] == "O" and board[4] == "O" and board[5] == "-":
        return 5

    if board[4] == "O" and board[5] == "O" and board[3] == "-":
        return 3

    if board[3] == "O" and board[5] == "O" and board[4] == "-":
        return 4

    if board[6] == "O" and board[7] == "O" and board[8] == "-":
        return 8

    if board[6] == "O" and board[8] == "O" and board[7] == "-":
        return 7

    if board[7] == "O" and board[8] == "O" and board[6] == "-":
        return 6

    # cols of 2
    if board[0] == "O" and board[3] == "O" and board[6] == "-":
        return 6

    if board[0] == "O" and board[6] == "O" and board[3] == "-":
        return 3

    if board[3] == "O" and board[6] == "O" and board[0] == "-":
        return 0

    if board[1] == "O" and board[4] == "O" and board[7] == "-":
        return 7

    if board[1] == "O" and board[7] == "O" and board[4] == "-":
        return 4

    if board[4] == "O" and board[7] == "O" and board[1] == "-":
        return 1

    if board[2] == "O" and board[5] == "O" and board[8] == "-":
        return 8

    if board[2] == "O" and board[8] == "O" and board[5] == "-":
        return 5

    if board[5] == "O" and board[8] == "O" and board[2] == "-":
        return 2

    # diagonals of 2
    if board[0] == "O" and board[4] == "O" and board[8] == "-":
        return 8
    
    if board[0] == "O" and board[8] == "O" and board[4] == "-":
        return 4

    if board[4] == "O" and board[8] == "O" and board[0] == "-":
        return 0

    if board[2] == "O" and board[4] == "O" and board[6] == "-":
        return 6

    if board[2] == "O" and board[6] == "O" and board[4] == "-":
        return 4

    if board[4] == "O" and board[6] == "O" and board[2] == "-":
        return 2


    # then check if there's any 2-in-a-row Xs to prevent winning
    # rows of 2
    if board[0] == "X" and board[1] == "X" and board[2] == "-":
        return 2

    if board[1] == "X" and board[2] == "X" and board[0] == "-":
        return 0

    if board[0] == "X" and board[2] == "X" and board[1] == "-":
        return 1

    if board[3] == "X" and board[4] == "X" and board[5] == "-":
        return 5

    if board[4] == "X" and board[5] == "X" and board[3] == "-":
        return 3

    if board[3] == "X" and board[5] == "X" and board[4] == "-":
        return 4

    if board[6] == "X" and board[7] == "X" and board[8] == "-":
        return 8

    if board[6] == "X" and board[8] == "X" and board[7] == "-":
        return 7

    if board[7] == "X" and board[8] == "X" and board[6] == "-":
        return 6

    # cols of 2
    if board[0] == "X" and board[3] == "X" and board[6] == "-":
        return 6

    if board[0] == "X" and board[6] == "X" and board[3] == "-":
        return 3

    if board[3] == "X" and board[6] == "X" and board[0] == "-":
        return 0

    if board[1] == "X" and board[4] == "X" and board[7] == "-":
        return 7

    if board[1] == "X" and board[7] == "X" and board[4] == "-":
        return 4

    if board[4] == "X" and board[7] == "X" and board[1] == "-":
        return 1

    if board[2] == "X" and board[5] == "X" and board[8] == "-":
        return 8

    if board[2] == "X" and board[8] == "X" and board[5] == "-":
        return 5

    if board[5] == "X" and board[8] == "X" and board[2] == "-":
        return 2

    # diagonals of 2
    if board[0] == "X" and board[4] == "X" and board[8] == "-":
        return 8
    
    if board[0] == "X" and board[8] == "X" and board[4] == "-":
        return 4

    if board[4] == "X" and board[8] == "X" and board[0] == "-":
        return 0

    if board[2] == "X" and board[4] == "X" and board[6] == "-":
        return 6

    if board[2] == "X" and board[6] == "X" and board[4] == "-":
        return 4

    if board[4] == "X" and board[6] == "X" and board[2] == "-":
        return 2
    



    # return index of the best position of board for CPU to fill
    scores = [0, 0, 0,
              0, 0, 0,
              0, 0, 0]
    
    # make score -1 for already filled board positions
    for i, v in enumerate(board):
        if v == "X" or v == "O":
            scores[i] = -1
    
    for i, v in enumerate(scores):
        if v != -1:
            if (i % 3 != 0 and i >= 1 and scores[i - 1] != NULL and scores[i - 1] == "X"):
                scores[i] += 10

            if (i % 3 != 2 and i <= 7 and scores[i + 1] != NULL and scores[i + 1] == "X"):
                scores[i] += 10

            if (i <= 5 and scores[i + 3] != NULL and scores[i + 3] == "X"):
                scores[i] += 10

            if (i >= 3 and scores[i - 3] != NULL and scores[i - 3] == "X"):
                scores[i] += 10
    
    return scores.index(max(scores))




def check_winner():
    rows = check_rows()
    cols = check_cols()
    diags = check_diags()

    if (rows or cols or diags):
        return True
    else:
        return False

def check_rows():
    num_x = 0
    num_o = 0
    index = 0
    
    while index <= 9:
        if index % 3 == 0:
            if num_x == 3 or num_o == 3:
                return True
            if index == 9:
                return False
            num_x = 0
            num_o = 0

        if board[index] == "X":
            num_x += 1
        elif board[index] == "O":
            num_o += 1

        index += 1
    
    return False
        


def check_cols():
    if ((board[0] == "X" and board[3] == "X" and board[6] == "X") or (board[0] == "O" and board[3] == "O" and board[6] == "O")):
        return True

    if ((board[1] == "X" and board[4] == "X" and board[7] == "X") or (board[1] == "O" and board[4] == "O" and board[7] == "O")):
        return True

    if ((board[2] == "X" and board[5] == "X" and board[8] == "X") or (board[2] == "O" and board[5] == "O" and board[8] == "O")):
        return True

    return False

def check_diags():
    if ((board[0] == "X" and board[4] == "X" and board[8] == "X") or (board[0] == "O" and board[4] == "O" and board[8] == "O")):
        return True

    if ((board[2] == "X" and board[4] == "X" and board[6] == "X") or (board[2] == "O" and board[4] == "O" and board[6] == "O")):
        return True

    return False


def check_tier():
    if "-" not in board and not check_winner():
        return True
    else:
        return False


play()

