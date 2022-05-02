from asyncio import subprocess
from re import sub
from tkinter import *
from tkinter.messagebox import *
import sys
import os
import settings
import subprocess
from settings import menu
import config
file = sys.argv[0]
current_path = os.path.dirname(file)
path_now = os.listdir(current_path)

class Help():
    def about(root):
        showinfo(title="Haqqında", message=f"Python-un Tkinter-də həyata keçirilən və C# dilində yazılan sadə bir mətn redaktorudur | {config.name} Tərəfindən hazırlanmışdır, Website: https://zeynalovenver3.wixsite.com/backpack-notepad")
    def settings(root):
        if "settings.py" in path_now:
            settings.menu.load()
        else:
            showerror(title="Backpack Notepad Settings Error", message="Parametrlər faylını yükləmək olmur!")
    def check_for_updates(root):
        with open(current_path+'\\version.log', 'r') as version_now:
            versi = version_now.read()
        try:
            subprocess.call(['pythonw', current_path+'\updates\update_format.pyw'])
            with open(current_path+'\updates\\version.log', 'r') as version_now_after:
                version_after = version_now_after.read()
            if versi == version_after:
                showinfo("Backpack Notepad Update", message="Backpack Notepad'a yenilənmə yoxdur")
            else:
                showinfo("Backpack Notepad Update", message="Backpack Notepad'a yenilənmə mövcuddur! Yeni versiya: "+version_after)
        except:
            pass


def main(root, text, menubar):

    help = Help()

    helpMenu = Menu(menubar)
    helpMenu.add_command(label="Ayarlar", command=help.settings)
    helpMenu.add_command(label="Haqqında", command=help.about)
    helpMenu.add_command(label="Program Yenilənməsi", command=help.check_for_updates)
    menubar.add_cascade(label="Kömək", menu=helpMenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    pass
