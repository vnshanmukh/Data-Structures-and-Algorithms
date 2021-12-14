def longestPalindromicSubstring(string):
	longest = ""
	for i in range(len(string)):
		for j in range(i,len(string)):
			subst = string[i:j+1]
			if len(subst) > len(longest) and ispalindrom(subst):
				longest = subst
	return longest
def ispalindrom(s):
	left = 0
	right = len(s) - 1
	while left < right:
		if s[left] != s[right]:
			return False
		else:
			left +=1
			right-=1
	return True