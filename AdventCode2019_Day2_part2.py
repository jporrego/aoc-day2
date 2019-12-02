import itertools
from itertools import combinations_with_replacement
# Gets data from .txt file and updates some values according to the puzzle
input_data = list(open("Day2_input.txt"))
input_data = input_data[0].split(",")
intcode = []
for char in input_data:
	intcode.append(int(char))


def reset_intcode():
	intcode.clear()
	for char in input_data:
		intcode.append(int(char))


def computer():
	i = 0
	while intcode[i] != 99 and 99 in intcode:
		if intcode[i] == 1:
			intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
			i += 4
		if intcode[i] == 2:
			intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
			i += 4
	return intcode[0]

noun_verb = list(itertools.combinations_with_replacement(range(0,100), 2))

i = 0
while intcode[0] != 19690720:
	reset_intcode()
	intcode[1], intcode[2] = noun_verb[i]
	computer()
	 
	if intcode[0] != 19690720:
		reset_intcode()
		intcode[2], intcode[1] = noun_verb[i]
		computer()
	
	i += 1





print(intcode[0:3])
