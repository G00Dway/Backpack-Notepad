from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *
from tkinter import messagebox
import file_menu
import splash_menu
import atexit
import edit_menu
import format_menu
import sys
import filter_menus
import os
import subprocess
file = sys.argv[0]
current_path_2 = os.path.dirname(file)
path_now_2 = os.listdir(current_path_2)
if os.path.exists(current_path_2+'/help_menu.py'):
    try:
        import help_menu
    except ImportError as fatal:
        showerror("Backpack Notepad Fatal Error", message="Lazımlı fayllardan birini başlatmağ olmur! Error kod: "+fatal)
else:
    showerror("Backpack Notepad Fatal Error", message="Fayllardan biri tapılmadı...")
    exit()
import config
files = ['config.py', 'edit_menu.py', 'help_menu.py', 'file_menu.py', 'format_menu.py', 'notepad-main.png']
file = sys.argv[0]
current_path = os.path.dirname(file)
path_now = os.listdir(current_path)

try:
    if os.path.exists(current_path+'/installed.cfg'):
        pass
    else:
        if "requirements.txt" in path_now:
            with open(current_path+'/installed.cfg', 'w') as cfg:
                cfg.write("Install='ok'")
except:
    pass

def on_close():
    if str(text.get(1.0,END)).isspace():
        root.destroy()
    else:
        response = messagebox.askyesno('Cıxış', 'həqiqətən çıxmaq istəyirsiniz?')
        if response:
            root.destroy()

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
version = "???"
try:
    with open(current_path+'/version.log', 'r') as ver_rn:
        version = ver_rn.read()
except:
    pass
root.title(f"Backpack Notepad (V.{version})")
root.geometry("750x350+450+200")
root.minsize(width=600, height=400)
# root.overrideredirect(True)
# root.attributes("-", True)
image_icon = PhotoImage(file=current_path+"/notepad-main.png")
root.iconphoto(True, image_icon)
text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
text.pack(fill=Y, expand=1)
text.focus_set()
menubar = Menu(root)
try:
    splash_menu.main("start")
except:
    pass
file_menu.main(root, text, menubar)
edit_menu.main(root, text, menubar)
format_menu.main(root, text, menubar)
help_menu.main(root, text, menubar)
filter_menus.main(root, text, menubar)
root.protocol('WM_DELETE_WINDOW',on_close)
root.mainloop()
