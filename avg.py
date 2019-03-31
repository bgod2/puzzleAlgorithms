



file = open('stats3', 'r')

total = 0
states = 0

with file as f:
	for line in f:
		total += int(line)
		states += 1


print 'states: ' + str(states)
print 'avg: ' + str(total / states)
file.close()