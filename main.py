import os
import ru_local as ru


def acceptCommand():
    while True:
        cmnd = int(input(ru.CHOICE))
        if cmnd > 0 and cmnd < 8:
            return int(cmnd)
        else:
            print(ru.NOT_CHOICE)
command = acceptCommand()
print(command)


def moveUp():
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    os.chdir(parent_directory)
    print(ru.CURRENT_DIRECTORY, os.getcwd())


def moveDown(currentDir):
    subdirectory_name = input(ru.CATALOG_NAME)
    if not subdirectory_name or not os.path.isdir(currentDir) or os.path.exists(currentDir):
        print(ru.TRY_AGAIN)
        return
    if not os.path.exists(os.path.join(currentDir, subdirectory_name)) or not os.path.isdir(os.path.join(currentDir, subdirectory_name)):
        print(ru.NOT_FIND)
        return
    else:
        os.chdir(os.path.join(currentDir, subdirectory_name))
        print(ru.NEW_NAME, os.getcwd())


def findFiles(directory, target):
    file_directory = []

    if os.path.isfile(directory) and target in os.path.basename(directory):
        file_directory.append(directory)

    if os.path.isdir(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                if target in file:
                    file_directory.append(os.path.join(root, file))

    if len(file_directory) == 0:
        print(ru.NOT_FIND)
    else:
        return file_directory


def run_command(command):
    if command == 1:
        print(*os.listdir())
    if command == 2:
        moveUp()
    if command == 3:
        direct = input()
        moveDown(direct)
    if command == 4:
        route = input()
        count_files(route)
    if command == 5:
        route = input()
        count_bytes(route)
    if command == 6:
        route = input()
        aim = input()
        findFiles(aim, route)


def count_files(path):
    cnt = 0

    try:
        for item in os.listdir(path):
            new_path = os.path.join(path, item)
            if os.path.isfile(new_path):
                cnt += 1
            elif os.path.isdir(new_path):
                cnt += count_files(new_path)
        return cnt
    except PermissionError:
        print(None)


def count_bytes(path):
    byte = 0

    try:
        for item in os.listdir(path):
            new_path = os.path.join(path, item)
            if os.path.isfile(new_path):
                byte += os.path.getsize(new_path)
            elif os.path.isdir(new_path):
                byte += count_bytes(new_path)
        return byte
    except PermissionError:
        print(None)


def main():
    while True:
        QUIT = 7
        print(os.getcwd())
        print(ru.MENU)
        command = acceptCommand()
        run_command(command)
        if command == QUIT:
            print('Работа программы завершена.')
            break


if __name__ == '__main__':
    main()
