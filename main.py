import os
import ru_local as ru


def run_command(command):
    if command == 1:
        print(*os.listdir())
    if command == 2:
        move_up()
    if command == 3:
        direct = input()
        move_down(direct)
    if command == 4:
        route = input()
        count_files(route)
    if command == 5:
        route = input()
        count_bytes(route)
    if command == 6:
        route = input()
        aim = input()
        find_files(aim, route)


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
        command = accept_command()
        run_command(command)
        if command == QUIT:
            print('Работа программы завершена.')
            break


if __name__ == '__main__':
    main()
