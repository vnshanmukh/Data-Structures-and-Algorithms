def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort(reverse = True)
	blueShirtHeights.sort(reverse = True)
	
	firstrow = "RED" if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
	for i in range(len(redShirtHeights)):
		redShirtHeight = redShirtHeights[i]
		blueShirtHeight = blueShirtHeights[i]
		if firstrow == 'RED':
			if redShirtHeight >= blueShirtHeight:
				return False
		else:
			if blueShirtHeight >= redShirtHeight:
				return False
    return True
