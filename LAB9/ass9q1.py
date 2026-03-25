import time
import random

# Global counters for performance evaluation
minimax_nodes = 0
alphabeta_nodes = 0

def check_winner(board):
    """Returns 1 if X wins, -1 if O wins, 0 for draw, None if ongoing."""
    win_lines = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for a, b, c in win_lines:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return 1 if board[a] == 'X' else -1
    if ' ' not in board: return 0
    return None

# Min-Max Implementation 
def minimax(board, is_maximizing):
    global minimax_nodes
    minimax_nodes += 1
    
    score = check_winner(board)
    if score is not None: return score

    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best_score = max(best_score, minimax(board, False))
                board[i] = ' '
        return best_score
    else:
        best_score = 1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best_score = min(best_score, minimax(board, True))
                board[i] = ' '
        return best_score

# Alpha-Beta Pruning Implementation 
def alpha_beta(board, alpha, beta, is_maximizing):
    global alphabeta_nodes
    alphabeta_nodes += 1
    
    score = check_winner(board)
    if score is not None: return score

    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best_score = max(best_score, alpha_beta(board, alpha, beta, False))
                board[i] = ' '
                alpha = max(alpha, best_score)
                if beta <= alpha: break # Beta cutoff
        return best_score
    else:
        best_score = 1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best_score = min(best_score, alpha_beta(board, alpha, beta, True))
                board[i] = ' '
                beta = min(beta, best_score)
                if beta <= alpha: break # Alpha cutoff
        return best_score

# --- Helper to generate varied game trees ---
def get_random_start(moves=4):
    board = [' '] * 9
    players = ['X', 'O']
    for i in range(moves):
        empty = [j for j in range(9) if board[j] == ' ']
        board[random.choice(empty)] = players[i % 2]
    # Ensure the random board isn't already finished
    if check_winner(board) is not None:
        return get_random_start(moves)
    return board

# Main Execution
if __name__ == "__main__":
    # Generate a random board with 4 moves already played
    current_board = get_random_start(4)
    
    print("Evaluating Varied Game Tree Start State:")
    print(f" {current_board[0]} | {current_board[1]} | {current_board[2]} ")
    print("---+---+---")
    print(f" {current_board[3]} | {current_board[4]} | {current_board[5]} ")
    print("---+---+---")
    print(f" {current_board[6]} | {current_board[7]} | {current_board[8]} \n")

    # 1. Evaluate pure Min-Max
    start_time = time.time()
    best_move_mm = -1
    best_score_mm = -1000
    for i in range(9):
        if current_board[i] == ' ':
            current_board[i] = 'X'
            score = minimax(current_board, False)
            current_board[i] = ' '
            if score > best_score_mm:
                best_score_mm = score
                best_move_mm = i
    mm_time = time.time() - start_time

    # 2. Evaluate Alpha-Beta
    start_time = time.time()
    best_move_ab = -1
    best_score_ab = -1000
    for i in range(9):
        if current_board[i] == ' ':
            current_board[i] = 'X'
            score = alpha_beta(current_board, -1000, 1000, False)
            current_board[i] = ' '
            if score > best_score_ab:
                best_score_ab = score
                best_move_ab = i
    ab_time = time.time() - start_time

    print("--- Q1: Min-Max Algorithm ---")
    print(f"Best Move: Index {best_move_mm}")
    print(f"Nodes Evaluated: {minimax_nodes}")
    print(f"Time Taken: {mm_time:.5f} sec\n")

    print("--- Q2: Alpha-Beta Pruning ---")
    print(f"Best Move: Index {best_move_ab}")
    print(f"Nodes Evaluated: {alphabeta_nodes}")
    print(f"Time Taken: {ab_time:.5f} sec")