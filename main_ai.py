import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 600
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

# Load images
background = pygame.image.load('images/bg.jpg')
x_img = pygame.image.load('images/x.png')
o_img = pygame.image.load('images/o.png')
x_img = pygame.transform.scale(x_img, (100, 100))
o_img = pygame.transform.scale(o_img, (100, 100))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Board variables
board = [[None]*3, [None]*3, [None]*3]
boardx = [100, 250, 400]
boardy = [100, 250, 400]

current_player = "X"
winner = None
game_over = False

# Fonts
font = pygame.font.Font(None, 74)

def draw_board():
    screen.blit(background, (0, 0))

    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                screen.blit(x_img, (boardx[col], boardy[row]))
            elif board[row][col] == "O":
                screen.blit(o_img, (boardx[col], boardy[row]))

def check_winner():
    global winner, game_over
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            winner = row[0]
            game_over = True
            return

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            winner = board[0][col]
            game_over = True
            return

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        winner = board[0][0]
        game_over = True
        return
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        winner = board[0][2]
        game_over = True
        return

    # Check for a draw
    if all([all(row) for row in board]) and winner is None:
        winner = "Draw"
        game_over = True

def reset_game():
    global board, current_player, winner, game_over
    board = [[None]*3, [None]*3, [None]*3]
    current_player = "X"
    winner = None
    game_over = False

def is_moves_left(board):
    for row in board:
        if None in row:
            return True
    return False

def evaluate(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == 'O':
                return 10
            elif row[0] == 'X':
                return -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'O':
                return 10
            elif board[0][col] == 'X':
                return -10

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'O':
            return 10
        elif board[0][0] == 'X':
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'O':
            return 10
        elif board[0][2] == 'X':
            return -10

    return 0

def alpha_beta_pruning(board, depth, alpha, beta, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = 'O'
                    best = max(best, alpha_beta_pruning(board, depth + 1, alpha, beta, not is_max))
                    board[i][j] = None
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = 'X'
                    best = min(best, alpha_beta_pruning(board, depth + 1, alpha, beta, not is_max))
                    board[i][j] = None
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = 'O'
                move_val = alpha_beta_pruning(board, 0, -1000, 1000, False)
                board[i][j] = None
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // (height // 3)
            clicked_col = mouseX // (width // 3)
            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = current_player
                check_winner()
                if not game_over:
                    current_player = "O" if current_player == "X" else "X"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

    if current_player == "O" and not game_over:
        move = find_best_move(board)
        if move != (-1, -1):
            board[move[0]][move[1]] = current_player
            check_winner()
            if not game_over:
                current_player = "X"

    draw_board()

    if game_over:
        end_text = font.render(f"{winner} wins!" if winner != "Draw" else "It's a draw!", True, black)
        screen.blit(end_text, (width // 2 - end_text.get_width() // 2, height // 2 - end_text.get_height() // 2))

    pygame.display.flip()
