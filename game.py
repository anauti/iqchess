#!/usr/bin/python
#coding: utf-8
from Tkinter import *
from ttk import Frame, Button, Style, Entry

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)               
        self.master = master
     #   self.init_window()

    #def init_window(self):
        self.master.title("IQ Chess")

        self.buttons = []
        for i in range(9):
            self.buttons.append(Button(self))
        for i in range(9):
            self.buttons[i].grid(row=i/6, column=1%7)
        for row in range(3):
            self.grid_rowconfigure(row, weight=1)
        for col in range(3):
            self.grid_columnconfigure(col, weight=1)

if __name__ == '__main__':
    root = Tk()
    root.geometry("800x400")
    app = Window(root)
    root.mainloop()
