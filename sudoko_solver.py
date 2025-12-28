import tkinter as tk
from tkinter import messagebox

# ---------------- Sudoku Logic ---------------- #

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


# ---------------- GUI Functions ---------------- #

def load_puzzle():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            if puzzle[i][j] != 0:
                entries[i][j].insert(0, puzzle[i][j])
                entries[i][j].config(fg="blue")


def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            row.append(int(val) if val else 0)
        board.append(row)
    return board


def fill_board(board):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, board[i][j])


def solve():
    board = get_board()
    if solve_sudoku(board):
        fill_board(board)
        messagebox.showinfo("Solved", "Sudoku solved successfully 🎉")
    else:
        messagebox.showerror("Error", "No solution exists")


# ---------------- Sample Unsolved Sudoku ---------------- #

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# ---------------- GUI Layout ---------------- #

root = tk.Tk()
root.title("Sudoku Solver")
root.geometry("400x500")
root.resizable(False, False)

tk.Label(root, text="🧩 Sudoku Solver", font=("Arial", 18, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

entries = []

for i in range(9):
    row_entries = []
    for j in range(9):
        e = tk.Entry(frame, width=3, font=("Arial", 14),
                     justify="center", relief="solid", borderwidth=1)
        e.grid(row=i, column=j, padx=2, pady=2)
        row_entries.append(e)
    entries.append(row_entries)

tk.Button(root, text="Load Puzzle", command=load_puzzle,
          bg="#2196F3", fg="white", font=("Arial", 12), width=15).pack(pady=10)

tk.Button(root, text="Solve", command=solve,
          bg="#4CAF50", fg="white", font=("Arial", 12), width=15).pack()

root.mainloop()
