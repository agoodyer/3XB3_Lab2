from graph import * 
from experiments2 import generate_random_graph


def check_vertex_cover(G, C):
    pass 





def remove_incident(G, v):
    v_adjacent = G.adjacent_nodes(v)
    
    for vertex in v_adjacent:
        G.adj[vertex] = [ u for u in G.adj[vertex] if u != v] # remove all instances of v from other adjacency list
    G.adj[v].clear() # wipe the adjacency list of v



def approx1(G):
    C = set()
    max_degree, max_vertex = 0,0
    for i in range(G.number_of_nodes()):
        if(len(G.adjacent_nodes(i)) > max_degree):
            max_degree, max_vertex = len(G.adjacent_nodes(i)), i
    
    C.add(max_vertex)
    remove_incident(G, max_vertex)


g = generate_random_graph(5, 8)

approx1(g)


graph = Graph(7)
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,4)
graph.add_edge(3,4)
graph.add_edge(3,5)
graph.add_edge(4,5)
graph.add_edge(4,6)