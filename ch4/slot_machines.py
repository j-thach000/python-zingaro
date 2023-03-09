# resubmitting to try out using modulo to track cycles

# todo
# [x] take input
# [x] process input (find out how many times Martha has to play with n quarters to go broke)
# [x] print output (string containing n times Martha has to play before going broke)

# n quarters
quarters = int(input())

# times the first/second/third machine had been played prior to Martha
m1 = int(input()) # 30 quarters every 35th play
m2 = int(input()) # 60 quarters every 100th play
m3 = int(input()) # 9 quarters every 10th play

# process input
plays = 0
while quarters >= 1:
	machine = plays % 3    
	quarters -= 1
	if machine == 0:
		m1 += 1
		if m1 % 35 == 0:
			quarters += 30
	elif machine == 1:
		m2 += 1
		if m2 % 100 == 0:
			quarters += 60
	elif machine == 2:
		m3 += 1
		if m3 % 10 == 0:
			quarters += 9

	plays += 1
	
# print output
print(f'Martha plays {plays} times before going broke.')