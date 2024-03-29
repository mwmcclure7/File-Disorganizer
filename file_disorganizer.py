import os
from shutil import move
import random

target_directory = input("Enter the directory that you would like to disorganize:")

# Completely disorganizes the target directory by taking files out of 
while True:
    folder_ext = '.placeholder'
    file_ext = ''
    if os.path.exists(target_directory):
        os.chdir(target_directory)

        while folder_ext != '':
            folder = random.choice(os.listdir(target_directory))
            folder_name, folder_ext = os.path.splitext(folder)
        current_directory = os.path.join(target_directory, folder)

        try:
            while file_ext == '':
                file = random.choice(os.listdir(current_directory))
                current_directory = os.path.join(current_directory, file)
                file_name, file_ext = os.path.splitext(file)
        except FileExistsError and IndexError:
            pass

        print(current_directory)
        new_location = os.path.join(target_directory, file)
        print(new_location)
        move(current_directory, new_location)
    else:
        print('Directory does not exist')
