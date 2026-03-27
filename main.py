import tkinter as tk
import numpy as np
from scipy import signal
from time import sleep
from threading import Thread

BOARD_SIZE_ROWS: int = 500
BOARD_SIZE_COLS: int = 500
CANVAS_ROWS: int = 40
CANVAS_COLS: int = 40
CANVAS_CELL_SIZE_ROWS: int = 10
CANVAS_CELL_SIZE_COLS: int = 10
CANVAS_SIZE_ROWS = CANVAS_ROWS * CANVAS_CELL_SIZE_ROWS
CANVAS_SIZE_COLS = CANVAS_COLS * CANVAS_CELL_SIZE_COLS

window_offset_row: int = 50
window_offset_cols: int = 50


tkr = tk.Tk()
play_button_obj: tk.Button
play_button_name = "play_button"
pause_button_name = "pause_button"
edit_button_name = "edit_button"
lock_button_name = "lock_button"
canvas_name = "canvas"
generation_label_name = "generation_label"
board: np.ndarray
generation: int
running: bool
wait_time: float


def setup_ui():
    global tkr, play_button_obj, play_button_name
    tkr.geometry("640x480")
    tkr.title("Game of Life")
    tk.Button(tkr, text="▶", name=play_button_name, command=play_button_command).grid(
        row=0, column=0
    )
    tk.Button(tkr, text="⏸", name=pause_button_name, command=pause_button_command).grid(
        row=0, column=1
    )
    tk.Button(tkr, text="✎", name=edit_button_name, command=edit_button_command).grid(
        row=0, column=2
    )
    tk.Button(tkr, text="🔒", name=lock_button_name, command=lock_button_command).grid(
        row=0, column=3
    )
    tk.Label(tkr, text="generation : ", name=generation_label_name).grid(
        row=0, column=4
    )
    cv = tk.Canvas(
        tkr, height=CANVAS_SIZE_ROWS, width=CANVAS_SIZE_COLS, name=canvas_name
    )
    cv.bind("<Button-1>", click_canvas)
    cv.grid(row=1, column=0, columnspan=5)


def click_canvas(event):
    event.__class__ = tk.Event


def make_step() -> None:
    global generation, board
    generation += 1
    neighbors = signal.convolve2d(board, [[1, 1, 1], [1, 0, 1], [1, 1, 1]], mode="same")
    dies = np.logical_and(np.logical_or(neighbors < 2, neighbors > 3), board == 1)
    borns = np.logical_and(board == 0, neighbors == 3)
    board[np.where(borns)] = 1
    board[np.where(dies)] = 0

    tkr.nametowidget(generation_label_name).config(text=f"generation : {generation}")
    canvas = tkr.nametowidget(canvas_name)
    canvas.__class__ = tk.Canvas
    for r in range(CANVAS_ROWS):
        for c in range(CANVAS_COLS):
            canvas.create_rectangle(
                r * CANVAS_CELL_SIZE_ROWS,
                c * CANVAS_CELL_SIZE_COLS,
                (r + 1) * CANVAS_CELL_SIZE_ROWS,
                (c + 1) * CANVAS_CELL_SIZE_COLS,
                fill="black"
                if board[r + window_offset_row, c + window_offset_cols] == 1
                else "white",
            )


def _thread_cycle() -> None:
    global running, wait_time
    while running:
        make_step()
        sleep(wait_time)


def run() -> None:
    global running
    running = True
    Thread(target=_thread_cycle).start()


def stop() -> None:
    global running
    running = False


def get_window(r0: int, r1: int, c0: int, c1: int) -> np.ndarray:
    global board
    return board[r0:r1, c0:c1]


def setup_board():
    global board, generation, running, wait_time
    board = np.ndarray(shape=(BOARD_SIZE_ROWS, BOARD_SIZE_COLS))
    generation = 0
    running = False
    wait_time = 1


def setup_engine():
    global run_status
    run_status = False


def set_run_state():
    global tkr, play_button_name, pause_button_name
    tkr.nametowidget(play_button_name).config(state=tk.DISABLED)
    tkr.nametowidget(pause_button_name).config(state=tk.ACTIVE)
    run()


def set_pause_state():
    global tkr, play_button_name, pause_button_name
    tkr.nametowidget(play_button_name).config(state=tk.ACTIVE)
    tkr.nametowidget(pause_button_name).config(state=tk.DISABLED)
    stop()


def play_button_command(*args):
    set_run_state()


def pause_button_command(*args):
    set_pause_state()


def edit_button_command(*args):
    pass


def lock_button_command(*args):
    pass


if __name__ == "__main__":
    setup_ui()
    setup_board()
    tkr.mainloop()
