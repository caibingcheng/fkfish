import sys
import platform
from tkinter import *
import argparse


def get_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', dest='mode',
                        type=str, help='fkfish mode', default=platform.system().lower())
    # parser.add_argument(
    #     '--high-cpu',  dest='highcpu', help='full processed cpu', action='store_true')
    return parser.parse_args()


class Module():
    @staticmethod
    def module(args):
        if args.mode == 'linux':
            from . import linux_reboot
            return linux_reboot
        if args.mode == 'windows':
            from . import linux_reboot
            return linux_reboot
        if args.mode == 'winblue':
            from . import windows_blue
            return windows_blue

        raise Exception('Unsupported system', args.mode)

    def __init__(self, args):
        self._module = Module.module(args)

    def frame_create(self, win):
        return self._module.frame_create(win)

    def frame_destroy(self, win):
        return self._module.frame_destroy(win)


class FKFish():
    def __init__(self, module):
        module = module

        win = self._win_create()
        frame = self._frame_pack(module, win)

        win.bind("<Control-m>",
                 lambda _: self._frame_destroy(module, win, frame))
        win.mainloop()

    def _win_create(self):
        win = Tk()
        win.title('fkfish')
        win.configure(bg='black')

        if platform.system() == "Linux":
            win.attributes('-type', 'black')
            win.attributes('-zoomed', False)
        win.attributes('-alpha', '1')
        win.attributes('-fullscreen', True)
        win.attributes('-topmost', True)

        return win

    def _frame_pack(self, module, win):
        frame = module.frame_create(win)
        frame.pack(padx=0, pady=0)
        return frame

    def _frame_destroy(self, module, win, frame):
        module.frame_destroy(frame)
        win.destroy()


def main():
    args = get_args(sys.argv)
    module = Module(args)
    FKFish(module)

    sys.exit()


if __name__ == '__main__':
    main()
