# todo
# [x] take input
# [x] process input
# [x] print output (int representing how long it takes to eat a box of smarties)

# eating smarties by group
# orange > blue > green > yellow > pink > violet > brown > red
# everything else, by the handful (max 7)
# finishes one color before the next
# handful = 7 smarties
# takes 13 seconds for non-red, even if hand is not full, 7
# red smarties = 16 seconds for each individual one
# after sorting the colors, how long does it take to eat all the smarties?

# colors
orange = 0
blue = 0
green = 0
yellow = 0
pink = 0
violet = 0
brown = 0
red = 0

time_to_eat = 0
color = ''

for i in range(10):
	while color != 'end of box':
		color = input()
		if color == 'orange': 
			orange += 1
			if orange == 7:
				time_to_eat += 13
				orange -= 7				
		if color == 'blue': 
			blue += 1
			if blue == 7:
				time_to_eat += 13
				blue -= 7
		if color == 'green': 
			green += 1
			if green == 7:
				time_to_eat += 13
				green -= 7
		if color == 'yellow': 
			yellow += 1
			if yellow == 7:
				time_to_eat += 13
				yellow -= 7
		if color == 'pink': 
			pink += 1
			if pink == 7:
				time_to_eat += 13
				pink -= 7
		if color == 'violet': 
			violet += 1
			if violet == 7:
				time_to_eat += 13
				violet -= 7
		if color == 'brown': 
			brown += 1
			if brown == 7:
				time_to_eat += 13
				brown -= 7
		if color == 'red': 
			red += 1
			if red == 1:
				time_to_eat += 16
				red -= 1			
		if color == 'end of box':
			if orange > 0: 
				time_to_eat += 13
			if blue > 0: 
				time_to_eat += 13
			if green > 0: 
				time_to_eat += 13
			if yellow > 0: 
				time_to_eat += 13
			if pink > 0: 
				time_to_eat += 13
			if violet > 0: 
				time_to_eat += 13
			if brown > 0: 
				time_to_eat += 13		
	print(time_to_eat)
	time_to_eat = 0
	color = ''
	orange = 0
	blue = 0
	green = 0
	yellow = 0
	pink = 0
	violet = 0
	brown = 0
	red = 0