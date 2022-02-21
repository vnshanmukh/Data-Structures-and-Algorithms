class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
	previousnode,currentnode = None,head
	while currentnode is not None:
		nextnode = currentnode.next
		currentnode.next = previousnode
		previousnode = currentnode
		currentnode = nextnode
	return previousnode

