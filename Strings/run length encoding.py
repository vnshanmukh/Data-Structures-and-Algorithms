def runLengthEncoding(string):
	encodedstring =[]
	currentrunlength = 1
	
	for i in range(1,len(string)):
		currentchar = string[i]
		previouschar = string[i-1]
		
		if currentchar != previouschar or currentrunlength == 9:
			encodedstring.append(str(currentrunlength))
			encodedstring.append(previouschar)
			currentrunlength =0
		currentrunlength +=1
	encodedstring.append(str(currentrunlength))
	encodedstring.append(string[len(string)-1])
	return "".join(encodedstring)