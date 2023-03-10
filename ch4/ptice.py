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

# incorrect logic for getting just the necessary amount of sequence characters for each boy
# still works but still the wrong logic lol
# sequence_adrian = 'ABC' * n_questions
# correct_adrian = 0

# sequence_bruno = 'BABC' * n_questions
# correct_bruno = 0

# sequence_goran = 'CCAABB' * n_questions
# correct_goran = 0

adrian = 'ABC'
bruno = 'BABC'
goran = 'CCAABB'
correct_adrian = 0
correct_bruno = 0
correct_goran = 0

# changed range from n_questions to len(exam_questions) for clearer intention of comparing 
# the string of exam answers to each boy's sequence
for i in range(len(exam_answers)):
	if adrian[i % len(adrian)] == exam_answers[i]:
		correct_adrian += 1
	if bruno[i % len(bruno)] == exam_answers[i]:
		correct_bruno += 1
	if goran[i % len(goran)] == exam_answers[i]:
		correct_goran += 1

most_correct = max(correct_adrian, correct_bruno, correct_goran)
print(most_correct)
if correct_adrian == most_correct:
	print('Adrian')
if correct_bruno == most_correct:
	print('Bruno')
if correct_goran == most_correct:
	print('Goran')
