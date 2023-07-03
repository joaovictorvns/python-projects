import sys

for i in range(16):
    for j in range(16):
        n = i*16+j
        sys.stdout.write(f'\u001b[48;5;{n}m {n:<4}')
    sys.stdout.write('\u001b[0m\n')
sys.stdout.flush()