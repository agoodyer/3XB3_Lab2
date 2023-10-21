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


def DFS3(G, node1):
    hasCycle = False
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
        else: 
            hasCycle = True
    print(hasCycle)
    return predecessor_dictionary

