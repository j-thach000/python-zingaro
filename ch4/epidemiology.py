# todo
# [x] take input
# [x] process input
# [x] print output (output the day that has a greater number of infected than our goal)

# inputs
target_infected = int(input())
current_infected = int(input())
infection_rate = int(input())

day = 0
total_infected = current_infected

while total_infected <= target_infected:
	day += 1
	current_infected *= infection_rate
	total_infected += current_infected
	
print(day)



