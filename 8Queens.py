def print_board(board, n):
    for row in range(n):
        if row < len(board):
            print(" ".join("Q" if i == board[row] else "." for i in range(n)))
        else:
            print(" ".join("." for _ in range(n)))
    print("\n" + "-" * (2 * n - 1) + "\n")

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(n, row=0, board=[]):
    print(f"Step {row + 1}: Trying to place Queen at row {row}\n")
    print_board(board, n)
    
    if row == n:
        print("Final Solution:\n")
        print_board(board, n)
        exit()
    
    for col in range(n):
        if is_safe(board, row, col, n):
            solve_n_queens(n, row + 1, board + [col])

solve_n_queens(8)
