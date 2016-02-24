# daily programmer easy challenge 8

bottles = 99

while bottles > 2:
	print '%d bottles of beer on the wall, %d bottles of beer.' \
	' Take one down, pass it around, %d bottles of beer on the wall' % (bottles, bottles, bottles - 1)
	bottles -= 1

print '%d bottles of beer on the wall, %d bottles of beer.' \
	' Take one down, pass it around, %d bottle of beer on the wall' % (bottles, bottles, bottles - 1)

bottles -= 1

print '%d bottle of beer on the wall, %d bottle of beer.' \
	' Take one down, pass it around, no more bottles of beer on the wall' % (bottles, bottles)