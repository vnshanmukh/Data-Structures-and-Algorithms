def mergeOverlappingIntervals(intervals):
	sortedintervals = sorted(intervals)
	
	MergedIntervals = []
	currentinterval = sortedintervals[0]
	MergedIntervals.append(currentinterval)
	
	
	for nextinterval in sortedintervals:
		_, currentintervalend = currentinterval
		nextintervalstart,nextintervalend = nextinterval
		
		if currentintervalend >=  nextintervalstart:
			currentinterval[1] = max(currentintervalend,nextintervalend)
		else:
			currentinterval = nextinterval
			MergedIntervals.append(currentinterval)
	return MergedIntervals