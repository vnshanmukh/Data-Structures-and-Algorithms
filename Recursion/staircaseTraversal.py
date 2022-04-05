def staircaseTraversal(height, maxsteps):
	return numberofwaystotop(height,maxsteps)
def numberofwaystotop(height,maxsteps):
	if height <=1:
		return 1
	numberofways =0
	for step in range(1,min(maxsteps,height)+1):
		numberofways +=numberofwaystotop(height-step,maxsteps)
	return numberofways
