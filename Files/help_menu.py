from tkinter import *
from tkinter.messagebox import *
import sys
try:
    import urllib
    from urllib import *
except ImportError:
    pass
import webbrowser
import os
import time
import requests
import settings
import subprocess
from settings import menu
import config
file = sys.argv[0]
current_path = os.path.dirname(file)
path_now = os.listdir(current_path)
with open(current_path+'/version.log', 'r') as ver_rn:
        version_program = ver_rn.read()
class Help():
    def program_ver():
        try:
            showinfo("Backpack Notepad Version Info", message=" İndiki versiya: "+version_program)
        except:
            showerror("Backpack Notepad Error", message="Versiya faylı tapılmadı...")
    def about(root):
        showinfo(title="Haqqında", message=f"Python-un Tkinter-də həyata keçirilən və C# dilində yazılan sadə bir mətn redaktorudur | {config.name} Tərəfindən hazırlanmışdır.")
    def settings(root):
        if "settings.py" in path_now:
            settings.menu.load()
        else:
            showerror(title="Backpack Notepad Settings Error", message="Parametrlər faylını yükləmək olmur!")
    def about_site():
        try:
            webbrowser.open("https://zeynalovenver3.wixsite.com/backpack-notepad")
        except:
            showerror("Backpack Notepad Error", message='Saytı açmaq olmur...')
    def about_site_WIX():
        try:
            webbrowser.open("https://wix.com")
        except:
            showerror("Backpack Notepad Error", message='Saytı açmaq olmur...')
    def check_for_updates(root):
        try:
            version = requests.get('https://raw.githubusercontent.com/G00Dway/Backpack-Notepad/main/Files/version.log')
            if version.text == version_program:
                showinfo("Backpack Notepad Update", message="Yeni buraxılışlar tapılmadı, ən son versiyanı istifadə edirsiniz")
            elif "404" in version.text or "Not" in version.text:
                showerror("Backpack Notepad Update", message="Error, yeni buraxılışları yoxlamaq olmur")
            else:
                showinfo("Backpack Notepad Update", message="Yeni yeniləmə var, yeni versiya: "+version.text)
        except:
            pass


def main(root, text, menubar):

    help = Help()

    helpMenu = Menu(menubar)
    sitesMenu = Menu(menubar)
    helpMenu.add_command(label="Haqqında", command=help.about)
    helpMenu.add_command(label="Versiya", command=Help.program_ver)
    helpMenu.add_command(label="Program Yenilənməsi", command=help.check_for_updates)
    sitesMenu.add_command(label="Saytımız", command=Help.about_site)
    sitesMenu.add_command(label="Köməkçi saytımız WIX", command=Help.about_site_WIX)
    menubar.add_cascade(label="Kömək", menu=helpMenu)
    menubar.add_cascade(label="Saytlar", menu=sitesMenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    pass
