# coding:utf-8


from tkinter import *
import tkinter.font as tkFont
import threading
import os
import random


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
        new_line = lines[start: start + batch]
        new_line = [
            ' '*3 + line if line.startswith('        ') else line for line in new_line]
        text = ''.join(new_line)
        textvariable.set('\n' + text)
        if text.endswith('...\n'):
            time.sleep(max(0.01, min(random.normalvariate(0.5, 0.2), 10)))
        else:
            time.sleep(random.random() / 10)


def frame_create(win):
    frame = Frame(win, cursor='none')
    width, height = win.winfo_screenwidth(), win.winfo_screenheight()
    canvas = Canvas(frame, height=height, width=width)
    canvas.pack()

    thread = threading.Thread(target=log_printer, args=(canvas,))
    thread.daemon = True
    thread.start()

    return frame


def frame_destroy(frame):
    pass
