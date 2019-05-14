def consec_sum(tar):

	res = []
	for i in range(1, tar):
		num = tar
		j = i
		temp = []
		while num - j >= 0:
			num -= j
			temp.append(j)
			j += 1

		if num == 0:
			res.append(temp)

	return res


while True:
	n = int(input('Enter num: '))
	if (int(n) == 0):
		break
	res = consec_sum(n)
	if (res):
		for x in res:
			print(x)

