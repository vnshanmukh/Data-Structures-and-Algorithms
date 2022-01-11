def spiralTraverse(a):
    # Write your code here.
	res =[]
	startrow,endrow = 0,len(a)-1
	startcol,endcol = 0, len(a[0])-1
	while startrow<=endrow and startcol <= endcol:
		for col in range(startcol,endcol+1):
			res.append(a[startrow][col])
		for row in range(startrow+1,endrow+1):
			res.append(a[row][endcol])
		for col in reversed(range(startcol,endcol)):
			if startrow == endrow:
				break
			res.append(a[endrow][col])
		for row in reversed(range(startrow+1,endrow)):
			if startcol == endcol:
				break
			res.append(a[row][startcol])
		startrow+=1
		startcol +=1
		endrow -=1
		endcol -=1
	return res