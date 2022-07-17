from tkinter import *
from tkinter.messagebox import *
import sys
import webbrowser
from tkinter import colorchooser
import os
import time
import settings
import subprocess
from settings import menu
file = sys.argv[0]
current_path = os.path.dirname(file)
path_now = os.listdir(current_path)

class Help():
    def exit():
        try:
            sys.exit()
        except:
            exit()
    def settings():
        pass

def main(root, text, menubar):
    def settings_menu():
        def load_settings():
            s = Tk()
            s.title("Backpack Notepad Ayarlar")
            s.geometry("100x300")
            s.mainloop()

        load_settings()



    def color():
        selected_color = colorchooser.askcolor()
        text.insert(INSERT, selected_color, "a")
    # def all_false():
    #     root.attributes("-fullscreen", False)
    #     root.attributes("-disabled", False)
    #     root.attributes("-toolwindow", False)
    def full_screen():
        def full_screen_exit():
            root.attributes("-fullscreen", False)
            instruments.delete("Full Ekran Cıxış")
            instruments.add_command(label="Full Ekran Böyüt", command=full_screen)
        root.attributes("-fullscreen", True)
        instruments.delete("Full Ekran Böyüt")
        instruments.add_command(label="Full Ekran Cıxış", command=full_screen_exit)
    def proqram_freeze():
        def proqram_unfreeze():
            root.attributes("-disabled", False)
            instruments.delete("Proqramı İşlət")
            instruments.add_command(label="Proqramı Dondur", command=proqram_freeze)
        root.attributes("-disabled", True)
        instruments.delete("Proqramı Dondur")
        instruments.add_command(label="Proqramı İşlət", command=proqram_unfreeze)
    def chng():
        def unchng():
            root.attributes("-toolwindow", False)
            instruments.delete("İnterfeysi Düzəlt")
            instruments.add_command(label="İnterfeysi Dəyiş", command=chng)
        root.attributes("-toolwindow", True)
        instruments.delete("İnterfeysi Dəyiş")
        instruments.add_command(label="İnterfeysi Düzəlt", command=unchng)
    helpMenu = Menu(menubar)
    instruments = Menu(menubar)
    instruments.add_command(label="Full Ekran Böyüt", command=full_screen)
    instruments.add_command(label="Proqramı Dondur", command=proqram_freeze)
    instruments.add_command(label="İnterfeysi Dəyiş", command=chng)
    instruments.add_command(label="Rəng Seçimi", command=color)
    helpMenu.add_command(label="Ayarlar Aç", command=settings_menu())
    menubar.add_cascade(label="İnstrumentlər", menu=instruments)
    menubar.add_cascade(label="Ayarlar", menu=helpMenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    pass
