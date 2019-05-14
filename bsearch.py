def bsearch(a, tar):
	l = 0
	h = len(a)-1
	m = 0
	while l < h:
		m = (l + h) // 2
		if tar < a[m]:
			h = m - 1
		elif tar > a[m]:
			l = m + 1
		else:
			l = m + 1
	print(str(l) + ':' + str(h))

tar = 5
A = [1,2,3,4,5,5,5,6,6,7]
bsearch(A, tar)