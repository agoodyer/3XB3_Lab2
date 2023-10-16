from graph import * 
import  random
import matplotlib.pyplot as plt
import numpy as np 


def generate_random_graph(n,e):
    graph = Graph(n)
    possible_edges = [(i,j) for i in range(n) for j in range(i+1,n)]
    if  e < 0 or e > len(possible_edges) : raise Exception('Illegal Edge Count') 

    for i in range(e):
        edge = possible_edges.pop(random.randint(0,len(possible_edges)-1))  
        graph.add_edge(edge[0], edge[1])  # add e random edges

    return graph



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
                S.append(node)
                print('next node: ',node, 'current node:', current_node  )
                predecessor_dictionary[node] = current_node
        else: 
            hasCycle = True
            print(node, '!')
    print(hasCycle)
    return predecessor_dictionary







#Breadth First Search
def BFS2(G, node1, node2):

    path=[]
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


#Breadth First Search
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

    print(marked)
    return predecessor_dictionary




def is_connected(G):
    node1 = 0
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
                marked[node] = True

    return all(marked.values())



graph = Graph(7)

# graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(3,4)
graph.add_edge(3,5)
graph.add_edge(4,5)
graph.add_edge(4,6)


print(BFS3(graph,1))

# print(graph.adj)

# print(is_connected(graph))


graph = generate_random_graph(7,6)

print(is_connected(graph))

# max number of edges = v*(v-1)/2



# N = 20
# connected = [ 0 for i in range( (N*(N-1)//2)) ]

# x = [ i for i in range( (N*(N-1)//2)) ]

# for i in range(100):
    
#     for j in range(len(x)):

#         graph = generate_random_graph(N,j)
#         connected[j] += is_connected(graph)

# plt.plot(x,connected)
# plt.show()



