def subarraySort(array):
	minoutoforder =float('inf')
	maxoutoforder = float('-inf')
	for i in range(len(array)):
		num = array[i]
		if isoutoforder(i,num,array):
			minoutoforder = min(minoutoforder,num)
			maxoutoforder = max(maxoutoforder,num)
	if minoutoforder == float('inf'):
		return [-1,-1]
	leftindex = 0
	while minoutoforder >= array[leftindex]:
		leftindex +=1
	rightindex = len(array) -1 
	while maxoutoforder <= array[rightindex]:
		rightindex -=1
	return [leftindex,rightindex]
def isoutoforder(i,num,array):
	if i == 0:
		return num  > array[i+1]
	if i == len(array)-1:
		return num < array[i-1]
	return num > array[i+1] or num < array[i-1]