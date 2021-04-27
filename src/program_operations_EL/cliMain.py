import sys
from src.program_operations_EL.commandParser import *


print("type 'help' to view commands")
for line in sys.stdin:
    if 'quit' == line.rstrip():
        break
    else:
        parseInput(line)
        print("<<Command ('help' to view)>>:")
print("Program exited")