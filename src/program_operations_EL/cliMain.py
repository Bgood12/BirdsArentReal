import sys
from src.program_operations_EL.commandParser import *


print("type 'help' to view commands")
for line in sys.stdin:
    if 'quit' == line.rstrip():
        break
    else:
        parseInput(line)
print("Program exited")
"""
print("type 'help' to view commands")
running = True
while running:
    line = input(">> ")
    if 'quit' == line.rstrip():
        running = False
    else:
        parseInput(line)
"""