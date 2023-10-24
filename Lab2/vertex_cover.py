from graph import * 
from experiments import generate_random_graph
import random

import matplotlib.pyplot as plt
import numpy as np 

     
def copy(G):
    graph = Graph(G.number_of_nodes())
    for i in range(G.number_of_nodes()):
        graph.adj[i] = G.adj[i].copy()
    return graph 


def remove_incident(G, v):
    v_adjacent = G.adjacent_nodes(v) 
    for vertex in v_adjacent:
        G.adj[vertex] = [ u for u in G.adj[vertex] if u != v] # remove all instances of v from other adjacency list
    G.adj[v].clear() # wipe the adjacency list of v



def approx1(G):
    graph = copy(G)
    C = set()

    while(not is_vertex_cover(graph,C)):
        max_degree, max_vertex = 0,0
        for i in range(graph.number_of_nodes()):
            if(len(graph.adjacent_nodes(i)) > max_degree):
                max_degree, max_vertex = len(graph.adjacent_nodes(i)), i
        
        C.add(max_vertex)
        remove_incident(graph, max_vertex)

    return C

def approx2(G):
    graph = copy(G)
    C = set()
    vertex=[]

    for i in range(graph.number_of_nodes()):
        if(graph.adjacent_nodes(i) not in vertex):
            vertex.append(graph.adjacent_nodes(i))

    while len(C) < (len(vertex)-1):
        if(is_vertex_cover(graph, C)):
            return C

        value= random.randint(0, len(vertex)-1)
        val2=value
        v= vertex[val2]
        C.update(v)

    return C

def MVC_edges(V, trials):

    max_edges = (V*(V-1)//2) 
    MVC_size = [ 0 for i in range(max_edges) ]
    approx1_size, approx2_size  = [ 0 for i in range(max_edges) ], [ 0 for i in range(max_edges) ]

    num_edges = [ i for i in range(max_edges) ]

    for i in range(trials): 
        for j in range(len(num_edges)):
            graph = generate_random_graph(V,j)
            approx1_size[j] += len(approx1(graph))
            approx2_size[j] += len(approx2(graph))
            MVC_size[j] += len(MVC(graph))
           

    plt.title("Edge Count vs MVC Size ")
    plt.xlabel('Edges')
    plt.ylabel('Size of MVC')
    plt.plot(num_edges,np.divide(MVC_size, trials), 'blue')
    plt.plot(num_edges,np.divide(approx1_size, trials), 'red')
    plt.plot(num_edges,np.divide(approx2_size, trials), 'green')
    
    plt.show()







graph = Graph(7)
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(3,4)
graph.add_edge(3,5)
graph.add_edge(4,5)
graph.add_edge(4,6)

# print(MVC(graph))
# print(approx1(graph))
# print(approx2(graph))
# print(len(approx2(graph)))

MVC_edges(8, 1000)