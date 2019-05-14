def merge(L,R):

	lsz = len(L)
	rsz = len(R)

	i = j = 0
	res = []
	while i < lsz and j < rsz:
		if L[i] < R[j]:
			res.append(L[i])
			i += 1
		elif L[i] > R[j]:
			res.append(R[j])
			j += 1
		else:
			res.append(L[i])
			i += 1
			j += 1

	while i < lsz:
		res.append(L[i])
		i += 1
	while j < rsz:
		res.append(R[j])
		j += 1

	#print('merged :' + str(res))
	return res

def msort(A):
	#print('splitting: ' + str(A))
	if len(A) <= 1:
		return A

	m = len(A) // 2

	l, r = A[0:m], A[m:]
	l = msort(l)
	r = msort(r)

	print('merging ' + str(l) + ':' + str(r))
	return merge(l, r)

X = [9,3,6,1]
Y = [8,5,2,7]

C = [9,3,6,1,8,5,2,7]

print(msort(C))