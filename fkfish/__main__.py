import sys
import platform
from tkinter import *
import argparse
import threading


def get_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', dest='mode',
                        type=str, help='fkfish mode', default=platform.system().lower())
    parser.add_argument('-p', '--passwd', dest='passwd',
                        type=str, help='exit nosafety passwd', default=None)
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
            from . import windows_blue
            return windows_blue
        if args.mode == 'winblue':
            from . import windows_blue
            return windows_blue
        if args.mode == 'black':
            from . import black_screen
            return black_screen

        raise Exception('Unsupported system', args.mode)

    def __init__(self, args):
        self._module = Module.module(args)

    def frame_create(self, win):
        return self._module.frame_create(win)

    def frame_destroy(self, win):
        return self._module.frame_destroy(win)


class FKFish():
    def __init__(self, args):
        module = Module(args)
        win = self._win_create()
        frame = self._frame_pack(module, win)

        self._frame_destroy(args, module, win, frame)
        win.mainloop()

    @staticmethod
    def _win_create():
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

    @staticmethod
    def _frame_pack(module, win):
        frame = module.frame_create(win)
        frame.pack(padx=0, pady=0)
        return frame

    @staticmethod
    def _frame_destroy(args, module, win, frame):
        def _destroy(module, win, frame):
            module.frame_destroy(frame)
            win.destroy()

        if args.passwd:
            class MatchPassWD(object):
                ipasswd = ""

                def __init__(self, passwd, task, *taskargs):
                    self.passwd = passwd
                    self.task = task
                    self.tarskargs = taskargs

                @staticmethod
                def input(self, event):
                    self.ipasswd = self.ipasswd + event.char
                    iplen = len(self.ipasswd)
                    plen = len(self.passwd)
                    if iplen > plen:
                        self.ipasswd = self.ipasswd[iplen - plen:]
                    if self.passwd in self.ipasswd:
                        self.task(*self.tarskargs)

            matchpwd = MatchPassWD(
                args.passwd, _destroy, module, win, frame)
            win.bind("<Key>", lambda event: MatchPassWD.input(matchpwd, event))
        else:
            win.bind("<Control-m>",
                     lambda _: _destroy(module, win, frame))


def main():
    args = get_args(sys.argv)
    FKFish(args)

    sys.exit()


if __name__ == '__main__':
    main()
