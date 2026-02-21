import random
from colorama import init, Fore, Style
init(autoreset=True)
# =========================================
# CONSTANTS (DO NOT EDIT)
# =========================================
win_conditions = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def display_board(board):
    """Prints the Tic-Tac-Toe board in color."""
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL

    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '---+---+---' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()

def player_choice():
    """Asks player to choose X or O and returns (player_symbol, ai_symbol)."""
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).strip().upper()
    return ('X', 'O') if symbol == 'X' else ('O', 'X')

# ==========================================================
# TODO 1: player_move(board, symbol)
# ==========================================================
def player_move(board, symbol):
    Move = input(Fore.GREEN + "Enter a number (1-9) to place your symbol: " + Style.RESET_ALL).strip()
    Move = int(Move) - 1  # Convert to 0-based index
    if 0 <= Move <= 8 and board[Move].isdigit():
        print(f"Moved to location {Move + 1}")
        board[Move] = symbol


# ==========================================================
# TODO 2: ai_move(board, ai_symbol, player_symbol)
# ==========================================================
def ai_move(board, ai_symbol, player_symbol):
    # TODO A: Try to win in 1 move
    if check_full(board):
        return
    else: 
        for i in range(9):
            if board[i].isdigit():
                boardcopy = board.copy()
                boardcopy[i] = ai_symbol
                if check_win(boardcopy, player_symbol):
                    board[i] = ai_symbol
                    print(f"AI places at location {i + 1}")
                    return
        # TODO B: Try to block player win in 1 move
        for i in range(9):
            if board[i].isdigit():
                boardcopy = board.copy()
                boardcopy[i] = player_symbol
                if check_win(boardcopy, player_symbol):
                    board[i] = ai_symbol
                    print(f"AI places at location {i + 1}")
                    return
        
        possiblemoves = [i for i in range(9) if board[i].isdigit()]

        move = random.choice(possiblemoves)
        board[move] = ai_symbol
        print(f"AI places at location {move + 1}")

    # TODO C: Else, pick a random empty spot

# ==========================================================
# TODO 3: check_win(board, symbol)
# ==========================================================
def check_win(board, symbol):
    win_conditions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for c in win_conditions:
        if all(board[i] == symbol for i in c):
            return True
    return False

# ==========================================================
# TODO 4: check_full(board)
# ==========================================================
def check_full(board):
    if all(board[i].isdigit() for i in range(9)):
        return True
    else:
        return False
            

# ==========================================================
# MAIN GAME (NOW WITH A FEW TODOs)
# ==========================================================
def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")

    # TODO (MAIN-1): Ask player's name in green and store it
    # Hint: if empty, default to "Player"
    name = input(Fore.GREEN + "Enter your name (or press Enter to use 'Player'): " + Style.RESET_ALL)
    if not name:
        name = "Player"

    while True:
        # TODO (MAIN-2): Initialize the board as ["1","2",...,"9"]
        board = ["1","2","3","4","5","6","7","8","9"]  # replace this line

        # TODO (MAIN-3): Get symbols using player_choice()
        player_symbol, ai_symbol = player_choice()

        # TODO (MAIN-4): Decide who starts ("Player" or "AI")
        # Simple option: always start with Player
        turn = "Player"  # replace this line

        while True:
            display_board(board)

            if turn == "Player":
                # TODO (MAIN-5): Call player_move() to place player's symbol
                player_move(board, player_symbol)

                # TODO (MAIN-6): If player wins, print win message with name and break
                if check_win(board, player_symbol):
                    print(Fore.GREEN + f"Congratulations {name}! You win!" + Style.RESET_ALL)
                    break

                # TODO (MAIN-7): If tie (board full), print tie message and break
                if check_full(board):
                    print(Fore.YELLOW + "It's a tie!" + Style.RESET_ALL)
                    break

                # TODO (MAIN-8): Switch turn to "AI"
                turn = "AI"

            else:
                # TODO (MAIN-9): Call ai_move() to place AI symbol
                ai_move(board, ai_symbol, player_symbol)

                # TODO (MAIN-10): If AI wins, print AI win message and break
                if check_win(board, ai_symbol):
                    print(Fore.RED + f"AI wins!" + Style.RESET_ALL)
                    break

                # TODO (MAIN-11): If tie (board full), print tie message and break
                if check_full(board):
                    print(Fore.YELLOW + "It's a tie!" + Style.RESET_ALL)
                    break

                # TODO (MAIN-12): Switch turn to "Player"
                turn = "Player"

        # TODO (MAIN-13): Ask "Play again? (yes/no): "
        # If answer is NOT "yes", print thank you and return
        again = input(Fore.CYAN + "Play again? (yes/no): " + Style.RESET_ALL).lower()
        if again != "yes":
            print(Fore.GREEN + "Thanks for playing!" + Style.RESET_ALL)
            return

if __name__ == "__main__":
    tic_tac_toe()
