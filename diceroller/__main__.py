from sys import argv, stderr, exit
from . import Roll

"""
CLI application to execute a diceroller expression.
Usage: python -m diceroller <expr>
The app prints the result in total as well as the natural roll and the modifier.
"""

if len(argv) < 2:
    print(f"Missing expression.\nUsage: python {argv[0]} <expr>\n", file=stderr)
    exit(1)

print(f'{Roll(argv[1]):f}')
