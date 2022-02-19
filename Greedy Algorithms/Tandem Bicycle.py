def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort()
	if fastest == False:
		reversearray(redShirtSpeeds)
	totalspeed =0
	for i in range(len(redShirtSpeeds)):
		rider1 = redShirtSpeeds[i]
		rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - i -1]
		totalspeed += max(rider1,rider2)
	return totalspeed
def reversearray(array):
	start = 0
	end = len(array)-1
	while start < end:
		array[start],array[end]= array[end],array[start]
		start+=1
		end-=1
