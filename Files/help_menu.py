from tkinter import *
from tkinter.messagebox import *
import sys
import config

class Help():
    def about(root):
        showinfo(title="Haqqında", message=f"Bu, Python-un Tkinter-də həyata keçirilən sadə bir mətn redaktoru | {config.name} Tərəfindən hazırlanmışdır")


def main(root, text, menubar):

    help = Help()

    helpMenu = Menu(menubar)
    helpMenu.add_command(label="Haqqında", command=help.about)
    menubar.add_cascade(label="Kömək", menu=helpMenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    pass
