"""
Module to create the layout of the game.
"""
import random
# Constants
n: int = 5
traps_no: int = 5
numbers: list[list[int]] = [[0 for i in range(n)] for j in range(n)]
def set_traps() -> None:
    """
    Method to print the layout of the game.
    """
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
