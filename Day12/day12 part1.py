values = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
position = 0

def copy(string_param):
	if string_param.isdigit():
		return int(string_param)
	else:
		return values[string_param]

with open('input.txt', 'r') as file:
	lines = [line.rstrip('\n') for line in file]

while position < len(lines):
	line = lines[position]
	params = line[4:].split()
	
	if line.startswith('inc'):
		values[params[0]] += 1
		position += 1
	elif line.startswith('dec'):
		values[params[0]] -= 1
		position += 1
	elif line.startswith('jnz'):
		if (params[0].isdigit() and int(params[0]) != 0) or (values[params[0]] != 0):
			position = position + int(params[1])
		else:
			position += 1
	else:
		values[params[1]] = copy(params[0])
		position += 1


print(values)