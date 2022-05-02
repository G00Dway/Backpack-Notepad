import huepy
import wget
import shutil
import os
import sys
import subprocess
file = sys.argv[0]
current_path = os.path.dirname(file)
path_now = os.listdir(current_path)
version = ""
try:
    if os.path.exists(current_path+'\\version.log'):
        try:
            os.remove("version.log")
        except:
            pass
    else:
        pass
except:
    pass
wget.download("https://raw.githubusercontent.com/G00Dway/Backpack-Notepad/main/Files/version.log")
try:
    try:
        for i in os.listdir(current_path):
            if ".log" in i:
                if "version" in i:
                    pass
                else:
                    os.remove(i)
            else:
                pass
    except:
        pass
    with open(current_path+'\\version.log', 'r') as f:
        vers = f.read()
    version = vers
except:
    pass

