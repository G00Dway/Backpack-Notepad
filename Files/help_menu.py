from tkinter import *
from tkinter.messagebox import *
import sys
import webbrowser
import os
import time
import settings
import subprocess
from settings import menu
import config
file = sys.argv[0]
current_path = os.path.dirname(file)
path_now = os.listdir(current_path)

class Help():
    def program_ver():
        try:
            with open(current_path+'\\version.log', 'r') as ver_rn:
                version_program = ver_rn.read()
            showinfo("Backpack Notepad Version Info", message=" İndiki versiya: "+version_program)
        except:
            showerror("Backpack Notepad Error", message="Versiya faylı tapılmadı...")
    def about(root):
        showinfo(title="Haqqında", message=f"Python-un Tkinter-də həyata keçirilən və C# dilində yazılan sadə bir mətn redaktorudur | {config.name} Tərəfindən hazırlanmışdır, Website: https://zeynalovenver3.wixsite.com/backpack-notepad")
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
            import wget
        except ImportError:
            print("Fayllar Yuklenir...")
            print()
            os.system('pip install wget')
            print()
            print()
            print('Yeniden deneyin')
            time.sleep(1.5)
            exit()
        try:
            print("Yenilənmələr Yoxlanılır...")
            with open(current_path+'\\version.log', 'r') as version_now:
                versi = version_now.read()
            try:
                if os.path.exists(current_path+'\\updates\\version.log'):
                    try:
                        os.remove(current_path+"\\updates\\version.log")
                    except:
                        pass
                else:
                    pass
            except:
                pass
            try:
                wget.download("https://raw.githubusercontent.com/G00Dway/Backpack-Notepad/main/Files/version.log", out=current_path+"\\updates")
            except Exception:
                wget.download("https://raw.githubusercontent.com/G00Dway/Backpack-Notepad/main/Files/version.log", out="updates")
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
                with open(current_path+'\\updates\\version.log', 'r') as f:
                    vers = f.read()
                version_after = vers
            except:
                pass
            if versi == version_after:
                showinfo("Backpack Notepad Update", message="Backpack Notepad'a yenilənmə yoxdur")
            else:
                showinfo("Backpack Notepad Update", message="Backpack Notepad'a yenilənmə mövcuddur! Yeni versiya: "+version_after)
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
    sitesMenu.add_command(label="Sayt WIX", command=Help.about_site_WIX)
    menubar.add_cascade(label="Kömək", menu=helpMenu)
    menubar.add_cascade(label="Saytlar", menu=sitesMenu)

    root.config(menu=menubar)


if __name__ == "__main__":
    pass
