# Gets data from .txt file and updates some values according to the puzzle
input_data = list(open("Day2_input.txt"))
input_data = input_data[0].split(",")
intcode = []
for char in input_data:
	intcode.append(int(char))
intcode[1] = 12
intcode[2] = 2

# Iterates through the intcode and applies the puzzle's logic
i = 0
while intcode[i] != 99 and 99 in intcode:
	if intcode[i] == 1:
		intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
		i += 4
	if intcode[i] == 2:
		intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
		i += 4

print (intcode)
