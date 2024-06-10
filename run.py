# Board cell values
cells = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

# Current player variable
current_player = "X"

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
        choice = int(input("    Please enter an empty cell number: "))
        if cells[choice] == " ":
            cells[choice] = current_player                                                
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