# TODO
# [x] take input
# [x] process input
# [x] print output

D1 = int(input())
D2 = int(input())
D3 = int(input())
D4 = int(input())

# condition 1: first of these four digits is an 8 or 9
if D1 == 8 or D1 == 9:
	condition_one = True
else:
	condition_one = False

# condition 2: last digit is an 8 or 9
if D4 == 8 or D4 == 9:
	condition_two = True
else:	condition_two = False

# condition 3: the second and third digits are the same
if D2 == D3:
	condition_three = True
else:
	condition_three = False

# check to answer or ignore
if (condition_one and condition_two) and condition_three:
	print('ignore')
else:
	print('answer')