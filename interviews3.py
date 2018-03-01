def question3(G):
    # using Kruskal's algorithm

    if type(G) != dict:
        return 'The input is not a dictionary. Please provide a dictionary.'

    # get the keys/vertices
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

    # loop through the edges and store the edges necessary
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

        # terminate early when all vertices are in one graph
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

# Test Case 
G = {'A':[('B',2)],'B':[('A',2),('C',5)],'C':[('B',5)]}
print (question3(G))

