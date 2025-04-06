"""
Module to show the traps of the game.
"""
n: int = 5
trap_values: list[list[object]] = [[0 for i in range(n)] for j in range(n)]
numbers: list[list[int]] = [[0 for i in range(n)] for j in range(n)]
def show_traps() -> None:
    """
    Function to display all the trap locations.
    """
    for r in range(n):
        for col in range(n):
            if numbers[r][col] == -1:
                trap_values[r][col] = 'M'
