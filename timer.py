import tkinter
from tkinter import *
from datetime import datetime


if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry("640x480")
    root.title("Eddy's Cube Timer")
    timer = StringVar()
    start_time = StringVar()
    time_elapsed = StringVar()
    timer_started = False
    def key(keypress):
        global timer_started
        global start
        if keypress.char == " " and timer_started == False:
            timer_started = True
            start = datetime.now()
            start_time.set(start)
            #tkinter.Label(root, textvariable=start_time).grid(row=1, column=1)
        elif keypress.char == " " and timer_started == True:
            timer_started = False
            finish = datetime.now() - start
            time_elapsed.set(finish)
            tkinter.Label(root, textvariable=time_elapsed).grid(row=1, column=2)


    tkinter.Label(root, text="3x3x3").grid(row=0, column = 5)
    frame = tkinter.Frame(root)
    frame.bind("<KeyPress>", key)
    frame.grid()
    frame.focus_set()
    root.mainloop()

    