import tkinter as tk
from board import board

tkr=None
brd:board

def setup_ui():
    global tkr
    tkr.geometry("640x480")
    tkr.title("GoL")
    tk.Button(tkr,text="▶",name="play_button",command=play_button_onclick).grid(row=0,column=0)
    tk.Button(tkr,text="⏸",name="pause_button",command=pause_button_onclick).grid(row=0,column=1)
    tk.Button(tkr,text="■",name="stop_button",command=stop_button_onclick).grid(row=0,column=2)
    tk.Button(tkr,text="✎",name="edit_button",command=edit_button_onclick).grid(row=0,column=3)
    tk.Button(tkr,text="🔒",name="lock_button",command=lock_button_onclick).grid(row=0,column=4)
    tk.Canvas(tkr,height=400,width=600,name="").grid(row=1,column=0,columnspan=5)
    
    

def setup_board():
    global brd
    brd=board(rows=500,cols=500)
    
def play_button_onclick(*args):
    global brd
    brd.make_step()

def pause_button_onclick(*args):
    pass

def stop_button_onclick(*args):
    pass

def edit_button_onclick(*args):
    pass

def lock_button_onclick(*args):
    pass
   
if __name__=="__main__":
    tkr=tk.Tk()
    setup_ui()
    setup_board()
    tkr.mainloop()
