# Rename lots of files stored in a certain directory
# Process each file name and remove the numbers from the name
import os

def rename_files():
    #1: Retrieve the file names from a certain directory
    files_list = os.listdir('/Users/spencerbertsch/Desktop/Udacity Courses/Python Programming/Sample Data/Renaming Files/prank')
    print(files_list)
    #Check that we're in the right directory!
    saved_path = os.getcwd()
    print(saved_path)

    os.chdir('/Users/spencerbertsch/Desktop/Udacity Courses/Python Programming/Sample Data/Renaming Files/prank')
    #2: Rename each of the files, removing the numbers from each name
    for file_name in files_list:
        new_file_name = file_name.translate(None, '0123456789') # removes all numbers from the file name
        os.rename(file_name, new_file_name)
        print("Old file name: " + file_name + "   New file name: " + new_file_name)


    os.chdir(saved_path) #change the working directory back to what it was before we renamed the files

rename_files()



