# coding:utf-8


from tkinter import *


def frame_create(win):
    frame = Frame(win, cursor='none')
    width, height = win.winfo_screenwidth(), win.winfo_screenheight()
    canvas = Canvas(frame, height=height, width=width, background='black', highlightthickness=0)
    canvas.pack()

    return frame

def frame_destroy(frame):
    pass
