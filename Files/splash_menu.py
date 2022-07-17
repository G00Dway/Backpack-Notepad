import tkinter
from tkinter import *
import sys
from turtle import title
import webbrowser
import threading
import os
import time
import subprocess
from settings import menu
file = sys.argv[0]
current_path = os.path.dirname(file)
path_now = os.listdir(current_path)

class Splash():
    def start_splash():
        pass


def main(load):
    if load == "start":
        Splash.start_splash()
    else:
        pass
