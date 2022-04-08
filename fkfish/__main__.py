import sys
import platform
from tkinter import *


_sys = platform.system()


def module():
    global _sys
    if _sys == 'Linux':
        from . import linux_reboot
        return linux_reboot
    elif _sys == 'Windows':
        from . import linux_reboot
        return linux_reboot

    raise Exception('Unsupported system', _sys)


_module = module()


def frame_pack(win):
    frame = _module.frame_create(win)
    frame.pack(padx=0, pady=0)
    return frame


def frame_destroy(win, frame):
    _module.frame_destroy(frame)
    win.destroy()


def win_create():
    win = Tk()
    win.title('fkfish')
    win.configure(bg='black')

    if _sys == "Linux":
        win.attributes('-type', 'black')
        win.attributes('-zoomed', False)
    win.attributes('-alpha', '1')
    win.attributes('-fullscreen', True)
    win.attributes('-topmost', True)

    return win


def main():
    win = win_create()
    frame = frame_pack(win)

    win.bind("<Control-m>", lambda _: frame_destroy(win, frame))
    win.mainloop()

    sys.exit()


if __name__ == '__main__':
    main()
