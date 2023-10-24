from graph import * 


"""
Construct predecessor dictionary starting from node1 until node2 is found. 
Once node2 is found, construct path by backtracking via predecessors to reach starting node  
"""
def BFS2(G, node1, node2):
    if node1 == node2: return [] # don't bother to search if we are already at the destination
    predecessor_dictionary = dict() 
    finished = False
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while (len(Q) != 0 and not finished) :
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                predecessor_dictionary[node] = current_node
                marked[node] = True
                if node == node2: finished = True

    
    path=[node2]
    node = node2
    while(node != node1):
        if predecessor_dictionary.get(node2) == None: return []
        node = predecessor_dictionary.get(node)
        path.insert(0,node)

    return path



"""
Performs Breadth First Search from node1 to all other reachable nodes
Returns a predecessor dictionary of the reachable nodes
"""
def BFS3(G, node1):

    predecessor_dictionary = dict() 
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                predecessor_dictionary[node] = current_node
                marked[node] = True

    return predecessor_dictionary










