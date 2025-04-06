"""
    Spacestation Game"""
# Importing packages
import random
import os

# Global variables
# Number of rows and columns
N = 5
# Number of traps
TRAPS_NO = 5
# The actual values of the grid
NUMBERS = [[0 for _ in range(N)] for _ in range(N)]
# The apparent values of the grid
TRAP_VALUES = [[' ' for _ in range(N)] for _ in range(N)]
# The positions that have been flagged
FLAGS: list[list[int]] = []
# The Visited positions for zero-valued cells
VIS: list[list[int]] = []
# Printing the Spacestation Layout
def print_traps_layout() -> None:
    """
    Method to print the layout of the game.
    """
    print()
    print("\t\tSPACESTATION\n")
    st = "   "
    for i in range(N):
        st = st + "     " + str(i + 1)
    print(st)
    for r in range(N):
        st = "     "
        if r == 0:
            for col in range(N):
                st = st + "______"
            print(st)
        st = "     "
        for col in range(N):
            st = st + "|     "
        print(st + "|")
        st = "  " + str(r + 1) + "  "
        for col in range(N):
            st = st + "|  " + str(TRAP_VALUES[r][col]) + "  "
        print(st + "|")
        st = "     "
        for col in range(N):
            st = st + "|_____"
        print(st + '|')
    print()
# Function for setting up Traps
def set_traps() -> None:
    """
    Function for setting up traps in the grid.
    """
    # Track of number of traps already set up
    count = 0
    while count < TRAPS_NO:
         # Random number from all possible grid positions
        val = random.randint(0, N*N-1)
        # Generating row and column from the number
        r = val // N
        col = val % N
        # Place the trap, if it doesn't already have one
        if NUMBERS[r][col] != -1:
            count = count + 1
            NUMBERS[r][col] = -1
# Function for setting up the other grid values
def set_values() -> None:
    """
    Function for setting up the other grid values.
    """
    # Loop for counting each cell value
    for r in range(N):
        for col in range(N):
            # Skip, if it contains a trap
            if NUMBERS[r][col] == -1:
                continue
            # Check up
            if r > 0 and NUMBERS[r-1][col] == -1:
                NUMBERS[r][col] = NUMBERS[r][col] + 1
            # Check down
            if r < N-1  and NUMBERS[r+1][col] == -1:
                NUMBERS[r][col] = NUMBERS[r][col] + 1
            # Check left
            if col > 0 and NUMBERS[r][col-1] == -1:
                NUMBERS[r][col] = NUMBERS[r][col] + 1
            # Check right
            if col < N-1 and NUMBERS[r][col+1] == -1:
                NUMBERS[r][col] = NUMBERS[r][col] + 1
            # Check top-left
            if r > 0 and col > 0 and NUMBERS[r-1][col-1] == -1:
                NUMBERS[r][col] = NUMBERS[r][col] + 1
            # Check top-right
            if r > 0 and col < N-1 and NUMBERS[r-1][col+1] == -1:
                NUMBERS[r][col] = NUMBERS[r][col] + 1
            # Check below-left
            if r < N-1 and col > 0 and NUMBERS[r+1][col-1] == -1:
                NUMBERS[r][col] = NUMBERS[r][col] + 1
            # Check below-right
            if r < N-1 and col < N-1 and NUMBERS[r+1][col+1] == -1:
                NUMBERS[r][col] = NUMBERS[r][col] + 1
# Recursive function to display all zero-valued neighbours
def neighbours(r: int, col: int, vis: list[list[int]]) -> None:
    """
    Function to process neighbouring cells recursively.
    Updates the TRAP_VALUES grid and marks cells as Visited.
    """

    # If the cell already not Visited
    if [r,col] not in VIS:
        # Mark the cell Visited
        VIS.append([r, col])
        # If the cell is zero-valued
        if NUMBERS[r][col] == 0:
            # Display it to the user
            TRAP_VALUES[r][col] = str(NUMBERS[r][col])
            # Recursive calls for the neighbouring cells
            if r > 0:
                neighbours(r-1, col, vis)
            if r < N-1:
                neighbours(r+1, col, vis)
            if col > 0:
                neighbours(r, col-1, vis)
            if col < N-1:
                neighbours(r, col+1, vis)
        else:
            TRAP_VALUES[r][col] = str(NUMBERS[r][col])
        # If the cell is not zero-valued
        if NUMBERS[r][col] != 0:
            TRAP_VALUES[r][col] = str(NUMBERS[r][col])
