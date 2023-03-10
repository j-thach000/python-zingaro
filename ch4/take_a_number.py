# todo
# [x] take input
# [x] process input
# [x] print output

next_ticket = int(input())

day_total_late = 0
remaining_in_line = 0
# unnecessary if we implicitly track the total tickets via the next ticket number
# no idea if that's an okay way to think for larger scale programs that might want to uniquely track this
remaining_tickets = 999 - (next_ticket - 1)

state = ''
while state != 'EOF':
	state = input()
	if remaining_tickets == 0: # unnecessary
		remaining_tickets = 999
		next_ticket = 1
	if state == 'TAKE':
		next_ticket += 1
		day_total_late += 1
		remaining_in_line += 1
		remaining_tickets -= 1
	elif state == 'SERVE':
		remaining_in_line -= 1
	elif state == 'CLOSE':
		print(day_total_late, remaining_in_line, next_ticket)
		remaining_in_line = 0
		day_total_late = 0