import os
import glob
import subprocess


# subprocess.call(["cat", "/Users/marcobarreirinhas/Programs/pythonCommands/moveAround.py"])
subprocess.call(["cd", "/"])
os.system("cd")


# for files in glob.glob(os.path.join("/Users/marcobarreirinhas/Programs", '*')):
#     print("Options: ")
#     print(os.path.basename(files) + "\n")

# location = input("What language would you like? ")

# exist = False

# for f in glob.glob(os.path.join("/Users/marcobarreirinhas/Programs", '*')):
#     names = os.path.basename(f)
#     if location == names:
#         exist = True
#         break

# if exist:
#     print(location)

    


# if not exist:
#     print("File does not exist")
#     create = input("Would you like to create a new file?")

#     create = create.lower()

#     if create == "y":
#         new_file = input("File name: ")
#         if new_file == "":
#             new_file = location
#         parent_file = input("Parent file: ")
#         if parent_file == "":
#             parent_file = "/Users/marcobarreirinhas/Programs"
#         path = os.path.join(parent_file, new_file)
#         os.mkdir(path)
