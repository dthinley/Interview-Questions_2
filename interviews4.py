class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

def question4(T, r, n1, n2):

	# Build a tree from the matrix
	bst = build_tree(T, r)

	return lca(bst.root, n1, n2)

# Lowest Common Ancestor
def lca(N, n1, n2):
	if not N:
		return None

	cur_node = N

	if cur_node.value > max(n1, n2):
		return lca(cur_node.left, n1, n2)
	elif cur_node.value < min(n1, n2):
		return lca(cur_node.right, n1, n2)
	else:
		return cur_node.value

def build_tree(T, r):
	tree = BinaryTree(r)
	insert_node(T, tree.root)

	return tree

def insert_node(T, node):
	stack = [node]
	while (stack):
		new_node = None
		#print node.value
		for index, e in enumerate(T[node.value]):
			#print e, index
			if e and index < node.value:
				new_node = node.left = Node(index)
				stack.append(node.left)

				insert_node(T, node.left)


			elif e and index > node.value:
				new_node = node.right = Node(index)
				stack.append(node.right)

				insert_node(T, node.right)

		return new_node
		stack.pop()
	return None



def test_question4():
	print ("Result for Question 4:")
	print (question4([[0, 1, 0, 0, 0],
	                 [0, 0, 0, 0, 0],
	                 [0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 1],
                     [0, 0, 0, 0, 0]],
                    3,
                    1,
                    4))
	
	print ('Testing BST with LST to the right of root')
	print (question4([[0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]],
                    3,
                    4,
                    6))

	print ('Testing BST with LST to the left of root')
	print (question4([[0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]],
                    3,
                    0,
                    1))

test_question4()
