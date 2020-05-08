CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'   # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset
print(CLEAR_SCREEN + RED + 'Welcome!' + RESET + "hello")


import colorama
from colorama import Fore, Back, Style
colorama.init()

# Set the color semi-permanently
print(Fore.CYAN)
print("Text will continue to be cyan")
print("until it is reset or changed")
print(Style.RESET_ALL)

# Colorize a single line and then reset
print(Fore.RED + 'You can colorize a single line.' + Style.RESET_ALL)

# Colorize a single word in the output
print('Or a single ' + Back.GREEN + 'words' + Style.RESET_ALL + ' can be highlighted')

# Combine foreground and background color
print(Fore.BLUE + Back.WHITE)
print('Foreground, background, and styles can be combined')
print("==========            ")

print(Style.RESET_ALL)
print('If unsure, reset everything back to normal.')