# TODO
# take input (6 integers: the types of points scored by each team) 
# process input (calculate how many points were made by each team and decide which is greater)
# print output

A3 = int(input()) * 3
A2 = int(input()) * 2
A1 = int(input()) 
apple_total = A3 + A2 + A1

B3 = int(input()) * 3
B2 = int(input()) * 2
B1 = int(input())
banana_total = B3 + B2 + B1

if apple_total > banana_total:
	print('A')
elif banana_total > apple_total:
	print('B')
else: 
	print('T')
