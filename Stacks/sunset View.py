def sunsetViews(buildings, direction):
	buildingswithsunsetview =[]
	startidx = 0 if direction == "WEST" else len(buildings)-1
	step = 1 if direction == "WEST" else -1
	 
	idx = startidx
	runningmaxheight = 0
	while idx >=0 and idx < len(buildings):
		buildingheight = buildings[idx]
		if buildingheight > runningmaxheight:
			buildingswithsunsetview.append(idx)
		runningmaxheight = max(runningmaxheight,buildingheight)
		idx+=step
	if direction == "EAST":
		return buildingswithsunsetview[::-1]
    return buildingswithsunsetview
