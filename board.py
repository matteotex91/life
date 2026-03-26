import numpy as np
from scipy import signal


class board:
    board: np.ndarray
    generation: int

    def __init__(Self, rows: int = 100, cols: int = 100):
        Self.board = np.ndarray(shape=(rows, cols))
        Self.generation = 0

    def make_step(Self) -> None:
        Self.generation += 1
        neighbors = signal.convolve2d(Self.board, [[1, 1, 1], [1, 0, 1], [1, 1, 1]], mode="same")
        dies = np.logical_and(np.logical_or(neighbors < 2, neighbors > 3), Self.board == 1)
        borns = np.logical_and(Self.board == 0, neighbors == 3)
        Self.board[np.where(borns)] = 1
        Self.board[np.where(dies)] = 0
        print("stop here")


if __name__ == "__main__":
    b = board()
    b.board = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
    while True:
        b.make_step()
