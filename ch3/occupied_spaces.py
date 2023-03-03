# todo
# [x] take input (1: n parking spaces, 2: n characters, 3: n characters)
# [x] process input
# [x] print output

parking_spaces = int(input())
yesterday = input()
today = input()

occupied = 0

for index in range(len(yesterday)):
	if yesterday[index] == 'C' and  today[index] == 'C':
		occupied += 1

print(occupied)