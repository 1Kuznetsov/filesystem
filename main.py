import os


def runCommand(command):
    if command == 1:
        return None
    if command == 2:
        return moveUp()
    if command == 3:
        return moveDown(curDir)
    if command == 4:
        return countFiles(pth)
    if command == 5:
        return countBytes(pth)
    if command == 6:
        return findFiles(trgt, pth)


def countFiles(path):
    cnt = 0

    try:
        for item in os.listdir(path):
            new_path = os.path.join(path, item)
            if os.path.isfile(new_path):
                cnt += 1
            elif os.path.isdir(new_path):
                cnt += countFiles(new_path)
        return cnt
    except PermissionError:
        print(None)


def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print('Работа программы завершена.')
            break


if __name__ == '__main__':
    main()
