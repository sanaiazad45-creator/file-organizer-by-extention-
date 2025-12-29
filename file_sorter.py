import os
import shutil

#folder dir for sorting files
folder_path = "/home/kardux/Project/Data_files/Test_folder"
#destination dirs for sorted files
files = os.listdir(folder_path)

for file in files:
    file_path = os.path.join(folder_path, file)

#if it be file, not folder
    if os.path.isfile(file_path):
        #get file extension
        file_extension = file.split(".")[-1].lower()
        #create destination folder path based on extension
        new_folder = os.path.join(folder_path, file_extension)
        os.makedirs(new_folder, exist_ok=True)

#new file path in destination folder
        new_path = os.path.join(new_folder, file)
#move file to new destination
        shutil.move(file_path, new_path)
        
        print("Moved Successfully")
        