def powerset(array):
	subsets=[[]]
	for val in array:
		for i in range(len(subsets)):
			currentsubset = subsets[i]
			subsets.append(currentsubset + [val])
	return subsets