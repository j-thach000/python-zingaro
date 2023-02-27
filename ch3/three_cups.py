# TODO
# [x] take input (series of  <= 50 characters on one line)
# [x] process input (process the corresponding moves to each character and track the ball location)
# [x] print output (integer 1/2/3 corresponding to the left middle and right cup

swap_sequence = input()
ball_position = 1

# for loop to run through the whole sequence and performance an action based on the char
for swap_type in swap_sequence:
	# A swaps
	if swap_type == 'A' and ball_position == 1:
		ball_position = 2
	elif swap_type == 'A' and ball_position == 2:
		ball_position = 1

	# B swaps
	elif swap_type == 'B' and ball_position == 2:
		ball_position = 3
	elif swap_type == 'B' and ball_position == 3:
		ball_position = 2

	# C swaps
	elif swap_type == 'C' and ball_position == 3:
		ball_position = 1
	elif swap_type == 'C' and ball_position == 1:
		ball_position = 3

print(ball_position)