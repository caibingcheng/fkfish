#coding:utf-8


from tkinter import *
import tkinter.font as tkFont
import threading
import os
import sys


def log_printer(parent):
    import time

    lines = []
    textvariable = StringVar()

    label = Label(parent, justify='left', anchor='w', bg='black', fg='white',
                  width=parent.winfo_screenwidth(), height=parent.winfo_screenheight(),
                  textvariable=textvariable)
    label.pack(padx=0, pady=0)

    log_dir = os.path.split(os.path.abspath(__file__))[0]
    log_path = os.path.join(log_dir, 'linux_boot.log')
    with open(log_path, encoding='utf-8') as f:
        lines = f.readlines()
        f.close()

    line_height = tkFont.Font(font=label['font']).metrics('linespace')
    batch = parent.winfo_screenheight() // line_height

    for start in range(0, len(lines) - batch):
        textvariable.set(''.join(lines[start: start + batch]))
        new_line = lines[start: start + batch]
        if '...' in new_line:
            time.sleep(0.5)
        time.sleep(0.1)


def frame_create(win):
    frame = Frame(win)
    width, height = win.winfo_screenwidth(), win.winfo_screenheight()
    canvas = Canvas(frame, height=height, width=width)
    canvas.pack()

    thread = threading.Thread(target=log_printer, args=(canvas,))
    thread.daemon = True
    thread.start()

    return frame


def frame_destroy(frame):
    pass