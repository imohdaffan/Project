import tkinter as tk
from tkinter import messagebox
import winsound  # Works on Windows
import os

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - GUI with Sound, Scoreboard & Restart")
        self.player = "X"
        self.score = {"X": 0, "O": 0}
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.score_label = tk.Label(root, text=self.get_score_text(), font=('Arial', 16), fg='blue')
        self.score_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.create_board()

        self.restart_button = tk.Button(root, text="🔁 Restart Game", font=('Arial', 12), bg='lightgray',
                                        command=self.reset_board)
        self.restart_button.grid(row=4, column=0, columnspan=3, pady=10)

    def get_score_text(self):
        return f"Score - X: {self.score['X']} | O: {self.score['O']}"

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=" ", font=('Arial', 30), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i + 1, column=j)
                self.buttons[i][j] = button

    def play_sound(self, filename):
        if os.path.exists(filename):
            winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC)

    def on_click(self, row, col):
        if self.buttons[row][col]["text"] == " ":
            self.buttons[row][col]["text"] = self.player
            self.play_sound("click.wav")

            if self.check_winner(self.player):
                self.play_sound("win.wav")
                self.score[self.player] += 1
                self.score_label.config(text=self.get_score_text())
                messagebox.showinfo("Game Over", f"🎉 Player {self.player} wins!")
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.reset_board()
            else:
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self, player):
        for i in range(3):
            if all(self.buttons[i][j]["text"] == player for j in range(3)):
                return True
            if all(self.buttons[j][i]["text"] == player for j in range(3)):
                return True
        if all(self.buttons[i][i]["text"] == player for i in range(3)):
            return True
        if all(self.buttons[i][2 - i]["text"] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(self.buttons[i][j]["text"] != " " for i in range(3) for j in range(3))

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = " "
        self.player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
