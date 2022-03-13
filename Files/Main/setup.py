import os
import time
from tkinter import *
from tkinter.messagebox import *
import sys
file = sys.argv[0]
path_run = os.path.dirname(file)
list_files = os.listdir(path_run)
files = ['config.py', 'edit_menu.py', 'help_menu.py', 'file_menu.py', 'format_menu.py']
for i in files:
    if i in list_files:
        pass
    else:
        error = showerror('Backpack Notepad Error', 'faylları yükləmək olmur, zəhmət olmasa tətbiqi öz qovluğunda başladın!')
        try:
            sys.exit()
        except:
            exit()
os.mkdir(path_run+'/files')
os.system('start '+path_run+'/Backpack_Notepad.exe')
exit()