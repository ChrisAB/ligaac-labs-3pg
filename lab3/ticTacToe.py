import tkinter as tk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk



class Window():
    def __init__(self, master=None):
        self.master = master
        load_red = Image.open("red_x.png")
        load_red = load_red.resize((75,75), Image.ANTIALIAS)
        self.render_red = ImageTk.PhotoImage(image=load_red)
        load_green = Image.open("green_o.jpg")
        load_green = load_green.resize((75,75), Image.ANTIALIAS)
        self.render_green = ImageTk.PhotoImage(load_green)
        load_placeholder = Image.open("placeholder.png")
        self.render_placeholder = ImageTk.PhotoImage(load_placeholder)
        self.board = [[],[],[]]
        self.player_turn = 1
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    height=75,
                    width=75,
                    borderwidth=1,
                    image=self.render_placeholder,
                    command=lambda m=[i,j]: self.assignImage(m)
                )
                self.board[i].append(button)
                button.grid(row=i,column=j)
        self.start_button = tk.Button(
            height=10,
            width=10,
            text="Start game"
        )
        #self.start_button.grid(row=3,column=3)
    
    def assignImage(self, method):
        if self.board[method[0]][method[1]].cget('image') != 'pyimage3':
            showinfo("Bad Square","Choose another square")
            return False
        if self.player_turn == 1:
            self.board[method[0]][method[1]].configure(image=self.render_green)
            self.player_turn = 2
        else:
            self.board[method[0]][method[1]].configure(image=self.render_red)
            self.player_turn = 1
        if(self.evaluateWinner()):
            self.master.destroy()
    
    def areButtonsEqual(self,button1,button2,button3):
        if(button1.cget('image') == button2.cget('image') and button2.cget('image') == button3.cget('image') and button3.cget('image') != "pyimage3"):
            return True
        else:
            return False

    def evaluateWinner(self):
        if (self.areButtonsEqual(self.board[0][0],self.board[1][1],self.board[2][2]) or
            self.areButtonsEqual(self.board[0][2],self.board[1][1],self.board[2][0]) or
            self.areButtonsEqual(self.board[0][0],self.board[0][1],self.board[0][2]) or
            self.areButtonsEqual(self.board[1][0],self.board[1][1],self.board[1][2]) or
            self.areButtonsEqual(self.board[2][0],self.board[2][1],self.board[2][2]) or
            self.areButtonsEqual(self.board[0][0],self.board[1][0],self.board[2][0]) or
            self.areButtonsEqual(self.board[0][1],self.board[1][1],self.board[2][1]) or
            self.areButtonsEqual(self.board[0][2],self.board[1][2],self.board[2][2])):
            showinfo("Winner winner chicken dinner","Player " + str(self.player_turn) + " won")
            return True
        else:
            return False

    def startGame(self):
        self.master.mainloop()

window = tk.Tk()
m = Window(window)
m.startGame()