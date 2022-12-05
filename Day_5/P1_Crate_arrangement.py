crateRow1 = ['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C']
crateRow2 = ['N', 'V', 'G', 'P', 'H', 'W', 'B']
crateRow3 = ['F', 'W', 'B', 'J', 'G']
crateRow4 = ['G', 'J', 'N', 'F', 'L', 'W', 'C', 'S']
crateRow5 = ['W', 'J', 'L', 'T', 'P', 'M', 'S', 'H']
crateRow6 = ['B', 'C', 'W', 'G', 'F', 'S']
crateRow7 = ['H', 'T', 'P', 'M', 'Q', 'B', 'W']
crateRow8 = ['F', 'S', 'W', 'T']
crateRow9 = ['N', 'C', 'R']

instructions = []
with open('day_5/input.txt') as f:
	for lineno, line in enumerate(f):
		if lineno > 9:
			instructions.append([int(s) for s in line.split() if s.isdigit()])

#Store [0] in n
#Store [1] in src
#Store [2] in dst

for i in range(len(instructions)):
	print(instructions[i][0])
		