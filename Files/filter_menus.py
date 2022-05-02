from tkinter import *
from tkinter.messagebox import *
import sys
import webbrowser
import os
import time
import settings
import subprocess
from settings import menu
file = sys.argv[0]
current_path = os.path.dirname(file)
path_now = os.listdir(current_path)

class Help():
    pass

def main(root, text, menubar):
    help = Help()
    helpMenu = Menu(menubar)

    root.config(menu=menubar)


if __name__ == "__main__":
    pass
