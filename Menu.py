#from termcolor import colored
import msvcrt
import sys, os

# Второй вариант
from colorama import Fore, Back, Style
from colorama import init
init()
class Menu:
    items = []
    selectedItem = 0
    def __init__(self, initItems):
        self.items = initItems

    def changeSItem(self, up):
        if len(self.items) != 0:
            if up:
                if self.selectedItem == len(self.items) - 1:
                    self.selectedItem = 0
                else:
                    self.selectedItem = self.selectedItem + 1
            else:
                if self.selectedItem == 0:
                    self.selectedItem = len(self.items) - 1
                else:
                    self.selectedItem = self.selectedItem - 1

    def printItems(self):
        for i in range(len(self.items)):
            if (i == self.selectedItem):
                print(Fore.RED + self.items[i])
            else:
                print(Fore.WHITE + self.items[i])

def wait_key():
    ''' Wait for a key press on the console and return it. '''
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result


MainMenu = Menu(['Пункт 1', 'Пункт 2', 'Пункт 3', 'Пункт 4'])
MainMenu.printItems()
while True:
    c = wait_key()
    os.system('cls')
    print("Entred key is {}", c)
    print(c == b'w')
    print(c == b's')
    if c == b'w':
        MainMenu.changeSItem(True)
    elif c == b's':
        MainMenu.changeSItem(False)
    MainMenu.printItems()
