
import numpy as np

#raw = open("inputs/1t.txt","r").read()
raw = open("inputs/1.txt","r").read()
input_array = [[int(item) for item in string.split('\n')] for string in raw.split('\n\n')[:]]

print("Answer Part 1:", max([sum(element) for element in input_array]))
print("Answer Part 2:", sum(sorted([sum(element) for element in input_array],)[-3:]))
