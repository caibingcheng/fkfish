# coding:utf-8


import os
from tkinter import *
import threading
import random
import time


def frame_create(win):
    frame = Frame(win, cursor='none')
    width, height = win.winfo_screenwidth(), win.winfo_screenheight()
    canvas = Canvas(frame, height=height, width=width)
    canvas.pack()

    windows_blue_dir = os.path.split(os.path.abspath(__file__))[0]
    windows_blue_path = os.path.join(windows_blue_dir, 'windows_blue.png')
    global windows_blue_image
    windows_blue_image = PhotoImage(file=windows_blue_path)

    label = Label(canvas, justify='left', anchor='w', bg='#017BE0',
                  width=canvas.winfo_screenwidth(), height=canvas.winfo_screenheight(),
                  image=windows_blue_image)
    label.pack(padx=0, pady=0)

    textvariable = StringVar()
    label_text = Label(label, justify='left', anchor='w', bg='#017BE0', fg='#FEFFF9', font=(
        "MS Sans Serif", 32), textvariable=textvariable, width=10, height=1)
    label_text.pack(padx=0, pady=0)
    label_text.place(x=227, y=570)

    # 5 min at least
    # 15 * 50 = 750s ava
    def progress(start):
        while start < 100:
            start = start + random.randint(1, 3)
            if start > 100:
                start = 100
            textvariable.set(str(start) + ('%' if start < 100 else '% 完成'))
            time.sleep(max(0.01, min(random.normalvariate(15, 2), 30)))

    thread = threading.Thread(target=progress, args=(0,))
    thread.daemon = True
    thread.start()

    return frame


def frame_destroy(frame):
    pass
