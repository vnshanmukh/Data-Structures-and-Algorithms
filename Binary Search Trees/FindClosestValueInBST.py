def findClosestValueInBst(tree, target):
	return helperfunc(tree,target,float("inf"))
def helperfunc(tree,target,closest):
	if tree is None:
		return closest
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	if target < tree.value:
		return helperfunc(tree.left, target,closest)
	elif target > tree.value:
		return helperfunc(tree.right, target, closest)
	else:
		return closest
    
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
