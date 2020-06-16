from os.path import exists, join, getsize
from tkinter import *
from os.path import splitext
import os
from PIL import Image, ImageTk

f = ""
filename = ""
file_extension = ""


class FileDetails():


    def __init__(self, cleanUpGui, folder, path):
        self.gui = cleanUpGui
        self.folder = folder
        self.path = path

    def get_extension(self):
        filename, file_extension = os.path.splitext(self.path)
        return file_extension

    def display_details(self):
        if self.path != "" and exists(join(self.folder.path, self.path)):
            self.gui.current_file_name.configure(text="file name: " + self.path)
            file_size = getsize(join(self.folder.path, self.path))
            self.gui.current_file_size.configure(text="file size: " + str(file_size))
            if self.get_extension() == ".txt" or ".docx":
                with open(join(self.folder.path, self.path), 'r') as f:
                    first_lines = f.readlines()
                self.gui.current_file_first_lines.configure(text="first lines: " + str(first_lines))
            elif self.get_extension() == ".png" or ".jpg":
                load = Image.open("parrot.jpg")
                render = ImageTk.PhotoImage(load)
                
                img = Label(self, image=render)
                img.image = render
                img.place(x=0, y=0)





                im = Image.open((join(self.folder.path, self.path)))
                self.gui.current_file_image.configure(text="Preview image: " + im.show())
        else:
            self.gui.current_file_name.configure(text="file name: <no file selected>")
            self.gui.current_file_size.configure(text="file size: <no file selected>")
            self.gui.current_file_first_lines.configure(text="first lines: <no file selected>")
            self.gui.current_file_image.configure(text="Preview image: <no image selected>")

    def save_files(self):
        with open("saved_files", "a") as myfile:
            myfile.write("%s\n" % self.path)





