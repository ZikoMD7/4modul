import sys
from pathlib import Path
from colorama import *



def define (current):
    for i in current.iterdir():
        if i.is_dir():
            print(Fore.RED+f'{i}'+Style.RESET_ALL)
            define(i)
        if i.is_file():
            print(Fore.YELLOW+f'{i}'+Style.RESET_ALL)



if __name__ == "__main__":

    if len(sys.argv)<2:
        print(Fore.BLUE + "input path" + Style.RESET_ALL)
        sys.exit(1)
    
    fh = sys.argv[1]
    current = Path(fh)

    if not current.exists():
        print(Fore.RED + "Шлях не знайдено" + Style.RESET_ALL)
        sys.exit(1)

    define(current)