def isGraph(g):
	if type(g) != dict:
		#print("input is not dict")
		return False
	else:
		for key in g:
			if type(key) is not int:
				return False
			if isinstance(type(g[key]), list):
				return False
			else:
				for i in range(0, len(g[key])):
					if type(g[key][i]) is not tuple:
						return False
	return True

##a nice, reasonably complex graph to test with. Source http://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/
graph1 = {
    0:[(1,4),(7,8)],
    1:[(2,8),(0,4),(7,11)],
    2:[(1,8),(3,7),(5,4),(8,2)],
    3:[(2,7),(5,14),(4,9)],
    4:[(3,9),(5,10)],
    5:[(4,10),(3,14),(2,4),(6,2)],
    6:[(8,6),(5,2),(7,1)],
    7:[(6,1),(8,7),(1,11),(0,8)],
    8:[(7,7),(6,6),(2,2)]
}

graph1MST = {
    0:[(1,4),(7,8)],
    1:[(0,4)],
    2:[(3,7),(5,4),(8,2)],
    3:[(2,7),(4,9)],
    4:[(3,9)],
    5:[(2,4),(6,2)],
    6:[(5,2),(7,1)],
    7:[(6,1),(0,8)],
    8:[(2,2)]
}

graph2 = {1: [(2, 2)],
 1: [(1, 2), (3, 5)], 
 3: [(2, 5)]}

graph2MST = {1: [(2, 2)],
 1: [(1, 2), (3, 5)], 
 3: [(2, 5)]}
