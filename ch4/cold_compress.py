# todo
# [x] take input
# [x] process input
# [x] print output

# block compressed form: # of times the symbol appears and then the symbol itself

total_lines = int(input())

for i in range(total_lines):
	sequence = input()
	occurrence = 0
	symbol = ''
	output = ''
	for char in sequence:
		if char != symbol and occurrence > 0:
			output += str(occurrence)
			output += ' '
			output += symbol
			output += ' '
			occurrence = 0
			symbol = ''		
		if occurrence == 0 and symbol == '':
			occurrence += 1
			symbol = char
		elif occurrence >= 1 and char == symbol:
			occurrence += 1
	# need to catch the case of the sequence ending
	if occurrence > 0:
			output += str(occurrence)
			output += ' '
			output += symbol
			output += ' '
	print(output[:-1])			