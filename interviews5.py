def findChildren(n):
	children = []
	x = 0
	for each in n:
		if each == 1:
			children.append(x)
		x +=1 
	return children
print("findChildren: "+str(findChildren([0,0,1,1])))

def findRight(n):
	children = findChildren(n)
	return children[-1]

def findLeft(n):
	children = findChildren(n)
	return children[0]

print("Find Right: "+ str(findRight([0,0,1,1])))
print("Find Left: "+ str(findLeft([0,0,1,1])))

def question4(m, r, n1, n2):
	nodeIndex = r
	root = m[nodeIndex]
	# make sure n1 and n2 are integers
	if type(n1) != int:
		return "n1 not int"
	if type(n2) != int:
		return "n2 not int"
	#Traverse tree starting at root
	current_node = root
	print("Node: "+str(current_node))
	while findLeft(current_node) != None or findRight(current_node) != None: 
		try:
			# if the current node is greater than both n1 and n2, go left
			if nodeIndex > n1 and nodeIndex > n2:
				nodeIndex = findLeft(current_node)
				current_node = m[nodeIndex]
			# if the current node is less than both n1 and n2, go left
			elif nodeIndex < n1 and nodeIndex < n2:
				nodeIndex = findRight(current_node)
				current_node = m[nodeIndex]
			# If the current node is between n1 and n2, the current node is the lca
			else:
				return nodeIndex
		except:
			break
	return nodeIndex
####Chain together node objects to construct a tree for test purposes

def test4():
	print("Q4 Test 1: LCA is root (should return 3)"+"\n"+str(question4([[0, 1, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[1, 0, 0, 0, 1],
		[0, 0, 0, 0, 0]],
		3,
		1,
		4)))

	print("Q4 Test 2: LCA is left of root (should return 2) "+"\n"+str(question4([
		[0,0,0,0,0,0],
		[1,0,0,0,0,0],
		[0,1,0,1,0,0],
		[0,0,0,0,0,0],
		[0,0,1,0,0,1],
		[0,0,0,0,0,0]],
		4,
		1,
		3)))

	print("Q4 Test 3: LCA is right of root (should return 4): "+"\n"+str(question4([
		[0,0,0,0,0,0],
		[1,0,0,0,0,0],
		[0,0,0,0,0,0],
		[0,1,0,0,1,0],
		[0,0,1,0,0,1],
		[0,0,0,0,0,0]
		],
		3,
		4,
		5)))

test4()
