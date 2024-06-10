import os
import sys


def restart():
    os.execv(sys.executable, (sys.executable, *sys.argv))


if __name__ == '__main__':
    print(input("> "))
    if input("Again? ") in "Yy":
        restart()
