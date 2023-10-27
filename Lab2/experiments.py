from graph import * 
from DFS import *
from BFS import * 

import  random
import matplotlib.pyplot as plt
import numpy as np 

"""
Generates a graph with n vertices and e  randomly selected edges. 
Edges are selected by removing an edge from the list of possible edges e times. 
An exception is thrown if the specified edge count is less than zero 
or greater than the maximum possible edges for a graph of size n. 
"""
def generate_random_graph(n,e):
    graph = Graph(n)
    possible_edges = [(i,j) for i in range(n) for j in range(i+1,n)]
    if  e < 0 or e > len(possible_edges) : raise Exception('Illegal Edge Count') 

    for i in range(e):
        edge = possible_edges.pop(random.randint(0,len(possible_edges)-1))  
        graph.add_edge(edge[0], edge[1])  # add e random edges

    return graph



"""
Determines if a graph G is connected by checking that 
all nodes of G are reachable from a starting node.  
More specifically, performs BFS and checks that the conjunction of the marked array is True. 
"""
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

    # if all nodes are marked, graph is connected
    return all(marked.values())

"""
Determines if a graph G has a cycle by performing DFS 
on all independent components of the graph. 
If the DFS process reaches the same node twice, it indicates the presence of a cycle. 
"""
def has_cycle(G):
    cycle = False
    unchecked_vertices = [i for i in range(G.number_of_nodes())]
    marked = {}
    for node in G.adj:
        marked[node] = False


    # Repeat cycle checking process for each independent component of the graph 
    while(not all(marked.values())):
        for key in marked:
            if not marked[key]: 
                S = [key]
                break

        while len(S) != 0: 
            current_node = S.pop()
            if not marked[current_node]:
                marked[current_node] = True
                for node in G.adj[current_node]:

                    if not marked[node]:
                        S.append(node)
            else: 
                cycle = True
   
    return cycle 




"""
Plots the edge count vs the probability a graph has a cycle 
averaged over a specified number of trials 
"""
def experiment_1(V, trials):

    max = V + V//2
    cycle = [ 0 for i in range(max) ]
    num_edges = [ i for i in range(max) ]

    for i in range(trials):
        for j in range(len(num_edges)):
            graph = generate_random_graph(V,j)
            cycle[j] += has_cycle(graph)
    

    plt.title("Edge Count vs Probability of Cycle ")
    plt.xlabel('Edges')
    plt.ylabel('P(Has Cycle)')
    plt.plot(num_edges,np.divide(cycle,trials), "red")
    plt.show()


def experiment_2(V, trials):

    max_edges = (V*(V-1)//2) 
    connected = [ 0 for i in range(max_edges) ]
    num_edges = [ i for i in range(max_edges) ]

    for i in range(trials): 
        for j in range(len(num_edges)):
            graph = generate_random_graph(V,j)
            connected[j] += is_connected(graph)

    plt.title("Edge Count vs Probability of Connected Graph ")
    plt.xlabel('Edges')
    plt.ylabel('P(connected)')
    plt.plot(num_edges,np.divide(connected, trials), 'blue')
    plt.show()




graph = Graph(7)

# graph.add_edge(0,1)

graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(3,4)
graph.add_edge(3,5)
graph.add_edge(4,5)
graph.add_edge(4,6)


# print('DFS2', DFS2(graph,1,6))
# print('DFS3', DFS3(graph,1))

# print('BFS2', BFS2(graph,1,1))
# print('BFS3', BFS3(graph,1))




# experiment_1(50,1000)
# experiment_2(20,1000)
