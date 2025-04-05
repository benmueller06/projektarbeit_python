n: int = 5
vis: list[list[int]] = []
numbers: list[list[int]] = [[0 for i in range(n)] for j in range(n)]
trap_values = [[' ' for y in range(n)] for x in range(n)]


def neighbours(r: int, col: int) -> None:
    """
    Function to process neighboring cells recursively.
    Updates the trap_values grid and marks cells as visited.
    """
    global trap_values
    global vis

    # If the cell is not already visited
    if [r, col] not in vis:
        # Mark the cell as visited
        vis.append([r, col])

        # Update the trap_values grid with the value from numbers
        trap_values[r][col] = str(numbers[r][col])

        # If the cell is zero-valued, recursively process its neighbors
        if numbers[r][col] == 0:
            if r > 0:
                neighbours(r - 1, col)
            if r < n - 1:
                neighbours(r + 1, col)
            if col > 0:
                neighbours(r, col - 1)
            if col < n - 1:
                neighbours(r, col + 1)
            if r > 0 and col > 0:
                neighbours(r - 1, col - 1)
            if r > 0 and col < n - 1:
                neighbours(r - 1, col + 1)
            if r < n - 1 and col > 0:
                neighbours(r + 1, col - 1)
            if r < n - 1 and col < n - 1:
                neighbours(r + 1, col + 1)