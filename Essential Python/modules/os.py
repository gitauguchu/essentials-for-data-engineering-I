#Provides functions for interacting with the operating system i.e managing files, directories and checking if they exist or not
import os

#Getting the current working directory
current_directory = os.getcwd()
print("Current directory", current_directory, sep=":")

#Listing files and directories in a directory
directory_path = r"C:\Users\user\Essential Python"
directory_contents = os.listdir(directory_path)
print(directory_contents)

#Check if a file or directory exists
path = r"C:\Users\user\Essential Python\modules\sys.py"
exists = os.path.exists(path)
print(exists)

#Getting information about a file
file_info = os.stat(path)
print(file_info)

#Creating a directory
#os.mkdir("fileio")

#Renaming a file
#os.rename("syst.py", "sys.py")

#Removing a file
#os.remove("remove.txt")

#Change current working directory
#os.chdir(r"C:\Users\user\Essential Python\modules")