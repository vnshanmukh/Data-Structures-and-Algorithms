#"string": "abcdcaf"
# result : b
# O(n^2) time | O(1) space where n is length of string

def firstNonRepeatingCharacter(string):
    # Write your code here.
	for idx in range(len(string)):
		founddup = False
		for idx2 in range(len(string)):
			if string[idx] == string[idx2] and idx!=idx2:
				founddup = True
				
		if founddup is False:
			return idx
    return -1