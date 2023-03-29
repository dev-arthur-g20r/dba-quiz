for number in range(1, 7):
	difference = number
	stair = ""
	while difference > 0:
		stair = stair + f"{number} "
		difference -= 1
	print(stair)