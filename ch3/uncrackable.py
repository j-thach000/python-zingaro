# TODO
# [x] take input (a single string)
# [x] process input (requirements for a password)
# [x] print output

# postmortem
# if there were bad inputs potentially 
# i would have to track the total length of the string and then compare
# if string_length == good_characters then the whole string was comprised of
# digits and lowercase/uppercase letters

password = input()

# password requirements
# every character is either a lowercase/uppercase letter or digit

character_length = 0   # [8,12]
lowercase = 0 	      # min 3
uppercase = 0 	      # min 2
digit = 0 	      # min 1

for char in password:
	character_length += 1
	if char.isupper():
		uppercase += 1
	if char.islower():
		lowercase += 1
	if char.isdigit():
		digit += 1

if ((character_length >= 8 and character_length <= 12) and 
	(lowercase >= 3) and (uppercase >= 2) and (digit >= 1)):
	print('Valid')
else:
	print('Invalid')