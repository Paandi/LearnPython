import os

#getcwd
#chdir
#listdir   --all dir and subdir
#mkdir
#rename
#remove
#rmdir


----get current path
os.getcwd()

--- change current directory
os.chdir("C:\\Users\\dinesh.pandey1\\AppData\\Local\\Programs\\Python\\")

--- list files in a dir 
os.list("C:\\Users\\dinesh.pandey1\\AppData\\Local\\Programs\\Python\\")

The above returns a list of files and subdir in current dir.

SCANDIR also does the samework more efficiently in terms of memory:

with os.scandir('my_directory/') as entries:
    for entry in entries:
        print(entry.name)


Here, os.scandir() is used in conjunction with the with statement because it supports the context manager protocol. Using a context manager closes the iterator and frees up acquired resources automatically after the iterator has been exhausted.


---- getting all the files in a list from a dir ...

if os.path.isfile(os.path.join(basepath, entry)):
        print(entry)



--- make dir

os.mkdir("C:\\Users\\dinesh.pandey1\\Desktop\\2021\\temp")

--- remvoe empty dir

os.rmdir("C:\\Users\\dinesh.pandey1\\Desktop\\2021\\temp")

--- remove file

os.remove('filename')


