def question4(T, r, n1, n2):
  if not T or r is None or n1 is None or n2 is None:
    return None
  # if n1 and n2 are on oposite sides from the root
  if (n1 <= r and n2 >= r) or (n1 >= r and n2 <= r):
    return r
  if n1 == n2:
    return n1

  # n2 should be the most distant from the root
  if abs(n2 - r) < abs(n1 - r):
    aux = n1
    n1 = n2
    n2 = aux

  # go up from n2 until the value crosses n1 
  lca = n2
  n2 = get_parent(T, lca)
  while abs(n2 - r) > abs(n1 - r):
    lca = n2
    n2 = get_parent(T, lca)
    
  return lca

""" Returns the parent of the specified node or None if it does not have one """
def get_parent(T, n):
  for idx, row in enumerate(T):
    if row[n] == 1:
      return idx
  return None

# Test Case 1
T = [[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]]
print (question4(T,3,1,4))

# Test Case 2
T1 = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,1],[0,1,0,1,0,0,0,0,0],
     [1,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
     [0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0]]
print (question4(T1,2,5,3))


