# Kuznetsov Igor - 100,
import os
import ru_local as ru


def acceptCommand():
    '''
    Requests the command number and, if the command number is specified incorrectly,
    displays an error message. Commands are requested until the correct command number
    is entered. Returns the correct command number.
    '''
    while True:
        cmd = int(input(ru.CHOICE))
        if cmd > 0 and cmd < 8:
            return int(cmd)
        else:
            print(ru.NOT_CHOICE)


def moveUp():
    '''
    Makes the current parent directory.
    '''
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    os.chdir(parent_directory)
    print(ru.CURRENT_DIRECTORY, os.getcwd())


def moveDown(currentDir):
    '''
    Prompts for the name of a subdirectory. If the name is specified correctly, it makes
    the directory located in currentDir current, otherwise it displays an error message.
    '''
    catalog_name = input(ru.CATALOG_NAME)

    if not catalog_name:
        print(ru.NOT_INDICATED)
        return

    check_path = os.path.join(currentDir, catalog_name)

    if not os.path.isdir(currentDir):
        print(ru.PATH_NOT_DIRECT_1, currentDir, ru.PATH_NOT_DIRECT_2)
        return

    if not os.path.exists(check_path) or not os.path.isdir(check_path):
        print(ru.SUBDIR_NOT_FOUND_1, catalog_name, ru.SUBDIR_NOT_FOUND_2, currentDir)
        return

    os.chdir(check_path)
    print(ru.NEW_NAME, os.getcwd())


def findFiles(directory, target):
    '''
    A recursive function that generates a list of paths to files whose names
    contain target. The search includes all subdirectories of the path directory.
    If the files are not found, displays a corresponding message.
    '''
    found_files = []
    if not os.path.exists(directory):
        print(f"Путь '{directory}' не существует")
        return found_files

    files_and_dirs = os.listdir(directory)

    for item in files_and_dirs:
        item_path = os.path.join(directory, item)

        if os.path.isfile(item_path):
            if target in item:
                found_files.append(item_path)
        else:
            found_files.extend(findFiles(item_path, target))
    return found_files


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
        return -1
    except FileNotFoundError:
        return -2


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
        return -1
    except FileNotFoundError:
        return -2


def run_command(command):
    if command == 1:
        data = os.listdir()
        for item in data:
            print(item)

    if command == 2:
        moveUp()

    if command == 3:
        moveDown(os.getcwd())

    if command == 4:
        catalog = input(ru.CATALOG_NAME)

        if catalog == '':
            res = count_files(os.getcwd())
        else:
            res = count_files(catalog)

        if res == -1:
            print('PermissionError')
        elif res == -2:
            print('FileNotFoundError')
        else:
            print(ru.COUNT, res)

    if command == 5:
        catalog = input(ru.CATALOG_NAME)

        if catalog == '':
            res = count_files(os.getcwd())
        else:
            res = count_files(catalog)

        if res == -1:
            print('PermissionError')
        elif res == -2:
            print('FileNotFoundError')
        else:
            print(ru.BITES, res)

    if command == 6:
        aim = input(ru.FILE_NAME)
        print(findFiles(os.getcwd(), aim))
    if command == 7:
        return None


def main():
    while True:
        QUIT = 7
        print(os.getcwd())
        print(ru.MENU)
        command = acceptCommand()
        run_command(command)
        print()
        if command == QUIT:
            print('Работа программы завершена.')
            break


if __name__ == '__main__':
    main()
