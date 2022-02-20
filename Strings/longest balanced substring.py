def longestBalancedSubstring(s):
    currentlong = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            sub = s[i:j+1]
            if len(sub) > currentlong and valid(sub):
                currentlong = len(sub)
    return currentlong   
def valid(st):
    d = {"(":")"}
    stack =[]
    for i in st:
        if i == "(":
            stack.append(i)
        if i ==")" and stack == []:
            return False
        if i == ")" and stack[-1] == "(":
            stack.pop()
    return len(stack) == 0