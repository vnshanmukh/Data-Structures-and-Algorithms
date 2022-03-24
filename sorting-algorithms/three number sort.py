def threeNumberSort(array, order):
	valuecount = [0,0,0]
	for i in array:
		orderidx = order.index(i)
		valuecount[orderidx]+=1
	for i in range(3):
		value = order[i]
		count = valuecount[i]
		numelementsbefor = sum(valuecount[:i])
		for n in range(count):
			currentidx = numelementsbefor + n
			array[currentidx] = value
	return array