def generateDocument(characters, document):
	characterFrequency ={}
	documentFrequency ={}
	for i in characters:
		characterFrequency[i] = characterFrequency.get(i,0)+1
	for i in document:
		documentFrequency[i] = documentFrequency.get(i,0)+1
	for i in documentFrequency:
		if characterFrequency.get(i) is None:
			return False
		elif documentFrequency.get(i) > characterFrequency.get(i):
			return False
	return True