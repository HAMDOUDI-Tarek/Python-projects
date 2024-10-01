import tkinter as tk
from tkinter import messagebox
from random import randrange

# Define the main game class
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        # Create the board buttons (3x3 grid)
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.board = [[str(3*i+j+1) for j in range(3)] for i in range(3)]
        self.create_buttons()

    # Create and layout buttons for each cell
    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=" ", font=('Arial', 24), width=5, height=2,
                                               command=lambda i=i, j=j: self.user_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)
        
        # The central cell is the first computer move (X)
        self.board[1][1] = "X"
        self.animate_move(self.buttons[1][1], "X")

    # Handle user move
    def user_move(self, i, j):
        if self.board[i][j] not in ["O", "X"]:
            self.board[i][j] = "O"
            self.animate_move(self.buttons[i][j], "O")
            if self.check_winner("O"):
                messagebox.showinfo("Tic Tac Toe", "You win!")
                self.reset_game()
            elif not self.free_fields():
                messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
                self.reset_game()
            else:
                self.cpu_move()

    # Handle CPU move
    def cpu_move(self):
        empty_cells = self.free_fields()
        if empty_cells:
            i, j = empty_cells[randrange(len(empty_cells))]
            self.board[i][j] = "X"
            self.animate_move(self.buttons[i][j], "X")
            if self.check_winner("X"):
                messagebox.showinfo("Tic Tac Toe", "You lose!")
                self.reset_game()
            elif not self.free_fields():
                messagebox.showinfo("Tic Tac Toe", "It's a Draw!")
                self.reset_game()

    # Simple animation to gradually increase text size for a move
    def animate_move(self, button, sign, size=10):
        if size <= 24:
            button.config(text=sign, font=('Arial', size))
            self.root.after(30, lambda: self.animate_move(button, sign, size + 2))
        else:
            button.config(state=tk.DISABLED)

    # Check for winner
    def check_winner(self, sign):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i][j] == sign for j in range(3)) or \
               all(self.board[j][i] == sign for j in range(3)):
                return True
        if all(self.board[i][i] == sign for i in range(3)) or \
           all(self.board[i][2-i] == sign for i in range(3)):
            return True
        return False

    # Get free fields
    def free_fields(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] not in ["O", "X"]]

    # Reset the game for a new round
    def reset_game(self):
        self.board = [[str(3*i+j+1) for j in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ", state=tk.NORMAL)
        self.board[1][1] = "X"
        self.animate_move(self.buttons[1][1], "X")

# Start the Tkinter event loop
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
