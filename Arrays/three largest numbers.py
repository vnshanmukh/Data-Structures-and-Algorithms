def findThreeLargestNumbers(array):
	for i in range(1,len(array)):
		j = i
		while j > 0 and array[j] < array[j-1]:
			swap(j,j-1,array)
			j = j-1
	return array[len(array)-3:]
def swap(i,j,array):
	array[i],array[j]=array[j],array[i]
    