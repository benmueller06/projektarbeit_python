"""
Module to create the layout of the game.
"""
n: int = 5
trap_values: list[list[int]] = [[0 for i in range(n)] for j in range(n)]

def print_traps_layout() -> None:
    """
    Method to print the layout of the game.
    """
    print()
    print("\t\t\tSPACESTATION\n")
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
