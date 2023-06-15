## In the event a filename has been appended with strange text inside of parentheses,
# this utility restores the original filename so that the files function as originally composed.

import os

path = "./target_directory/"
target = os.fsencode(path)
file_count = 0

input("Press any key to start reformatting file(s) in the target directory...")

for file in os.listdir(target):
    f = os.fsdecode(file)

    if f.find('(') == -1 or f.find(')') == -1:
        pass

    else:

        start_index = f.find('(') - 1
        end_index = f.find('.')
        file_name = f[:start_index]
        file_suffix = f[end_index:]

        old_path = path + f
        new_path = path + file_name + file_suffix

        try:
            os.rename(old_path, new_path)
            file_count += 1

        except FileNotFoundError:
            print(f + " not found!")
            pass

        except FileExistsError:
            print("Ignoring " + f + ". File already exists")
            pass

print("Renaming operation completed for " + str(file_count) + " file(s)")

# if __name__ == '__main__':
#
