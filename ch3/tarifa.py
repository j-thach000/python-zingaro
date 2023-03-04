# todo
# [x] take input
# [x] process input
# [x] print output (how many megabytes does he have available for the n+1 month)

# integer x representing the allowance of megabytes per month
monthly_mb = int(input())

# integer n representing the first N months of using the plan
months_used = int(input())

# n lines of megabytes spent per month
excess = 0
for i in range(months_used):
	# process month 
	used = int(input())
	excess = excess + monthly_mb - used

print(excess + monthly_mb)
	
	

