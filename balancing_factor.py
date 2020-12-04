#calculating balancing factor for each node in BST

def factor(node):
	if node is None
		return 0
	elif (left.child is None AND right.child is None)
		return 1
	else 
		return max(height(left.child), height(right.child)) + 1
