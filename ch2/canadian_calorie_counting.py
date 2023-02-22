# TODO
# [x] take input
# [x] process input
# [x] print output

# mistakes
# constantly forgetting to actually print the output
# not constantly checking code while building, instead of building it all and then testing at the very end

choice_burger = int(input())
choice_side = int(input())
choice_drink = int(input())
choice_dessert = int(input())

# burger calories
if choice_burger == 1:
	calories_burger = 461
elif choice_burger == 2:
	calories_burger = 431
elif choice_burger == 3:
	calories_burger = 420
else:
	calories_burger = 0

# side calories
if choice_side == 1:
	calories_side = 100
elif choice_side == 2:
	calories_side = 57
elif choice_side == 3:
	calories_side = 70
else:
	calories_side = 0

# drink calories
if choice_drink == 1:
	calories_drink = 130
elif choice_drink == 2:
	calories_drink = 160
elif choice_drink == 3:
	calories_drink = 118
else:
	calories_drink = 0

# dessert calories
if choice_dessert == 1:
	calories_dessert = 167
elif choice_dessert == 2:
	calories_dessert = 266
elif choice_dessert == 3:
	calories_dessert = 75
else:
	calories_dessert = 0

calories_total = calories_burger + calories_side + calories_drink + calories_dessert
print(f'Your total Calorie count is {calories_total}.')
