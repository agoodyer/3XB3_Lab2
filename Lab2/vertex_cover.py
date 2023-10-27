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

def approx3(G):
    C = set()
    graph = copy(G)

    while not is_vertex_cover(graph,C):
        u = random.randint(0,graph.number_of_nodes()-1)
        adj = graph.adjacent_nodes(u)
        if len(adj) > 0:
            v = adj[random.randint(0, len(adj)-1)]
            remove_incident(graph,u)
            remove_incident(graph,v)
            C.add(u)
            C.add(v)
    
    return C

def MVC_edges(V, trials):

    max_edges = (V*(V-1)//2) 
    MVC_size = [ 0 for i in range(max_edges) ]
    approx1_size = [ 0 for i in range(max_edges) ]
    approx2_size = [ 0 for i in range(max_edges) ]
    approx3_size = [ 0 for i in range(max_edges) ]

    num_edges = [ i for i in range(max_edges) ]

    for i in range(trials): 
        for j in range(len(num_edges)):
            graph = generate_random_graph(V,j)
            approx1_size[j] += len(approx1(graph))
            approx2_size[j] += len(approx2(graph))
            approx3_size[j] += len(approx3(graph))
            MVC_size[j] += len(MVC(graph))
           

    plt.title("Edge Count vs Vertex Cover Size ")
    plt.xlabel('Edges')
    plt.ylabel('Size of VC')
    plt.plot(num_edges,np.divide(MVC_size, trials), 'red')
    plt.plot(num_edges,np.divide(approx1_size, trials), 'blue')
    plt.plot(num_edges,np.divide(approx2_size, trials), 'orange')
    plt.plot(num_edges,np.divide(approx3_size, trials), 'green')
    plt.legend(['MVC', 'approx1', 'approx2', 'approx3'])
    
    plt.show()



def generate_all_graphs(n):

    possible_edges = [(i,j) for i in range(n) for j in range(i+1,n)]
    all_graphs = []

    pow = power_set(possible_edges)

    for edge_set in pow: 
        graph = Graph(n)
        for edge in edge_set: 
            graph.add_edge(edge[0], edge[1])
        
        all_graphs.append(graph)
    
    return all_graphs


"""
Generates all possible graphs of size n and then determines the size difference between the approx1 and the MVC

"""
def worst_case(n):
    all_graphs = generate_all_graphs(n)

    worst_approx = set()
    worst_actual = set()
    max_diff = 0 

    for graph in all_graphs:
        approximation = approx1(graph)
        actual = MVC(graph) 

        diff = len(approximation) - len(actual)

        if diff > max_diff:
            worst_approx =  approximation
            worst_actual = actual
            max_diff = diff

    
    #uncomment to see actual and worst case approximate MVCs

    print("Worst case for n= ",n ," : ", max_diff)
    # print('actual: ', worst_actual)
    # print('approx: ', worst_approx)

    return max_diff



"""
Graphs the worst case difference between the MVC and approx1
for a graph of size n. Only works for small input sizes since generating
all graph configurations is extremely intensive. 
"""
def graph_worst_case(n):


    worst_difference = [ 0 for i in range(n+1) ]


    graph_size = [ i for i in range(n+1) ]

    for i in range(n+1): 
        worst_difference[i] = worst_case(i)

            
           

    plt.title("Graph Size vs Worst Case of approx1")
    plt.xlabel('Graph size')
    plt.ylabel('|MVC| - |approx1| ')
    plt.plot(graph_size,worst_difference, 'red')

    plt.legend(['Difference'])
    
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
# print(approx3(graph))
# print(test(graph))
# print(len(approx2(graph)))

# MVC_edges(8, 1000)

# generate_all_graphs(3)

# worst_case(5)

graph_worst_case(7)


