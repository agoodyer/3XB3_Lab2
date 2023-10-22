from graph import * 


"""
Using the Predecessor dictionary of BFS3, 
We can start at the end node, and traverse backwards to our start node 
by repetitively following the predecessor of our current node
If no such predecessor exists, there is no path. 
"""
def BFS2(G,node1,node2):
    predecessors = BFS3(G,node1)
    path=[]
    node = node2
    while(node != node1):
        if predecessors.get(node2) == None: return []
        path.insert(0,node)
        node = predecessors.get(node)

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



