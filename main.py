import math
import random


def print_board(board):
    for i in range(3):
        for j in range(3):
            cell = board[i * 3 + j]
            print("X" if cell == 1 else "O" if cell == 2 else "-", sep=" ")
        print()


def check_winning_condition(board):
    temp = board.copy()
    temp.sort()
    # 0 = not_over, 1 = x win, 2 = o win, 3 = tie
    if board[0] == board[1] == board[2] != 0:
        return board[0]
    elif board[3] == board[4] == board[5] != 0:
        return board[3]
    elif board[6] == board[7] == board[8] != 0:
        return board[6]
    elif board[6] == board[3] == board[0] != 0:
        return board[6]
    elif board[7] == board[4] == board[1] != 0:
        return board[7]
    elif board[8] == board[5] == board[2] != 0:
        return board[8]
    elif board[0] == board[4] == board[8] != 0:
        return board[0]
    elif board[6] == board[4] == board[2] != 0:
        return board[6]
    elif temp[0] != 0:
        return 3
    else:
        return 0


def random_move(board):
    move = random.randint(0, 8)
    while board[move] != 0:
        move = random.randint(0, 8)
    return move


def smart_move(board: list, turn: int):
    best_score = -math.inf
    best_move = None
    empty_cells_index = []
    for i in range(len(board)):
        if board[i] == 0:
            empty_cells_index.append(i)

    for idx in empty_cells_index:
        board[idx] = turn
        score = minimax(turn, True, board)
        board[idx] = 0
        if score > best_score:
            best_score = score
            best_move = idx
    return best_move


def minimax(turn, is_max_turn: bool, board: list):
    state = check_winning_condition(board)
    if state == 3:
        return 0
    elif state == 1 or state == 2:
        return 1 if state == turn else -1

    empty_cells_index = []
    for i in range(len(board)):
        if board[i] == 0:
            empty_cells_index.append(i)

    scores = []
    for idx in empty_cells_index:
        board[idx] = turn
        scores.append(minimax(change_turn(turn), not is_max_turn, board))
        board[idx] = 0

    return max(scores) if is_max_turn else min(scores)


def tic_tac_toe(option):
    # option 1 = random move, option 2 = smart move
    # 1 = x, 2 = O
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    game_over = False

    while not game_over:
        if option == 1:
            move = random_move(board)
        else:
            move = smart_move(board, turn)

        board[move] = turn
        turn = change_turn(turn)

        if board.count(1) + board.count(2) >= 5:
            game_result = check_winning_condition(board)

            if game_result != 0:
                return game_result


def change_turn(turn):
    if turn == 1:
        turn += 1
    else:
        turn -= 1
    return turn


if __name__ == '__main__':
    x_win = 0
    o_win = 0
    tie = 0
    no_of_round = 1000000
    for i in range(no_of_round):
        result = tic_tac_toe(1)
        if result == 1:
            x_win += 1
        elif result == 2:
            o_win += 1
        else:
            tie += 1

    print(f"From {no_of_round} rounds, x wins {x_win} rounds ({(x_win / no_of_round * 100):.2f}%).")
    print(f"From {no_of_round} rounds, o wins {o_win} rounds ({(o_win / no_of_round * 100):.2f}%).")
    print(f"From {no_of_round} rounds, tie happens {tie} rounds ({(tie / no_of_round * 100):.2f}%).")
