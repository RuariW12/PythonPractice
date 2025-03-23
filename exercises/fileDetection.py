# Python file detection

import os

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else:
    print("That location doesn't exist")

# if it's in another folder, you do example/test.txt
# example would be whatever the file name is

#absolute file path:

file_path1 = "C:\\Users\HP\Desktop\\test.txt"
#would look something like this to find it in os