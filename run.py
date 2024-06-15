# Board cell values
cells = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

# Current player variable
current_player = "X"

# Game winning combinations
COMBOS = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [7, 5, 3],
]

def game_instructions():
    """
    Display the game instructions to the user.
    """
    print("        TIC-TAC-TOE INSTRUCTIONS\n")
    print("    1: Take turns marking an empty cell!")
    print("    2: Get 3 marks in a row to win!(up/down, across, or diagonal)")
    print("    3: A legend is provided to help you make your moves!")
    print("    4: When all the cells are full the game is over!")
    print("    5: If no player has 3 in a row, the game ends in a tie!\n")


def render_legend():
    """
    Display a legend showing the cell reference numbers.
    """
    print("    1|2|3")
    print("    4|5|6")
    print("    7|8|9")


def render_board():
    """
    Display the game board to the user.
    """
    print(f"               {cells[1]} | {cells[2]} | {cells[3]}")
    print(f"              ---|---|---")
    print(f"               {cells[4]} | {cells[5]} | {cells[6]}")
    print(f"              ---|---|---")
    print(f"               {cells[7]} | {cells[8]} | {cells[9]}\n")


def update_board():
    """
    Update the game board with a valid input.
    """
    try:
        choice = int(input(f"    {current_player} Make your move! (1-9): "))
        if cells[choice] == " ":
            cells[choice] = current_player
            check_winner()
            check_tie()
            change_player()                                                
        else:
            print("  ## This cell is taken, please choose and EMPTY cell! ##")
        if choice < 1:
            raise IndexError(" ## Please enter a number between 1-9! ##")
    except IndexError:
        print("  ## Please only enter a number between 1-9! ##")
    except ValueError:
        print("  ## Please enter a NUMBER between 1-9! ##")
    else:
        pass    


def check_winner():
    """
    Check to see if any of the winning combinations have been met.
    """
    for i in range(len(COMBOS)):        
        CONDITION = COMBOS[i]            
        CELL_A = cells[CONDITION[0]]
        CELL_B = cells[CONDITION[1]]
        CELL_C = cells[CONDITION[2]]
        if CELL_A == " " or CELL_B == " " or CELL_C == " ":
            continue
        if CELL_A == CELL_B and CELL_B == CELL_C:
            render_board()
            print(f"\n               {current_player} WON THIS ROUND!!!\n")


def check_tie():
    """
    Check to see if all the cells are full
    and if so the game will end in a tie.
    """
    board_full = True
    for i in range(len(cells)):
        if cells[i] == " ":
            board_full = False
            break

    if board_full == True:
        render_board()
        print("\n        THIS ROUND IS A TIE!!!\n")            




def change_player():
    """
    Find the current player marker and change it to its counter part.
    """
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"                


def main():
    """
    Run the game functions.
    """
    game_instructions()
    while True:
        render_legend()
        render_board()
        update_board()          
    

main()