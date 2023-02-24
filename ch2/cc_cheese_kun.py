# todo
# [x] take input (integer, width of her pizza / integer, % of the pizza covered in cheese)
# [x] process input 
#	- absolutely: width 3 and cheesiness of >= 95%
#	- fairly: width 1 and cheesiness of <= 50%
#	- very: anything else
# [x] print output (string explaining how satisfied she is with her pizza)

width = int(input())
cheesiness = int(input())

if (width == 3) and (cheesiness >= 95):
	satisfaction_level = 'absolutely'
elif (width == 1) and (cheesiness <= 50):
	satisfaction_level = 'fairly'
else:
	satisfaction_level = 'very'

print('C.C. is ' + satisfaction_level + ' satisfied with her pizza.')