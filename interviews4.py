def question3(g):
	#check that the input is a properly formatted graph adjacency tree
	if not isGraph(g):
		print("The input graph is not properly formatted")
		return False
	#get node set
	nodes = g.keys()
	#get edge set
	edges = set()
	for x in nodes:
		for y in g[x]:
			if x > y[0]:
				edges.add((y[1], y[0], x))
			elif x < y[0]:
				edges.add((y[1], x, y[0]))
	# sort edges
	edges = sorted(list(edges))
	# loop through edges and store only those which do not create cycles with disjoin set/union find algorithm
	mst_edges = []
	x = 0
	nodes = list(nodes)
	for node in nodes:
		nodes[x] = set([node])
		x += 1
	for x in edges:
		# get indices of both nodes
		for y in range(0, len(nodes)):
			if x[1] in nodes[y]:
				x1 = y
			if x[2] in nodes[y]:
				x2 = y
		# Store union in the smaller index and pop the larger. Append edge to mst_edges
		if x1 < x2:
			nodes[x1] = set.union(nodes[x1], nodes[x2])
			nodes.pop(x2)
			mst_edges.append(x)
		if x1 > x2:
			nodes[x2] = set.union(nodes[x1], nodes[x2])
			nodes.pop(x1)
			mst_edges.append(x)
		# break loop when all nodes are in one graph
		if len(nodes) == 1:
			break
	#  put mst in proper format
	mst = {}
	for x in mst_edges:
		if x[1] in mst:
			mst[x[1]].append((x[2], x[0]))
		else:
			mst[x[1]] = [(x[2], x[0])]
		if x[2] in mst:
			mst[x[2]].append((x[1], x[0]))
		else:
			mst[x[2]] = [(x[1], x[0])]
	return mst

def testQ3():
	##Test case 1, input graph with cycles
	for key in list(graph1.keys()):
		for edge in question3(graph1)[key]:
			if edge not in graph1MST[key]:
				print("Q3 Test1 (Graph with cycles): fail")
		else:
			print("Q3 Test 1 (Graph with cycles): pass")
	##Test case 2, input graph with no cycles
	for key in list(graph2.keys()):
		for edge in question3(graph2)[key]:
			if edge not in graph2MST[key]:
				print("Q3 Test2 (Graph without cycles): fail")
		else:
			print("Q3 Test2 (Graph without cycles): pass")
	##Test case 3, non graph input
	if not question3(0):
		print("Q3 Test3 (non-graph input): Pass")
	else:
		print("Q3 Test3 (non-graph input): Fail")
testQ3()
#question3(graph)
