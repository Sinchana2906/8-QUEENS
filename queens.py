def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    # Extra condition: no adjacency
    for i in range(row):
        if abs(board[i] - col) <= 1 and abs(i - row) <= 1:
            return False

    return True


def solve_nqueens(n=8):
    solutions = []
    board = [-1] * n

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


def print_board(solution):
    n = len(solution)
    for row in range(n):
        line = ""
        for col in range(n):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")


if __name__ == "__main__":
    sols = solve_nqueens(8)
    print(f"Found {len(sols)} solutions")
    for sol in sols[:3]:  # print first 3 solutions
        print_board(sol) 
