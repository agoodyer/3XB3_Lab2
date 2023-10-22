#DEPTH FIRST SEARCH IMPLEMENTATIONS


def DFS2(G, node1, node2):
    
    path = []
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            path.append(current_node)
            for node in G.adj[current_node]:
                if node == node2:
                    path.append(node)
                    return path
                S.append(node)
    return []



"""
Performs Breadth First Search from node1 to all other reachable nodes
Returns a predecessor dictionary of the reachable nodes
"""
def DFS3(G, node1):

    predecessor_dictionary = dict() 
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0: 
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:

                if not marked[node]:
                    S.append(node)
                    predecessor_dictionary[node] = current_node
    return predecessor_dictionary

