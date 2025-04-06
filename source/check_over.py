"""
Module to check over the game.
"""
n: int = 5
trap_values: list[list[int]] = [[0 for i in range(n)] for j in range(n)]
traps_no: int = 5
def check_over() -> bool:
    """
    Function to check for completion of the game.
    """
    # Count of all numbered values
    count = 0
    # Loop for checking each cell in the grid
    for r in range(n):
        for col in range(n):
            # If cell not empty or flagged
            if trap_values[r][col] != ' ' and trap_values[r][col] != 'F':
                count = count + 1

    # Count comparison
    return bool(count == n * n - traps_no)
