import os
import ru_local as ru


def acceptCommand():
    while True:
        cmnd = int(input(ru.CHOICE))
        if cmnd > 0 and cmnd < 8:
            return int(cmnd)
        else:
            print(ru.NOT_CHOICE)
# command = acceptCommand()
# print(command)


def moveUp():
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    os.chdir(parent_directory)
    print(ru.CURRENT_DIRECTORY, os.getcwd())


def moveDown(currentDir):
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


def run_command(command):
    if command == 1:
        print(*os.listdir())
    if command == 2:
        moveUp()
    if command == 3:
        direct = os.getcwd()
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
    # print(findFiles('/Users/mariaadreeva/PycharmProjects', 'krivoshapova'))