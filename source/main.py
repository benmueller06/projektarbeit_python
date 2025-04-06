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
NUMBERS = [[0 for _ in range(n)] for _ in range(n)]
# The apparent values of the grid
TRAP_VALUES = [[' ' for _ in range(n)] for _ in range(n)]
# The positions that have been flagged
FLAGS: list[list[int]] = []
# The visited positions for zero-valued cells
VIS: list[list[int]] = []
# Printing the Spacestation Layout
def print_traps_layout() -> None:
    """
    Method to print the layout of the game.
    """
    global trap_values
    global n
    print()
    print("\t\tSPACESTATION\n")
    st = "   "
    for i in range(n):
        st = st + "     " + str(i + 1)
    print(st)
    for r in range(n):
        st = "     "
        if r == 0:
            for col in range(n):
                st = st + "______"
            print(st)
        st = "     "
        for col in range(n):
            st = st + "|     "
        print(st + "|")
        st = "  " + str(r + 1) + "  "
        for col in range(n):
            st = st + "|  " + str(trap_values[r][col]) + "  "
        print(st + "|")
        st = "     "
        for col in range(n):
            st = st + "|_____"
        print(st + '|')
    print()
# Function for setting up Traps
def set_traps() -> None:
    """
    Function for setting up traps in the grid.
    """
    global numbers
    global traps_no
    global n
    # Track of number of traps already set up
    count = 0
    while count < traps_no:
         # Random number from all possible grid positions
        val = random.randint(0, n*n-1)
        # Generating row and column from the number
        r = val // n
        col = val % n
        # Place the trap, if it doesn't already have one
        if numbers[r][col] != -1:
            count = count + 1
            numbers[r][col] = -1
# Function for setting up the other grid values
def set_values() -> None:
    """
    Function for setting up the other grid values.
    """
    global numbers
    global n
    # Loop for counting each cell value
    for r in range(n):
        for col in range(n):
            # Skip, if it contains a trap
            if numbers[r][col] == -1:
                continue
            # Check up
            if r > 0 and numbers[r-1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check down
            if r < n-1  and numbers[r+1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check left
            if col > 0 and numbers[r][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check right
            if col < n-1 and numbers[r][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check top-left
            if r > 0 and col > 0 and numbers[r-1][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check top-right
            if r > 0 and col < n-1 and numbers[r-1][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check below-left
            if r < n-1 and col > 0 and numbers[r+1][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # Check below-right
            if r < n-1 and col < n-1 and numbers[r+1][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1
# Recursive function to display all zero-valued neighbours
def neighbours(r: int, col: int) -> None:
    """
    Function to process neighbouring cells recursively.
    Updates the trap_values grid and marks cells as visited.
    """
    global trap_values
    global numbers
    global vis

    # If the cell already not visited
    if [r,col] not in vis:
        # Mark the cell visited
        vis.append([r, col])
        # If the cell is zero-valued
        if numbers[r][col] == 0:
            # Display it to the user
            trap_values[r][col] = str(numbers[r][col])
            # Recursive calls for the neighbouring cells
            if r > 0:
                neighbours(r-1, col)
            if r < n-1:
                neighbours(r+1, col)
            if col > 0:
                neighbours(r, col-1)
            if col < n-1:
                neighbours(r, col+1)
            if r > 0 and col > 0:
                neighbours(r-1, col-1)
            if r > 0 and col < n-1:
                neighbours(r-1, col+1)
            if r < n-1 and col > 0:
                neighbours(r+1, col-1)
            if r < n-1 and col < n-1:
                neighbours(r+1, col+1)
        # If the cell is not zero-valued
        if numbers[r][col] != 0:
            trap_values[r][col] = str(numbers[r][col])
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
    print("2. In order to flag a trap, enter F after row and column numbers, Example \"2 3 F\"")
# Function to check for completion of the game
def check_over() -> bool:
    """
    Function to check for completion of the game.
    """
    global trap_values
    global n
    global traps_no
    # Count of all numbered values
    count = 0
     # Loop for checking each cell in the grid
    for r in range(n):
        for col in range(n):
            # If cell not empty or flagged
            if trap_values[r][col] != ' ' and trap_values[r][col] != 'F':
                count = count + 1
    # Count comparison
    if count == n * n - traps_no:
        return True
    else:
        return False
# Display all the trap locations
def show_traps() -> None:
    """
    Function to display all the trap locations.
    """
    global trap_values
    global numbers
    global n

    for r in range(n):
        for col in range(n):
            if numbers[r][col] == -1:
                trap_values[r][col] = 'M'

def game_loop() -> None:
    """
    Main function to run the game loop.
    """
    global n, traps_no, numbers, trap_values, flags

    set_traps()
    set_values()
    instructions()

    over = False

    while not over:
        print_traps_layout()

        inp = input("Enter row number followed by space and column number = ").split()

        if len(inp) == 2:
            try:
                val = list(map(int, inp))
            except ValueError:
                clear()
                print("Wrong input!")
                instructions()
                continue
        elif len(inp) == 3:
            if inp[2].lower() != 'f':
                clear()
                print("Wrong Input!")
                instructions()
                continue
            try:
                val = list(map(int, inp[:2]))
            except ValueError:
                clear()
                print("Wrong input!")
                instructions()
                continue

            if val[0] > n or val[0] < 1 or val[1] > n or val[1] < 1:
                clear()
                print("Wrong input!")
                instructions()
                continue

            r, col = val[0] - 1, val[1] - 1
            if [r, col] in flags:
                clear()
                print("Flag already set")
                continue

            if trap_values[r][col] != ' ':
                clear()
                print("Value already known")
                continue

            if len(flags) < traps_no:
                clear()
                print("Flag set")
                flags.append([r, col])
                trap_values[r][col] = 'F'
                continue
            else:
                clear()
                print("Flags finished")
                continue

        else:
            clear()
            print("Wrong input!")
            instructions()
            continue

        if val[0] > n or val[0] < 1 or val[1] > n or val[1] < 1:
            clear()
            print("Wrong Input!")
            instructions()
            continue

        r, col = val[0] - 1, val[1] - 1

        if [r, col] in flags:
            flags.remove([r, col])

        if numbers[r][col] == -1:
            trap_values[r][col] = 'M'
            show_traps()
            print_traps_layout()
            print("Landed on a trap. GAME OVER!!!!!")
            over = True
            continue

        elif numbers[r][col] == 0:
            global vis
            vis = []
            trap_values[r][col] = '0'
            neighbours(r, col)

        else:
            trap_values[r][col] = str(numbers[r][col])

        if check_over():
            show_traps()
            print_traps_layout()
            print("Congratulations!!! YOU WIN")
            over = True
            continue
        clear()
if __name__ == "__main__":
    game_loop()
