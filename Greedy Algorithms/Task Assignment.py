def taskAssignment(k, tasks):
	pairedtasks =[]
	sortedtasks = sorted(tasks)
	indices = getindices(tasks)
	for i in range(k):
		task1duration = sortedtasks[i]
		indiceswithtask1duration = indices[task1duration]
		task1index = indiceswithtask1duration.pop()
		
		task2sortedindex = len(tasks) -1 -i
		task2duration = sortedtasks[task2sortedindex]
		indiceswithtask2duration = indices[task2duration]
		task2index = indiceswithtask2duration.pop()
		
		pairedtasks.append([task1index,task2index])
	return pairedtasks
def getindices(tasks):
	indices = {}
	for i,taskduration in enumerate(tasks):
		if taskduration in indices:
			indices[taskduration].append(i)
		else:
			indices[taskduration] =[i]
    return indices
