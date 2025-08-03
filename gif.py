import os
import sys
import time
import random

try:
    import colorama
    from colorama import Fore, Style
except ImportError:
    print("Install colorama for colors: pip install colorama")
    sys.exit(1)

colorama.init()

WIDTH = 60
HEIGHT = 20
BINARY_CHARS = ['0', '1']
MESSAGE = "I'm watching you"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    columns = [0] * WIDTH  # each column's current Y position

    while True:
        # Build each line of output
        lines = []
        for y in range(HEIGHT):
            line_chars = []
            for x in range(WIDTH):
                # If this row is the "message" row and position matches message start
                msg_start = (WIDTH - len(MESSAGE)) // 2
                if y == HEIGHT // 2 and msg_start <= x < msg_start + len(MESSAGE):
                    line_chars.append(Fore.LIGHTGREEN_EX + MESSAGE[x - msg_start] + Style.RESET_ALL)
                else:
                    # Randomly print '0' or '1' if within falling column range
                    if columns[x] >= y:
                        line_chars.append(Fore.GREEN + random.choice(BINARY_CHARS) + Style.RESET_ALL)
                    else:
                        line_chars.append(' ')
            lines.append("".join(line_chars))

        print("\n".join(lines))
        # Update column positions randomly to simulate falling effect
        for i in range(WIDTH):
            columns[i] = columns[i] + 1 if random.random() > 0.5 else columns[i]
            if columns[i] > HEIGHT:
                columns[i] = 0

        time.sleep(0.1)
        clear_screen()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("Exiting...")

