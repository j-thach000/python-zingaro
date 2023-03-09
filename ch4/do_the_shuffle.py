# todo
# [x] take input (alternating lines of which button # was pressed and the # of times it was pressed)
# [x] process input
# [x] print output

songs = 'ABCDE'

button = 0
while button != 4:
	# read button (just store it)
	# read number of presses (just store it)
	# process button presses (for range loop to iterate each time it was pressed)
	button = int(input())
	button_presses = int(input())
	for i in range(button_presses):
		if button == 1:
			songs = songs[1:] + songs[0]
		elif button == 2:
			songs = songs[-1] + songs[:-1]
		elif button == 3:
			songs = songs[1] + songs[0] + songs[2:]

output = ''
for song in songs:
	output = output + song + ' '

print(output[:-1])