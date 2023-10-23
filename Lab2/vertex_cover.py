from graph import * 
from experiments2 import generate_random_graph
import random


       
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
    
    C = set()
    vertex=[]

    for i in range(G.number_of_nodes()):
        if(G.adjacent_nodes(i) not in vertex):
            vertex.append(G.adjacent_nodes(i))
    

    while len(C)< (len(vertex)-1):
        if(is_vertex_cover(G, C)):
            return C

        value= random.randint(0, len(vertex)-1)
        val2=value
        v= vertex[val2]

        C.update(v)

    

g = generate_random_graph(5, 8)
print(approx2(g))





graph = Graph(7)
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(3,4)
graph.add_edge(3,5)
graph.add_edge(4,5)
graph.add_edge(4,6)



