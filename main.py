import tkinter as tk
from board import board

class main_gui:
    
    tkr=None
    brd:board
    
    def setup_ui(self):
        self.tkr.geometry("640x480")
        self.tkr.title("GoL")
        tk.Button(self.tkr,text="▶",).grid(row=0,column=0)
        tk.Button(self.tkr,text="⏸",).grid(row=0,column=1)
        tk.Button(self.tkr,text="■",).grid(row=0,column=2)
        tk.Button(self.tkr,text="✎").grid(row=0,column=3)
        tk.Button(self.tkr,text="🔒").grid(row=0,column=4)
        

    def setup_board(self):
        self.brd=board(rows=500,cols=500)
        
    
        
    def __init__(self):
        self.tkr=tk.Tk()
        self.setup_ui()
        self.setup_board()
        
        self.tkr.mainloop()
        
if __name__=="__main__":
    m=main_gui()