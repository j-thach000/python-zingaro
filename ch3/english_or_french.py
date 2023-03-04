# todo
# [x] take input (N characters, followed by N lines of text)
# [x] process input 
# [x] print output

# t > s = english
# s > t = french
# t = s = french

n = int(input())

s = 0
t = 0

for i in range(n):
	string_input = input()
	for char in string_input:
		if char == 's' or char == 'S':
			s += 1
		elif char == 't' or char == 'T':
			t += 1  

if t > s: print('English')
elif s > t: print('French')
else: print('French')
