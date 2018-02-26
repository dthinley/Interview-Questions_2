#### 1.	Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a boolean True or False.

#### Solution: 
##### *An anagram of a string is another string that contains same characters, only the order of characters can be different. For example, “abcd” and “dabc” are anagram of each other.*

In this question, we can check whether two strings are anagram by checking the count of all characters in both string. If all counts are the same, then the two strings are anagram. The function iterates through substrings of s with length len(t) and performs the anagram test until an anagram is found, in which case the function returns true. If the function reaches the end of s without finding an anagram, it returns false.

Refer: [answer1.py](https://github.com/dthinley/Interview-Questions_2/blob/master/interview1.py).

#### 2.	Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2 (a), and return a string.

#### Solution: 
The solution checks whether each substring of string (a) is a palindrome and records the current longest. The outer for-loop for i in range(len(a)) and inner for-loop for j in range(0, i) takes time complexity of O(n2). The only space needed is to record the current substring and the current longest substring thus the sapce complexity is O(1).

Refer: [answer2.py](https://github.com/dthinley/Interview-Questions_2/blob/master/interviews2.py).

#### 3.	Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:
{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
#### Vertices are represented as unique strings. The function definition should be question3(G)

#### Solution:  
Kruskal’s Algorithm builds the spanning tree by adding edges one by one into a growing spanning tree. Kruskal's algorithm follows greedy approach as in each iteration it finds an edge which has least weight and add it to the growing spanning tree.

Algorithm Steps:
1. *Sort the graph edges with respect to their weights.
2. *Start adding edges to the MST from the edge with the smallest weight until the edge of the largest weight.
3. *Only add edges which doesn't form a cycle , edges which connect only disconnected components.
4. *So now the question is how to check if 2 vertices are connected or not ?

This could be done using DFS which starts from the first vertex, then check if the second vertex is visited or not. But DFS will make time complexity large as it has an order of O(V+E) where V is the number of vertices, E is the number of edges. So the best solution is "Disjoint Sets": 

Disjoint sets are sets whose intersection is the empty set so it means that they don't have any element in common.

#### 4.	Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case might be
question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.

#### Solution: 
This solution represents the bst as a series of nodes with values, and left/right nodes which are initialized to None. A bst is then created by stringing together node objects and assigning left and right values. Starting at the root, the question4 function checks each node to see if the value is higher or lower than both input nodes. If value is higher than both, the function proceeds to the left node, if lower the right. If the node's value is between the values of node1 and node2, then that node is the lca of node1 and node2

Because this algorithm only needs to visit one node per level of the tree, the runtime complexity is proportional to the height of the tree, i.e. O(log(n)). Because we have to store the tree, the space complexity is O(n).

#### 5.	Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a node in the linked list. Return the value of the node at that position.
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

Solution: The findLength helper function iterates through the linked list, incrementing a counter, until the current node has no "next" value, returning the counter. The question5 function iterates through the linked list, incrementing a counter, until the counter value reaches lengthList - m - 1, returning the current node.

Because the function iterates through the linked list, the time complexity is O(n). Because we only have to store the current node and the counter value at any given time, the space complexity is O(1).


