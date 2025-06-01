#!/usr/bin/env python3
"""
Tic Tac Toe – Command-Line Edition
---------------------------------
• Two-player game (X vs. O) played in the terminal.
• Players enter positions 1-9 that map to board squares:

      1 | 2 | 3
     ---+---+---
      4 | 5 | 6
     ---+---+---
      7 | 8 | 9

• Detects wins across rows, columns, and diagonals.
• Handles draws, invalid moves, and replay prompts.
"""

import sys

# Winning line indices (0-based)
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),        # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),        # columns
    (0, 4, 8), (2, 4, 6)                    # diagonals
]


def print_board(board: list[str]) -> None:
    """Display the current board state."""
    display = [str(v) if isinstance(v, int) else v for v in board]
    print(f"\n {display[0]} | {display[1]} | {display[2]} "
          f"\n---+---+---"
          f"\n {display[3]} | {display[4]} | {display[5]} "
          f"\n---+---+---"
          f"\n {display[6]} | {display[7]} | {display[8]} \n")


def check_winner(board: list[str]) -> str | None:
    """Return 'X' or 'O' if that player has won, otherwise None."""
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] and board[a] in ("X", "O"):
            return board[a]
    return None


def is_draw(board: list[str]) -> bool:
    """True if all squares are filled and there is no winner."""
    return all(isinstance(v, str) for v in board) and not check_winner(board)


def get_move(player: str, board: list[str]) -> int:
    """Prompt the current player for a legal move (1-9)."""
    while True:
        try:
            pos = int(input(f"Player {player}, choose a square (1-9): ").strip())
            if pos not in range(1, 10):
                raise ValueError
            if isinstance(board[pos - 1], str):
                print("That square is already taken. Try again.")
                continue
            return pos - 1  # convert to 0-based index
        except ValueError:
            print("Invalid input. Enter a number 1 through 9.")


def play_game() -> None:
    """Run a single round of Tic Tac Toe."""
    board: list[str | int] = list(range(1, 10))  # 1-9 placeholders
    current = "X"

    while True:
        print_board(board)
        move = get_move(current, board)
        board[move] = current

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🎉 Player {winner} wins!\n")
            break
        if is_draw(board):
            print_board(board)
            print("It’s a draw! 🤝\n")
            break

        current = "O" if current == "X" else "X"  # switch player

    again = input("Play again? (y/n) ").strip().lower()
    if again.startswith("y"):
        play_game()
    else:
        print("Thanks for playing!")
        sys.exit(0)


if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
