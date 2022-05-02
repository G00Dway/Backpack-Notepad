from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *
import file_menu
import atexit
import edit_menu
import format_menu
import help_menu
import config
import os
import sys
files = ['config.py', 'edit_menu.py', 'help_menu.py', 'file_menu.py', 'format_menu.py', 'notepad-main.png']
file = sys.argv[0]
current_path = os.path.dirname(file)
path_now = os.listdir(current_path)
version = "0.3"

try:
    if os.path.exists(current_path+'\installed.cfg'):
        pass
    else:
        if "requirements.txt" in path_now:
            os.system('pip install -r requirements.txt')
            with open(current_path+'\installed.cfg', 'w') as cfg:
                cfg.write("Install='ok'")
except:
    pass

for i in files:
    if i in path_now:
        pass
    else:
        error = showerror('Backpack Notepad Error', 'faylları yükləmək olmur, zəhmət olmasa tətbiqi öz qovluğunda başladın!')
        try:
            sys.exit()
        except:
            exit()
root = Tk()

root.title(f"Backpack Notepad - V.{version}")
root.geometry("700x350+300+300")
root.minsize(width=600, height=400)
image_icon = PhotoImage(file=current_path+"/notepad-main.png")
root.iconphoto(True, image_icon)
text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
text.pack(fill=Y, expand=1)
text.focus_set()
menubar = Menu(root)

file_menu.main(root, text, menubar)
edit_menu.main(root, text, menubar)
format_menu.main(root, text, menubar)
help_menu.main(root, text, menubar)
root.mainloop()
