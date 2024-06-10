# Board cell values
cells = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def render_board():
    """
    Display the game board to the user.
    """
    print(f"               {cells[1]} | {cells[2]} | {cells[3]}")
    print(f"              ---|---|---")
    print(f"               {cells[4]} | {cells[5]} | {cells[6]}")
    print(f"              ---|---|---")
    print(f"               {cells[7]} | {cells[8]} | {cells[9]}\n")


def main():
    """
    Run the game functions.
    """
    render_board()          
    

main()