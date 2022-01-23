def isMonotonic(array):
	ic = True
	de = True
	for i in array:
		if i > i+1 :
			ic = False
		else:
			de = False
		
    return ic || de
