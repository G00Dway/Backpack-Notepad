import os
import time
import sys
from tkinter import *
from tkinter.messagebox import *
file = sys.argv[0]
path_run = os.path.dirname(file)
list_files = os.listdir(path_run)
files = ['config.py', 'edit_menu.py', 'help_menu.py', 'file_menu.py', 'format_menu.py', 'LICENSE', 'notepad-main.png', 'setup.exe', 'version.log', 'Backpack_Notepad.exe']
proceed = askyesno("Backpack Notepad Uninstallation", "Həqiqətən proqramı silmək istəyirsiniz?")
if proceed:
    time.sleep(0.5)
    for i in files:
        if i in list_files:
            os.remove(i)
        else:
            pass
    info = showinfo('Backpack Notepad Uninstallation', 'Proqram silindi.')
else:
    sys.exit()
exit()