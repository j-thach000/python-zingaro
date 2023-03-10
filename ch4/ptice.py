# todo
# [x] take input
# [x] process input
# [x] print output

# input
n_questions = int(input())
exam_answers = input()

# output
# 1. some logic printing the largest number of correct answers of the three boys
#    account for ties
# 2. print names of those who have the most correct answers

sequence_adrian = 'ABC' * n_questions
correct_adrian = 0

sequence_bruno = 'BABC' * n_questions
correct_bruno = 0

sequence_goran = 'CCAABB' * n_questions
correct_goran = 0

for i in range(n_questions):
	if sequence_adrian[i] == exam_answers[i % len(adrian)]:
		correct_adrian += 1
	if sequence_bruno[i] == exam_answers[i]:
		correct_bruno += 1
	if sequence_goran[i] == exam_answers[i]:
		correct_goran += 1

most_correct = max(correct_adrian, correct_bruno, correct_goran)
print(most_correct)
if correct_adrian == most_correct:
	print('Adrian')
if correct_bruno == most_correct:
	print('Bruno')
if correct_goran == most_correct:
	print('Goran')