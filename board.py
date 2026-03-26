import numpy as np
from scipy import signal
from time import sleep
from tkinter import Tk


class board:
    board: np.ndarray
    generation: int
    running: bool
    wait_time: float

    def __init__(self, rows: int = 100, cols: int = 100):
        self.board = np.ndarray(shape=(rows, cols))
        self.generation = 0
        self.running = False
        self.wait_time = 1

    def make_step(self) -> None:
        self.generation += 1
        neighbors = signal.convolve2d(
            self.board, [[1, 1, 1], [1, 0, 1], [1, 1, 1]], mode="same"
        )
        dies = np.logical_and(
            np.logical_or(neighbors < 2, neighbors > 3), self.board == 1
        )
        borns = np.logical_and(self.board == 0, neighbors == 3)
        self.board[np.where(borns)] = 1
        self.board[np.where(dies)] = 0

    def run(self, tkr: Tk) -> None:
        while self.running:
            self.make_step()

            sleep(self.wait_time)

    def stop(self) -> None:
        self.running = False

    def get_window(self, r0: int, r1: int, c0: int, c1: int) -> np.ndarray:
        return self.board[r0:r1, c0:c1]


if __name__ == "__main__":
    b = board()
    b.board = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
    while True:
        b.make_step()
