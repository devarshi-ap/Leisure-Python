"""
author: @dev
since: 2021-02-17

This script implements the 'os' and 'shutil' modules to organize any given folder in terms of file type.
Say you have a mess of a folder with gifs, jpg's, xml's- virtually any file type, use this script to create folders that categorize loose files into their respective filetype folder.
"""

import os
import shutil

# path of folder needing organized
os.chdir("C:/Users/Amit/Pictures/_untitled.01/Organize")
print(os.getcwd())

# string var of folder path with unorganized files
Parent_folder = "C:/Users/Amit/Pictures/_untitled.01/Organize/"


try:
    for filename in os.listdir(Parent_folder):
        # splits filename into a list; [1] gives ext (.txt), [1:] splices the period (txt)
        ext = os.path.splitext(filename)[1][1:]
        print(ext)

        # if a folder with a given filetype  doesn't already exist, make one; otherwise, add to preexisting
        old_Location = Parent_folder + filename
        new_Location = Parent_folder + ext + "/" + filename

        if not os.path.isdir(ext):
            os.makedirs(ext)
            shutil.move(old_Location, new_Location)
        else:
            shutil.move(old_Location, new_Location)
except FileNotFoundError:
    print("No files to move broski.")
