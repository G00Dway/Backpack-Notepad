from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import sys


class File():
    def newFile(self):
        self.filename = "Başsız"
        self.text.delete(0.0, END)

    def saveFile(self):
        try:
            t = self.text.get(0.0, END)
            f = open(self.filename, 'w')
            f.write(t)
            f.close()
        except:
            self.saveAs()

    def saveAs(self):
        f = asksaveasfile(mode='w', defaultextension='.txt')
        t = self.text.get(0.0, END)
        try:
            f.write(t.rstrip())
        except:
            showerror(title="Oops!", message="Faylı saxlamaq olmur...")

    def openFile(self):
        f = askopenfile(mode='r')
        self.filename = f.name
        t = f.read()
        self.text.delete(0.0, END)
        self.text.insert(0.0, t)

    def quit(self):
        entry = askyesno(title="Çıxış", message="Çıxmaq istədiyinizə əminsiniz?")
        if entry == True:
            self.root.destroy()

    def __init__(self, text, root):
        self.filename = None
        self.text = text
        self.root = root


def main(root, text, menubar):
    filemenu = Menu(menubar)
    objFile = File(text, root)
    filemenu.add_command(label="Yeni", command=objFile.newFile)
    filemenu.add_command(label="Aç", command=objFile.openFile)
    filemenu.add_command(label="Yadda saxla", command=objFile.saveFile)
    filemenu.add_command(label="Kimi saxlamaq...", command=objFile.saveAs)
    filemenu.add_separator()
    filemenu.add_command(label="Cıxış", command=objFile.quit)
    menubar.add_cascade(label="Fayl", menu=filemenu)
    root.config(menu=menubar)


if __name__ == "__main__":
    pass
