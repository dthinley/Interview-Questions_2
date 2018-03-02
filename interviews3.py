def question3(G):
    if type(G) != dict:
        return 'Error: Input is not a dictionary'

    # get a set of vertices
    keys = G.keys()

    # get unique set of edges
    edges = set()
    for i in keys:
        for j in G[i]:
            if i > j[0]:
                edges.add((j[1], j[0], i))
            elif i < j[0]:
                edges.add((j[1], i, j[0]))

    # sort the edges by weight and make it a list
    edges = sorted(list(edges))

    # loop through the edges and store the needed edges 
    output_edges = []
    keys = [set(i) for i in keys]
    for i in edges:
        # get indices of both keys
        for j in range(len(keys)):
            if i[1] in keys[j]:
                i1 = j
            if i[2] in keys[j]:
                i2 = j

        # store union in the smaller index and pop the larger index
        # also store the edge in output_edges
        if i1 < i2:
            keys[i1] = set.union(keys[i1], keys[i2])
            keys.pop(i2)
            output_edges.append(i)
        if i1 > i2:
            keys[i2] = set.union(keys[i1], keys[i2])
            keys.pop(i1)
            output_edges.append(i)

        # if all vertices are in one graph, terminate
        if len(keys) == 1:
            break
            
    # generate the ouput graph from output_edges
    output_graph = {}
    for i in output_edges:
        if i[1] in output_graph:
            output_graph[i[1]].append((i[2], i[0]))
        else:
            output_graph[i[1]] = [(i[2], i[0])]

        if i[2] in output_graph:
            output_graph[i[2]].append((i[1], i[0]))
        else:
            output_graph[i[2]] = [(i[1], i[0])]
            
    return output_graph

def test3():
    print "Test Case 1 - Edge Case"
    print "Input - not dictionary"
    print "Output - "+str(question3(123))
    
    print "Test Case 2 - Edge Case"
    print "Input - not enogh edges"
    print "Output - "+str(question3({}))
    
    G = {'A': [('B', 1), ('C', 7)],
     'B': [('A', 1), ('C', 5), ('D', 3), ('E', 4)],
     'C': [('A', 7), ('B', 5), ('D', 6)],
     'D': [('B', 3), ('C', 6), ('E', 2)],
     'E': [('B', 4), ('D', 2)],
    }
    
    print "Test Case 3"
    print "Input - G"
    print "Output - "+str(question3(G))
    
    G = {'A': [('B', 1), ('C', 1)],
     'B': [('A', 1), ('C', 1)],
     'C': [('A', 1), ('B', 1)],
    }
    
test3()
