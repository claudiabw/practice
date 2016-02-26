# advent of code day 1

# Santa's directions: ( = go up one floor, ) = go down one

# make a file with the directions
#f = open('day1.txt', 'r')
#directions = f.read()

# enter the directions via commandline
directions = raw_input("Give Santa Directions! ")

floor = 0

for char in directions:
	if char == '(':
		floor += 1
	elif char == ')':
		floor -= 1

print floor