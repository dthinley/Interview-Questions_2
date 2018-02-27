def question3(G):
    
    # make sure G is dictionary
    
    if type(G) != dict:
        return "Error: G is not dictionary!"

    # G have more than one node
    
    if len(G) < 2:
        return "Error: G has not enough vertices to form edges!"

    # get a set of vertices
    
    vertices = G.keys()

    # get unique set of edges
    
    edges = set()
    for i in vertices:
        for j in G[i]:
            if i > j[0]:
                edges.add((j[1], j[0], i))
            elif i < j[0]:
                edges.add((j[1], i, j[0]))

    # sort edges by weight
    
    edges = sorted(list(edges))

    # loop through edges and store only the needed ones
    
    output_edges = []
    vertices = [set(i) for i in vertices]
    for i in edges:
        # get indices of both vertices
        for j in xrange(len(vertices)):
            if i[1] in vertices[j]:
                i1 = j
            if i[2] in vertices[j]:
                i2 = j

        # store union in the smaller index and pop the larger index
        # also store the edge in output_edges
        
        if i1 < i2:
            vertices[i1] = set.union(vertices[i1], vertices[i2])
            vertices.pop(i2)
            output_edges.append(i)
        if i1 > i2:
            vertices[i2] = set.union(vertices[i1], vertices[i2])
            vertices.pop(i1)
            output_edges.append(i)

        # terminate early when all vertices are in one graph
        
        if len(vertices) == 1:
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
    G = {'A': [('B', 2)],
         'B': [('A', 2), ('C', 5)],
         'C': [('B', 5)]}
    print ("\nTesting 3")
    print ("Edge case (not dictionary):", "Pass" if "Error: G is not dictionary!" == question3(123) else "Fail")
    print ("Edge case (empty dictionary):", "Pass" if "Error: G has not enough vertices to form edges!" == question3({}) else "Fail")
    print ("Case (example case):", "Pass" if G == question3(G) else "Fail")
    G = {'A': [('B', 7), ('D', 5)],
         'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
         'C': [('B', 8), ('E', 5)],
         'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
         'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
         'F': [('D', 6), ('E', 8), ('G', 11)],
         'G': [('E', 9), ('F', 11)]}
    H = {'A': [('D', 5), ('B', 7)],
         'B': [('A', 7), ('E', 7)],
         'C': [('E', 5)],
         'D': [('A', 5), ('F', 6)],
         'E': [('C', 5), ('B', 7), ('G', 9)],
         'F': [('D', 6)],
         'G': [('E', 9)]}
    print ("Case (Wikipedia example):", "Pass" if H == question3(G) else "Fail")
