from os import listdir
from os.path import isdir, isfile, join


class FolderDetails():

    def __init__(self, path):
        self.path = path
        if isdir(path):
            # only add files not sub folders
            self.files_to_check = [f for f in listdir(path) if isfile(join(path, f))]

    def save_files(self, file_name):
        if file_name:
            never_delete = open(join(self.path, "saved_files"), "a")
            never_delete.write(file_name.path)
            never_delete.write("\n")

    def get_next_file(self):
        never_delete = open(join(self.path, "saved_files"), "r").read().splitlines()
        while self.files_to_check:
            next_file = self.files_to_check.pop()
            if next_file not in never_delete:
                return next_file
        else:
            pass


