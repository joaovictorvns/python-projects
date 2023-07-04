import sys
import time

def progress_bar_cli(i_fill: int = 0, c_fill: str = '#', s_side: str = '[]') -> None:
    sys.stdout.write(f'\r{i_fill:>3}% {s_side[0]}{c_fill*i_fill:<100}{s_side[1]}')

if __name__ == '__main__':
    progress_bar_cli()
    for i in range(1, 101):
        time.sleep(0.1)
        progress_bar_cli(i)
    print()