import random
import time


def get_count_neighbourhood(field, x, y, empty):
	neighbourhood = []
	steps = [
        [x + 1, y],
        [x - 1, y],
        [x, y + 1],
        [x, y - 1],
        [x + 1, y + 1],
        [x - 1, y - 1],
        [x + 1, y - 1],
        [x - 1, y + 1],
    ]

	for item in steps:
		new_x = item[0]
		new_y = item[1]
		if 0 <= new_x < len(field) and 0 <= new_y < len(field):
			if field[new_y][new_x] != empty:
				neighbourhood.append(0)
					
	return len(neighbourhood)


def beautiful_output(matrix):
	numbers = " ".join([str(i) for i in range(len(matrix[0]))])
	print("  "+numbers)
	i = 0
	for item in matrix:
		paste_number = str(i)
		if i < 10:
			paste_number += " " 
		print("{0}|{1}|".format(paste_number, "|".join(item)))
		i+=1

	return

def main():
	size = 5
	cell = '\033[32mo\033[0m'
	empty = 'x'

	field = [[empty for x in range(size)] for y in range(size)]
	next_generation = [[empty for x in range(size)] for y in range(size)]


	# for i in range(100):
	# 	x = random.randint(0, size-1)
	# 	y = random.randint(0, size-1)
	# 	field[y][x] = cell

	field[0][0] = cell
	field[1][0] = cell
	field[0][1] = cell
	field[1][1] = cell
	
	beautiful_output(field)
	generation = 0

	while(generation < 10):
		if generation > 0:
			field = [[next_generation[y][x] for x in range(len(next_generation[y]))] for y in range(len(next_generation)) ]
			next_generation = [[empty for x in range(size)] for y in range(size)]
		for y in range(len(field)):
			for x in range(len(field[0])):
				count_neighbourhood = get_count_neighbourhood(field, x, y, empty)
				if count_neighbourhood < 2 or count_neighbourhood > 3:
					next_generation[y][x] = empty					
				else:
					next_generation[y][x] = cell
					
		generation += 1
		beautiful_output(next_generation)
		time.sleep(1)
	pass

if __name__ == "__main__":
	main()
	pass
			

