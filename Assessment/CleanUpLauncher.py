from tkinter import *

from Assessment.CleanUpGui import CleanUpGui

root = Tk()
cleanup = CleanUpGui(root)
folder_path = StringVar()

root.geometry("400x400")


# messy folder should be a sub-folder in your project.


root.mainloop()