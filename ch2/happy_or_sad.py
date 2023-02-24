message = input()
happy_total = message.count(':-)')
sad_total = message.count(':-(')

if happy_total > sad_total:
	print('happy')
elif sad_total > happy_total:
	print('sad')
elif (sad_total >= 1 and happy_total >= 1) and (sad_total == happy_total):
	print('unsure')
else:
	print('none')