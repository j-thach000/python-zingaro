# todo
# [x] take input
# [x] process input
# [x] print output (who is the current owner of the wand, how many owners did the wand have?)

# uppercase letter, the label of the initial wizard the wand is obeying
current_owner = input()
total_owners = 1
previous_owners = current_owner

# number of duels
duel_count = int(input())

# a string with 2 characters, separated by a space
for i in range(duel_count):
	duel_pairing = input()
	if duel_pairing[2] == current_owner:
		current_owner = duel_pairing[0]
		if previous_owners.count(duel_pairing[0]) == 0:		
			previous_owners += duel_pairing[0]
			total_owners += 1		

print(current_owner)
print(total_owners)
		
	