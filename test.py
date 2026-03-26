import tkinter as tk
from board import board

tkr = None
brd: board
run_status: bool
play_button_obj: tk.Button
play_button_name = "play_button"
pause_button_name = "pause_button"
stop_button_name = "stop_button"
edit_button_name = "edit_button"
lock_button_name = "lock_button"
canvas_name = "canvas"


def setup_ui():
    global tkr, play_button_obj, play_button_name
    tkr.geometry("640x480")
    tkr.title("GoL")
    tk.Button(tkr, text="▶", name=play_button_name, command=play_button_command).grid(
        row=0, column=0
    )
    tk.Button(tkr, text="⏸", name=pause_button_name, command=pause_button_command).grid(
        row=0, column=1
    )
    tk.Button(tkr, text="■", name=stop_button_name, command=stop_button_command).grid(
        row=0, column=2
    )
    tk.Button(tkr, text="✎", name=edit_button_name, command=edit_button_command).grid(
        row=0, column=3
    )
    tk.Button(tkr, text="🔒", name=lock_button_name, command=lock_button_command).grid(
        row=0, column=4
    )
    tk.Canvas(tkr, height=400, width=600, name=canvas_name).grid(
        row=1, column=0, columnspan=5
    )


def setup_board():
    global brd
    brd = board(rows=500, cols=500)


def setup_engine():
    global run_status
    run_status = False


def set_run_state():
    global tkr, play_button_name, pause_button_name, brd
    tkr.nametowidget(play_button_name).config(state=tk.DISABLED)
    tkr.nametowidget(pause_button_name).config(state=tk.ACTIVE)
    brd.run()


def set_pause_state():
    global tkr, play_button_name, pause_button_name, brd
    tkr.nametowidget(play_button_name).config(state=tk.ACTIVE)
    tkr.nametowidget(pause_button_name).config(state=tk.DISABLED)
    brd.stop()


def play_button_command(*args):
    set_run_state()


def pause_button_command(*args):
    set_pause_state()


def stop_button_command(*args):
    pass


def edit_button_command(*args):
    pass


def lock_button_command(*args):
    pass


if __name__ == "__main__":
    tkr = tk.Tk()
    setup_ui()
    setup_board()
    tkr.mainloop()
