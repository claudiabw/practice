# advent of code day 2

f = open('day2.txt', 'r')
total = 0


for line in f:
	dimensions_array = line.split('\n')
	dimensions = dimensions_array[0].split('x')
	ints = []
	for elem in dimensions:
		ints.append(int(elem))
	l = ints[0]
	w = ints[1]
	h = ints[2]
	total += 2 * (l*w + w*h + l*h) + min(l*w, w*h, l*h)

print total