from graph import * 
from DFS import *
from BFS import * 

import  random
import matplotlib.pyplot as plt
import numpy as np 

'''
Generates a graph with n vertices and e  randomly selected edges. 
Edges are selected by removing an edge from the list of possible edges e times. 
An exception is thrown if the specified edge count is less than zero 
or greater than the maximum possible edges for a graph of size n. 
'''
def generate_random_graph(n,e):
    graph = Graph(n)
    possible_edges = [(i,j) for i in range(n) for j in range(i+1,n)]
    if  e < 0 or e > len(possible_edges) : raise Exception('Illegal Edge Count') 

    for i in range(e):
        edge = possible_edges.pop(random.randint(0,len(possible_edges)-1))  
        graph.add_edge(edge[0], edge[1])  # add e random edges

    return graph


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



def has_cycle(G):
    cycle = False
    unchecked_vertices = [i for i in range(G.number_of_nodes())]
    marked = {}
    for node in G.adj:
        marked[node] = False


    while(not all(marked.values())):
        for key in marked:
            if not marked[key]: 
                S = [key]
                break

        # print(marked)
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


def experiment_2(V, trials):
    connected = [ 0 for i in range( (V*(V-1)//2)) ]

    num_edges = [ i for i in range( (V*(V-1)//2)) ]

    for i in range(trials):
        
        for j in range(len(num_edges)):

            graph = generate_random_graph(V,j)
            connected[j] += is_connected(graph)

    plt.plot(num_edges,connected)
  
    plt.show()




def experiment_1(V, trials):
    cycle = [ 0 for i in range(V + V//4) ]

    num_edges = [ i for i in range(V + V//4) ]

    for i in range(trials):
        
        for j in range(len(num_edges)):

            graph = generate_random_graph(V,j)
            cycle[j] += has_cycle(graph)

    plt.plot(num_edges,cycle)

    plt.axvline(x = V-1, color = 'b', label = 'axvline - full height')
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



print(BFS3(graph,1))


# experiment_1(30,100)
# experiment_2(20,100)
