# todo
# [x] take input (3 integers)
# [x] process input (find the median of three values)
# [x] print output

bowl_weight1 = int(input())
bowl_weight2 = int(input())
bowl_weight3 = int(input())

if ((bowl_weight1 > bowl_weight2 and bowl_weight1 < bowl_weight3) or (bowl_weight1 < bowl_weight2 and bowl_weight1 > bowl_weight3)):
	print(bowl_weight1)
elif ((bowl_weight2 > bowl_weight1 and bowl_weight2 < bowl_weight3) or (bowl_weight2 < bowl_weight1 and bowl_weight2 > bowl_weight3)):
	print(bowl_weight2)
else: 
	print(bowl_weight3)