# Function for clearing the terminal
def clear() -> None:
    """
    Function to clear the terminal screen.
    """
    os.system("clear")
# Function to display the instructions
def instructions() -> None:
    """
    Function to display the instructions for the game.
    """
    print("Instructions:")
    print("1. Enter row and column number to select a cell, Example \"2 3\"")
    print("2. In order to flag a trap, enter F after row and column NUMBERS, Example \"2 3 F\"")
# Function to check for completion of the game
def check_over() -> bool:
    """
    Function to check for completion of the game.
    """
    # Count of all numbered values
    count = 0
     # Loop for checking each cell in the grid
    for r in range(N):
        for col in range(N):
            # If cell not empty or flagged
            if TRAP_VALUES[r][col] != ' ' and TRAP_VALUES[r][col] != 'F':
                count = count + 1
    # Count comparison
    return bool(count == N * N - TRAPS_NO)
# Display all the trap locations
def show_traps() -> None:
    """
    Function to display all the trap locations.
    """

    for r in range(N):
        for col in range(N):
            if NUMBERS[r][col] == -1:
                TRAP_VALUES[r][col] = 'M'

def process_input(inp: list[str]) -> tuple[int, int] | None:
    """
    Process user input and validate it.
    Returns a tuple of row and column indices if valid, or None if invalid.
    """
    try:
        val = list(map(int, inp))
        if val[0] > N or val[0] < 1 or val[1] > N or val[1] < 1:
            clear()
            print("Wrong input!")
            instructions()
            return None
        return val[0] - 1, val[1] - 1
    except ValueError:
        clear()
        print("Wrong input!")
        instructions()
        return None

def handle_flag(val: tuple[int, int]) -> None:
    """
    Handle flagging logic for the game.
    """
    r, col = val
    if [r, col] in FLAGS:
        clear()
        print("Flag already set")
        return

    if TRAP_VALUES[r][col] != ' ':
        clear()
        print("Value already known")
        return

    if len(FLAGS) < TRAPS_NO:
        clear()
        print("Flag set")
        FLAGS.append([r, col])
        TRAP_VALUES[r][col] = 'F'
    else:
        clear()
        print("Flags finished")

def handle_cell_selection(val: tuple[int, int]) -> bool:
    """
    Handle cell selection logic for the game.
    Returns True if the game is over, False otherwise.
    """
    r, col = val

    if [r, col] in FLAGS:
        FLAGS.remove([r, col])

    if NUMBERS[r][col] == -1:
        TRAP_VALUES[r][col] = 'M'
        show_traps()
        print_traps_layout()
        print("Landed on a trap. GAME OVER!!!!!")
        return True

    if NUMBERS[r][col] == 0:
        vis: list[list[int]] = []
        TRAP_VALUES[r][col] = '0'
        neighbours(r, col, vis)
    else:
        TRAP_VALUES[r][col] = str(NUMBERS[r][col])

    if check_over():
        show_traps()
        print_traps_layout()
        print("Congratulations!!! YOU WIN")
        return True

    return False

def game_loop() -> None:
    """
    Main function to run the game loop.
    """
    set_traps()
    set_values()
    instructions()

    over = False

    while not over:
        print_traps_layout()

        inp = input("Enter row number followed by space and column number = ").split()

        if len(inp) == 2:
            result = process_input(inp)
            if result is None:
                continue
            over = handle_cell_selection(result)

        elif len(inp) == 3:
            if inp[2].lower() != 'f':
                clear()
                print("Wrong Input!")
                instructions()
                continue
            result = process_input(inp[:2])
            if result is None:
                continue
            handle_flag(result)

        else:
            clear()
            print("Wrong input!")
            instructions()
if __name__ == "__main__":
    game_loop()
