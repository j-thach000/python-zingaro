# todo
# [x] take input (string)
# [x] process input
# [x] print output

word = input()

honi = 0
h_count = 0
o_count = 0
n_count = 0
i_count = 0

for char in word:
	if (char == 'H' and h_count == 0 and o_count == 0 and n_count == 0 and i_count == 0):
		h_count = 1
	elif (char == 'O' and o_count == 0 and h_count == 1 and n_count == 0 and i_count == 0):
		o_count = 1
	elif (char == 'N' and n_count == 0 and h_count == 1 and o_count == 1 and i_count == 0):
		n_count = 1
	elif (char == 'I' and i_count == 0 and h_count == 1 and o_count == 1 and n_count == 1):
		i_count = 1
	if (h_count == 1 and o_count == 1 and n_count == 1 and i_count == 1):
		honi += 1
		h_count = 0
		o_count = 0
		n_count = 0
		i_count = 0

print(honi)