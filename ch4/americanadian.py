# todo
# [x] take input
# [x] process input
# [x] print output

# read a line of input from user
# check if the spelling of the word is american or canadian
# echo back the canadian spelling if the word is american
# echo back the same word if it is canadian
# terminate when the user types quit!

word = ''
while word != 'quit!':
	word = input()
	if (len(word) > 4 and
	word[-3] != 'a' and
	word[-3] != 'e' and
	word[-3] != 'i' and
	word[-3] != 'o' and
	word[-3] != 'u' and
	word[-3] != 'y' and
	word[-2:] == 'or'):
		word = word[:-2] + 'our'
		print(word)

	else:
		if word == 'quit!':
			break
		print(word)
	