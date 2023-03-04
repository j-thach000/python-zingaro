# todo
# [x] take input
# [x] process input
# [x] print output (number of questions student gets correct)

n = int(input())

student_response = ''
answer_key = ''

total_correct = 0

# student responses
for i in range(n):
	student_response += input()
	
# answer key
for i in range(n):
	answer_key += input()

# check student responses against answer key
for i in range(len(student_response)):
	if student_response[i] == answer_key[i]:
		total_correct += 1		

print(total_correct)
