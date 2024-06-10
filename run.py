# Board cell values
cells = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

# Current player variable
current_player = "X"


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
    while True:
        render_board()
        update_board()          
    

main()