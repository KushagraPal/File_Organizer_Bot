import os
import shutil
from os import listdir
from os.path import isfile, join
import json

target = input("Enter folder path: ")

with open(join("config.json")) as json_file:
    mapping = json.load(json_file)

files = [f for f in listdir(target) if isfile(join(target, f))]

def move_file(file,move_to,extension):
    if not os.path.isdir(move_to):
        try:
            os.makedirs(move_to,
                      exist_ok=True)
        except PermissionError:
            print("Permission denied: Unable to create.")
        except Exception as e:
            print(f"An error occurred: {e}")

    if os.path.exists(join(move_to,f"{file}")):
        i = 1
        file_name = file.rsplit(".", 1)[0]
        while True:
            if not os.path.exists(join(move_to,f"{file_name}({i}).{extension}")):
                break
            i += 1

        shutil.move(join(target,file), join(move_to,f"{file_name}({i}).{extension}"))
        return
    shutil.move(join(target,file), join(move_to,file))


for file in files:
    extension = file.rsplit(".", 1)[-1].lower()
    if extension in mapping:
        move_file(file,join(target,f"{mapping[extension]}"),extension)

    elif  "." not in file :
        move_file(file,join(target,"Unknown"),extension)
    else:
        move_file(file,join(target,f"{extension}"),extension)
print("All done!")
