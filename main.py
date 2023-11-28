import os


def runCommand(command):
    pass


def countFiles(path):
    pass


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
