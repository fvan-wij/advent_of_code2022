#P2

crateRow =	([['S', 'Z', 'P', 'D', 'L', 'B', 'F', 'C'], 
['N', 'V', 'G', 'P', 'H', 'W', 'B'],
['F', 'W', 'B', 'J', 'G'],
['G', 'J', 'N', 'F', 'L', 'W', 'C', 'S'],
['W', 'J', 'L', 'T', 'P', 'M', 'S', 'H'],
['B', 'C', 'W', 'G', 'F', 'S'],
['H', 'T', 'P', 'M', 'Q', 'B', 'W'],
['F', 'S', 'W', 'T'], 
['N', 'C', 'R']])

#Test case
# crateRow = ([['Z', 'N'], ['M', 'C', 'D'], ['P']])

instructions = []

with open('day_5/input.txt') as f:
	for lineno, line in enumerate(f):
		if lineno > 9:
			instructions.append([int(s) for s in line.split() if s.isdigit()])

# with open('day_5/test.txt') as f:
# 	for lineno, line in enumerate(f):
# 			instructions.append([int(s) for s in line.split() if s.isdigit()])

def move_crate(nOfCrates, sourc, dest):
	x = 0
	temp = []

	temp.append(crateRow[sourc - 1][-nOfCrates:])
	del crateRow[sourc - 1][-nOfCrates:]
	j = len(temp[0])
	while x < j:
		crateRow[dest - 1].append(temp[0][x])
		x += 1

n = [] #n of crates to be moved
src = [] #from source
dst = [] #to destination

for i in range(len(instructions)):
	n.append(instructions[i][0])
	src.append(instructions[i][1])
	dst.append(instructions[i][2])

for j in range(len(instructions)):
	move_crate(n[j], src[j], dst[j])

print(crateRow)
	
# P1 = FWSHSPJWM
# P2 = PWPWHGFZS