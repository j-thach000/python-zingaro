# todo
# [x] take input
# [x] process input
# [x] print output

month = int(input())
day = int(input())

# date occurs before 2/18: Before
# date occurs after 2/18: After
# date occurs on 2/18: Special

# cases involving february
if (month == 2) and (day == 18):
	print('Special')
elif (month == 2) and (day < 18):
	print ('Before')
elif (month == 2) and (day > 18):
	print ('After')

# cases involving non-february months
elif (month < 2):
	print ('Before')
elif (month > 2):
	print ('After')