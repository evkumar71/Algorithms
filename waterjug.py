def getNewStates(x,y):
	res = []
	"""
	res.append((xmax, y));
	res.append((x, ymax));
	res.append((0,y))
	res.append((x,0))
	res.append((xmax, y-(xmax-x)))
	res.append((x-(ymax-y), ymax))
	res.append((x+y, 0))
	res.append((0, x+y))
	"""

	if x < xmax:
		res.append((xmax, y));	# Fill x

	if y < ymax:
		res.append((x, ymax));	# Fill y

	if x > 0:
		res.append((0,y))		# Empty x

	if y > 0:
		res.append((x,0))		# Empty y

	if (x+y > 0 and x+y >= xmax and y > 0):
		res.append((xmax, y-(xmax-x)))		# Pour x-> y

	if (x+y > 0 and x+y >= ymax and x > 0):
		res.append((x-(ymax-y), ymax))		# Pour y-> x

	if (x+y >0 and x+y <= xmax and y >= 0):
		res.append((x+y, 0))				# Pour all from y-> x

	if (x+y >0 and x+y <= ymax and x >= 0):
		res.append((0, x+y))				# Pour all from x-> y

	return res

def waterjug(x, y, d):
	Q = []
	visited = []

	Q.append((x, y))
	step = 0

	solved = False
	while Q :	# not-empty
		cur = Q.pop(0)
		print('prcessing: ' + str(cur))
		#print('visited:' + str(visited))
		x, y = cur[0], cur[1]

		if cur not in visited:
			visited.append(cur)
			step += 1

		if x == d or y == d or x+y ==d:
			solved = True
			break

		if len(Q) == 0:
			# since cur-st is not the solution,
			# find all new states
			newStates = getNewStates(x,y)
			print('new:' + str(newStates))

			# from cur-state, we can go to 8 different states
			for st in newStates:
				x, y = st[0], st[1]
				if (x,y) not in visited:
					Q.append(st)
					visited.append(st)
					step += 1

				if x == d or y==d or x+y == d:
					solved = True
					break

			#print('new ({}, {})'.format(x, y))

		if solved:
			break

	print('Solved : {} : {}'.format(solved, step))
	for s in visited:
		print(s)
		# check if we reached final state

xmax = 1
ymax = 2
d = 3

waterjug(0, 0, d)