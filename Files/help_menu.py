from tkinter import *
from tkinter.messagebox import *
import sys
import os
import settings
from settings import menu
import config
file = sys.argv[0]
current_path = os.path.dirname(file)
path_now = os.listdir(current_path)

class Help():
    def about(root):
        showinfo(title="Haqqında", message=f"Python-un Tkinter-də həyata keçirilən sadə bir mətn redaktoru | {config.name} Tərəfindən hazırlanmışdır.")
    def settings(root):
        if "settings.py" in path_now:
            settings.menu.load()
        else:
            showerror(title="Backpack Notepad Settings Error", message="Parametrlər faylını yükləmək olmur!")


def main(root, text, menubar):

    help = Help()

    helpMenu = Menu(menubar)
    helpMenu.add_command(label="Ayarlar", command=help.settings)
    helpMenu.add_command(label="Haqqında", command=help.about)
    menubar.add_cascade(label="Kömək", menu=helpMenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    pass
