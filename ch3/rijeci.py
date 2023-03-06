# todo
# [x] take input (integer K representing how many times the button was pressed)
# [x] process input
# [x] print output

# had to read editorial

k = int(input())

a = 1
b = 0

a_new = 0
b_new = 0

for i in range(k):
	b_new = a + b	
	a_new = b
	a = a_new
	b = b_new
			
print(a, b)