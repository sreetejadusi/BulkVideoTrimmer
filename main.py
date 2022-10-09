from tkinter import *
from tkinter import filedialog
from pathlib import Path
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# ----------------------COMMANDS----------------------------
pathlist = []
filenames =[]


class AddFolder:
    def addfolder(self):
        self.folder = filedialog.askdirectory()
        for x in os.listdir(self.folder):
            pathlist.append(os.path.join(self.folder, x))
        for x in pathlist:
            sourcelist.insert(END, os.path.basename(x))
        renamedlist.delete(0, END)


class AddFiles:
    def addfiles(self):
        self.files = filedialog.askopenfilenames()
        for x in self.files:
            pathlist.append(x)
            filenames.append(Path(x).stem)
            sourcelist.insert(END, os.path.basename(x))
        renamedlist.delete(0, END)


class Clear:
    def clear(self):
        pathlist.clear()
        filenames.clear()
        sourcelist.delete(0, END)


class Sort:
    def sort(self):
        pathlist.sort()
        filenames.sort()
        sourcelist.delete(0, END)
        for x in pathlist:
            sourcelist.insert(END, os.path.basename(x))

class Trim:
    def trim(self):
        for path in list(pathlist):
            renamedlist.delete(0, END)
            ffmpeg_extract_subclip(path, int(trimfrom.get()), int(trimto.get()), targetname=os.path.dirname(path)+"/" + "TRIMMED"+os.path.basename(path))
            renamedlist.insert(END, os.path.basename(path))

# ----------------------GUI---------------------------------
window = Tk()
window.geometry("800x700")
window.config(bg="#F78E69")
window.title("Bulk Video Trimmer By Sree Teja Dusi")
window.resizable(0,0)

# ----------------------FIRSTFRAME---------------------------
firstframe = Frame(window, bg="#F78E69", padx=10, pady=10)
selection = Label(firstframe, text="Source Files", fg="black", bg="#F78E69", font=("Arial", 12))
addfolder = Button(firstframe, text="Add Folder", bg="white", fg="black", padx=2, bd=2, width=10,
                   command=AddFolder().addfolder)
addfiles = Button(firstframe, text="Add Files", bg="white", fg="black", padx=2, bd=2, width=10,
                  command=AddFiles().addfiles)
removesel = Button(firstframe, text="Remove Selection", bg="white", fg="black", padx=2, bd=2, width=10)
clear = Button(firstframe, text="Clear", bg="white", fg="black", padx=2, bd=2, width=10, command=Clear().clear)
sort = Button(firstframe, text="Sort", bg="white", fg="black", padx=2, bd=2, width=10, command=Sort().sort)
trim = Button(firstframe, text="Trim", bg="yellow", fg="black", padx=2, bd=2, width=10, command=Trim().trim)

# ----------------------SECONDFRAME--------------------------
secondframe = Frame(window, bg="#F78E69", padx=10, pady=10)
scrollone = Scrollbar(secondframe)
sourcelist = Listbox(secondframe, bg="white", fg="black", selectmode=MULTIPLE)
sourcelist.config(yscrollcommand=scrollone.set, width=114)
scrollone.config(command=sourcelist.yview)

# ----------------------THIRDFRAME---------------------------
thirdframe = Frame(window, bg="#F78E69", padx=10, pady=10)
modified = Label(thirdframe, text="Trimmed Files", fg="black", bg="#F78E69", font=("Arial", 12))

# ----------------------FOURTHFRAME-------------------------

fourthframe = Frame(window, bg="#F78E69", padx=10, pady=10)
scrolltwo = Scrollbar(fourthframe)
renamedlist = Listbox(fourthframe, bg="white", fg="black")
renamedlist.config(yscrollcommand=scrolltwo.set, width=114)
scrolltwo.config(command=renamedlist.yview)

# -----------------------FIFTHFRAME-------------------------
fifthframe = Frame(window, bg="#F78E69", padx=10, pady=10)
# FIFTHSUBONE

fifthsubone = Frame(fifthframe, bg="#F78E69", padx=10, pady=10)
Label(fifthsubone, text="Trim from", bg="#F78E69", fg="black", font=("Arial", 12)).pack(side=LEFT)
trimfrom = Entry(fifthsubone, bg="white", fg="black", font=("Arial", 12), width=16)
labelto = Label(fifthsubone, bg="#F78E69", fg="black", font=("Arial", 12), text="to")
trimto = Entry(fifthsubone, bg="white", fg="black", font=("Arial", 12), width=16)


############################END###################################
Label(window, text="Sree Teja Dusi", font=("Comic Sans", 13), fg="black", bg="#F78E69").pack(side=BOTTOM)

# FRAMES
firstframe.pack()
secondframe.pack()
thirdframe.pack()
fourthframe.pack()
fifthframe.pack()
# FIFTHSUBS
fifthsubone.pack()

# Elements
# FIRST FRAME
selection.grid(row=1, column=1, padx=10)
addfolder.grid(row=1, column=3, padx=10)
addfiles.grid(row=1, column=5, padx=10)
clear.grid(row=1, column=7, padx=10)
sort.grid(row=1, column=9, padx=10)
trim.grid(row=1, column=13, padx=10)
# SECONDFRAME
sourcelist.pack(side=LEFT)
scrollone.pack(side=RIGHT, fill=BOTH)

# THIRDFRAME
modified.pack(side=LEFT)

# FOURTHFRAME
renamedlist.pack(side=LEFT)
scrolltwo.pack(side=RIGHT, fill=BOTH)

# FIFTHFRAME
# FIFTHSUBONE
trimfrom.pack(side=LEFT, padx=10)
labelto.pack(side=LEFT)
trimto.pack(side=LEFT, padx=10)


window.mainloop()